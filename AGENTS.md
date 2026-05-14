# AGENTS.md

## Contexto do projeto

Este projeto se chama PyAulas. É uma aplicação em Python com Streamlit para disponibilizar materiais didáticos, textos explicativos, aulas, exercícios e recursos de Química Geral Experimental.

## Regras gerais

- Responder em português do Brasil, salvo quando eu pedir outro idioma.
- Preservar a clareza didática para estudantes do ensino técnico/integrado.
- Antes de alterar código, explicar brevemente o plano.
- Evitar mudanças grandes sem necessidade.
- Preferir soluções simples, legíveis e fáceis de manter.
- Não remover funcionalidades existentes sem avisar.
- Quando alterar arquivos Python, verificar imports, nomes de variáveis e possíveis erros de execução.

## Stack

- Python
- Streamlit
- Markdown
- pandas, matplotlib e bibliotecas científicas quando necessário

## Comandos úteis

- Rodar o app: `streamlit run app.py`
- Instalar dependências: `pip install -r requirements.txt`

## Estilo de código

- Usar nomes de variáveis claros.
- Separar funções quando o código ficar longo.
- Evitar duplicação.
- Manter textos didáticos em português claro.
- Não misturar lógica pesada diretamente na interface Streamlit quando puder separar em funções.

## Segurança

- Não inserir chaves de API, senhas ou tokens no código.
- Não modificar arquivos de configuração sensíveis sem confirmação.
- Não apagar arquivos ou conteúdos didáticos sem confirmação.
