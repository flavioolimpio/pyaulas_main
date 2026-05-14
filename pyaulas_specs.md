# PyAulas — Specs de Refatoração

**Contexto:** Portal educacional em Streamlit (PyAulas) que serve conteúdo de Química Geral, Química I, II, III e OBQ para alunos do IFG. Cada disciplina tem 4 bimestres, cada bimestre tem três blocos: Verificação de Aprendizagem, Atividades Complementares (links + vídeos) e Downloads (PDFs de aulas, listas, templates).

**Estado atual:** todo o conteúdo está hardcoded em arquivos `.py`. Estrutura repete entre disciplinas e entre bimestres, gerando duplicação difícil de manter.

**Objetivo desta refatoração:** separar conteúdo de apresentação. Eu (professor) quero editar bimestres sem mexer em código Python.

---

## 1. Arquitetura alvo

```
pyaulas/
├── app.py                        # entrypoint Streamlit (roteamento)
├── config.py                     # constantes globais (título, logo, contato)
├── components/
│   ├── __init__.py
│   ├── sidebar.py                # render do menu de navegação
│   ├── disciplina_page.py        # render genérico de qualquer disciplina
│   ├── bimestre_block.py         # render do bloco de 1 bimestre (verificação + complementares + downloads)
│   └── home.py                   # render da página inicial
├── content/                      # ← TODO conteúdo editável fica aqui
│   ├── home.md
│   ├── contato.md
│   ├── quimica_geral/
│   │   ├── _meta.yaml            # nome, ementa, plano de ensino, template
│   │   ├── bimestre_1.yaml
│   │   ├── bimestre_2.yaml
│   │   ├── bimestre_3.yaml
│   │   └── bimestre_4.yaml
│   ├── quimica_1/
│   │   └── ... (mesma estrutura)
│   ├── quimica_2/
│   ├── quimica_3/
│   └── obq/
├── static/
│   ├── planos_ensino/            # PDFs dos planos
│   ├── aulas/                    # PDFs das aulas (quimica1_b1_aula01.pdf, etc.)
│   ├── listas/                   # listas de exercícios
│   └── templates/                # template relatório .docx
├── utils/
│   ├── content_loader.py         # carrega e valida YAML/MD
│   └── paths.py                  # helpers de caminho
└── requirements.txt
```

**Por quê assim:** adicionar uma aula nova passa a ser editar 1 YAML + soltar 1 PDF em `static/`. Adicionar uma disciplina nova é criar 1 pasta em `content/`. Zero Python tocado pra conteúdo.

---

## 2. Modelo de dados

### `content/<disciplina>/_meta.yaml`

```yaml
nome: "Química 1"
slug: "quimica_1"
icone: "📘"
ordem: 3                          # ordem no menu lateral
ementa: |
  Texto curto opcional descrevendo a disciplina.
plano_ensino: "planos_ensino/quimica1.pdf"
template_relatorio: "templates/relatorio_quimica1.docx"   # opcional
```

### `content/<disciplina>/bimestre_N.yaml`

```yaml
titulo: "1º Bimestre: Matéria e Modelos Atômicos"

verificacao:
  descricao: "Revise os conceitos fundamentais abordados no primeiro bimestre e certifique-se de compreender cada item abaixo:"
  itens:
    - "Postulados da Teoria Atômica de Dalton e sua importância para o entendimento da constituição da matéria."
    - "Experimento de Rutherford e o modelo nuclear do átomo, incluindo conclusões sobre a eletrosfera e o núcleo."
    # ... resto dos itens

complementares:
  descricao: "Explore recursos online para aprofundar seu aprendizado:"
  links:
    - titulo: "PhET: Construa um Átomo"
      url: "https://phet.colorado.edu/..."
      descricao: "Monte diferentes átomos interativamente."
    - titulo: "Vídeo: Modelo Atômico de Thomson"
      url: "https://youtube.com/..."
      descricao: "Demonstração do tubo de raios catódicos."

downloads:
  - rotulo: "📝 Baixar Lista de Exercícios 1º Bimestre"
    arquivo: "listas/quimica1_b1_lista.pdf"
  - rotulo: "📄 Baixar Aula 01: Matéria"
    arquivo: "aulas/quimica1_b1_aula01.pdf"
  - rotulo: "📄 Baixar Aula 02: Modelos Atômicos"
    arquivo: "aulas/quimica1_b1_aula02.pdf"
```

**Regras:**
- Qualquer um dos três blocos (`verificacao`, `complementares`, `downloads`) é opcional — se faltar, o renderizador omite a seção.
- Arquivos em `downloads[].arquivo` e `_meta.plano_ensino` são caminhos relativos a `static/`.
- Validar no carregamento (schema simples com `pydantic` ou validação manual): se um PDF declarado não existir em `static/`, logar warning e mostrar o botão desabilitado com tooltip.

---

## 3. Componentes Streamlit

### `components/bimestre_block.py`
Função única `render_bimestre(bimestre: dict, static_dir: Path)` que:
1. Renderiza título centralizado (`st.markdown` com `<h2 style='text-align:center'>`).
2. Se existir `verificacao`: descrição + `st.markdown` com lista numerada gerada a partir de `itens`.
3. Se existir `complementares`: descrição + lista de bullets com links markdown `[titulo](url) – descricao`.
4. Se existir `downloads`: para cada item, `st.download_button` lendo o PDF de `static/`.

### `components/disciplina_page.py`
`render_disciplina(slug: str)`:
1. Carrega `_meta.yaml`.
2. Renderiza título da disciplina.
3. Botões de download para `plano_ensino` e `template_relatorio` (se existirem).
4. `st.selectbox` "Selecione a aula" populado com os títulos dos 4 bimestres encontrados na pasta.
5. Chama `render_bimestre()` com o YAML escolhido.

### `components/sidebar.py`
Lê todos os `_meta.yaml` em `content/`, ordena por campo `ordem`, monta navegação com `st.sidebar.radio` ou `st.page_link` (Streamlit ≥1.30 tem multipágina nativa — recomendo migrar pra isso se ainda não está usando).

### `app.py`
Roteamento mínimo. Se for multipágina nativa, cada disciplina vira um `pages/<slug>.py` de 3 linhas chamando `render_disciplina(slug)`.

---

## 4. `utils/content_loader.py`

Funções esperadas:

```python
def list_disciplinas() -> list[Disciplina]:
    """Varre content/, retorna lista ordenada por _meta.ordem."""

def load_disciplina_meta(slug: str) -> dict: ...

def load_bimestres(slug: str) -> list[dict]:
    """Retorna bimestres ordenados por número do arquivo."""

def load_markdown(path: str) -> str:
    """Para home.md, contato.md."""
```

Cachear com `@st.cache_data` — o conteúdo é estático em runtime.

---

## 5. Migração do conteúdo atual

Tarefa pro Claude Code, na ordem:

1. **Inventariar** o `.py` atual: identificar onde estão os strings de cada bimestre de cada disciplina.
2. **Extrair** cada bloco para o YAML correspondente em `content/<disciplina>/bimestre_N.yaml` seguindo o schema acima.
3. **Mover** os PDFs hoje servidos para `static/` com nomenclatura `<disciplina>_b<N>_<tipo>_<descricao>.pdf` (ex: `quimica1_b1_aula01.pdf`).
4. **Substituir** o código de renderização hardcoded pelos componentes genéricos.
5. **Validar** rodando localmente: cada disciplina × cada bimestre × cada download tem que continuar funcionando.

---

## 6. Padrões de código

- **Type hints** em todas as funções públicas dos `components/` e `utils/`.
- **Docstrings** curtas em português (estilo do Flávio).
- **Sem lógica de UI dentro de `utils/`** — utils só carrega e valida dados.
- **Imports** organizados: stdlib → terceiros → locais.
- **Constantes de path** centralizadas em `utils/paths.py` (`CONTENT_DIR`, `STATIC_DIR`, `ROOT_DIR`).
- **Sem strings mágicas de caminho** dentro de componentes — sempre via `paths.py`.

---

## 7. Não-objetivos (deixar pra depois)

Pra não inflar o escopo desta refatoração:
- Autenticação de alunos.
- Sistema de progresso/checklist persistente.
- Quiz interativo.
- Analytics.
- i18n.

Esses entram em uma rodada futura, depois que a base estiver limpa.

---

## 8. Critérios de aceitação

A refatoração está pronta quando:
- [ ] Nenhum conteúdo textual de aula está em `.py`.
- [ ] Adicionar um 5º bimestre (hipotético) é só criar `bimestre_5.yaml` — zero código tocado.
- [ ] Adicionar uma disciplina nova é só criar `content/nova_disciplina/` com `_meta.yaml` e bimestres — zero código tocado.
- [ ] Renomear ou esconder uma disciplina é editar `_meta.yaml`.
- [ ] Todos os botões de download do site atual continuam funcionando.
- [ ] `streamlit run app.py` sobe sem warnings.

---

## 9. Prompt sugerido pro Claude Code

> Estou refatorando o PyAulas (Streamlit). Anexei o documento de specs `pyaulas_specs.md` e o código atual. Quero que você:
>
> 1. Leia o `.py` atual e me mostre um inventário do conteúdo encontrado (disciplinas, bimestres, downloads).
> 2. Antes de tocar em qualquer coisa, proponha a estrutura final de pastas confirmando com o que está em specs.
> 3. Crie a estrutura `content/` e migre **um bimestre como exemplo** (Química 1, 1º bimestre) pra eu validar o YAML.
> 4. Depois que eu aprovar, migre o restante e implemente os componentes.
>
> Não pule pra implementação completa — faça incremental e me mostre o YAML do exemplo antes de seguir.
