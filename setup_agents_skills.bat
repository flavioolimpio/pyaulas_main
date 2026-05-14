@echo off
setlocal enabledelayedexpansion

echo ============================================
echo Configurando AGENTS.md, CLAUDE.md e Skills
echo Projeto: PyAulas
echo ============================================
echo.

REM Garante que o script esta sendo executado na pasta atual do projeto
set "PROJECT_DIR=%CD%"

echo Pasta atual:
echo %PROJECT_DIR%
echo.

REM Cria estrutura de pastas
if not exist ".claude" mkdir ".claude"
if not exist ".claude\skills" mkdir ".claude\skills"

if not exist ".claude\skills\revisar-streamlit" mkdir ".claude\skills\revisar-streamlit"
if not exist ".claude\skills\escrever-aula-quimica" mkdir ".claude\skills\escrever-aula-quimica"
if not exist ".claude\skills\gerar-exercicios-quimica" mkdir ".claude\skills\gerar-exercicios-quimica"
if not exist ".claude\skills\revisar-codigo-python" mkdir ".claude\skills\revisar-codigo-python"
if not exist ".claude\skills\preparar-commit" mkdir ".claude\skills\preparar-commit"

REM Cria pastas globais tambem
if not exist "%USERPROFILE%\.codex" mkdir "%USERPROFILE%\.codex"
if not exist "%USERPROFILE%\.claude" mkdir "%USERPROFILE%\.claude"
if not exist "%USERPROFILE%\.claude\skills" mkdir "%USERPROFILE%\.claude\skills"

REM Faz backup se os arquivos ja existirem
set "STAMP=%DATE:/=-%_%TIME::=-%"
set "STAMP=%STAMP: =0%"

if exist "AGENTS.md" copy "AGENTS.md" "AGENTS.md.bak_%STAMP%" >nul
if exist "CLAUDE.md" copy "CLAUDE.md" "CLAUDE.md.bak_%STAMP%" >nul
if exist "%USERPROFILE%\.codex\AGENTS.md" copy "%USERPROFILE%\.codex\AGENTS.md" "%USERPROFILE%\.codex\AGENTS.md.bak_%STAMP%" >nul

echo Criando AGENTS.md...

> "AGENTS.md" (
echo # AGENTS.md
echo.
echo ## Contexto do projeto
echo.
echo Este projeto se chama PyAulas. É uma aplicação em Python com Streamlit para disponibilizar materiais didáticos, textos explicativos, aulas, exercícios e recursos de Química Geral Experimental.
echo.
echo ## Regras gerais
echo.
echo - Responder em português do Brasil, salvo quando eu pedir outro idioma.
echo - Preservar a clareza didática para estudantes do ensino técnico/integrado.
echo - Antes de alterar código, explicar brevemente o plano.
echo - Evitar mudanças grandes sem necessidade.
echo - Preferir soluções simples, legíveis e fáceis de manter.
echo - Não remover funcionalidades existentes sem avisar.
echo - Quando alterar arquivos Python, verificar imports, nomes de variáveis e possíveis erros de execução.
echo.
echo ## Stack
echo.
echo - Python
echo - Streamlit
echo - Markdown
echo - pandas, matplotlib e bibliotecas científicas quando necessário
echo.
echo ## Comandos úteis
echo.
echo - Rodar o app: `streamlit run app.py`
echo - Instalar dependências: `pip install -r requirements.txt`
echo.
echo ## Estilo de código
echo.
echo - Usar nomes de variáveis claros.
echo - Separar funções quando o código ficar longo.
echo - Evitar duplicação.
echo - Manter textos didáticos em português claro.
echo - Não misturar lógica pesada diretamente na interface Streamlit quando puder separar em funções.
echo.
echo ## Segurança
echo.
echo - Não inserir chaves de API, senhas ou tokens no código.
echo - Não modificar arquivos de configuração sensíveis sem confirmação.
echo - Não apagar arquivos ou conteúdos didáticos sem confirmação.
)

echo Criando CLAUDE.md...

> "CLAUDE.md" (
echo # CLAUDE.md
echo.
echo ## Projeto
echo.
echo PyAulas é um projeto em Python/Streamlit para organizar e disponibilizar aulas, materiais didáticos e atividades de Química Geral Experimental.
echo.
echo ## Como o Claude deve ajudar
echo.
echo - Atuar como assistente de desenvolvimento e revisão didática.
echo - Sugerir melhorias de código sem reescrever tudo desnecessariamente.
echo - Manter a linguagem didática, objetiva e adequada a estudantes.
echo - Quando eu pedir uma alteração, indicar quais arquivos devem ser modificados.
echo - Quando possível, propor uma solução incremental.
echo.
echo ## Preferências
echo.
echo - Responder em português do Brasil.
echo - Ser direto, técnico e objetivo.
echo - Para código, preferir exemplos completos e executáveis.
echo - Explicar erros de forma prática, com o comando ou arquivo que precisa ser ajustado.
echo.
echo ## Cuidados
echo.
echo - Não apagar conteúdo didático sem confirmação.
echo - Não mudar a estrutura do projeto sem justificar.
echo - Não criar dependências novas sem explicar por que são necessárias.
)

echo Criando skill: revisar-streamlit...

> ".claude\skills\revisar-streamlit\SKILL.md" (
echo ---
echo description: Use esta skill quando o usuário pedir revisão, melhoria, refatoração ou diagnóstico de páginas Streamlit em Python.
echo ---
echo.
echo # Revisar aplicação Streamlit
echo.
echo ## Objetivo
echo.
echo Revisar código Streamlit com foco em legibilidade, organização, usabilidade e manutenção.
echo.
echo ## Procedimento
echo.
echo 1. Identifique o arquivo principal da aplicação, geralmente `app.py`, `main.py` ou arquivos dentro de `pages/`.
echo 2. Verifique se há imports desnecessários, duplicação de código ou blocos muito longos.
echo 3. Avalie se a interface está clara para o usuário final.
echo 4. Preserve o comportamento existente, salvo se o usuário pedir mudança funcional.
echo 5. Sugira alterações pequenas e incrementais.
echo.
echo ## Critérios de qualidade
echo.
echo - Código legível.
echo - Separação entre lógica e interface.
echo - Uso adequado de `st.title`, `st.header`, `st.subheader`, `st.markdown` e `st.sidebar`.
echo - Evitar repetição.
echo - Evitar variáveis globais desnecessárias.
echo - Manter textos em português claro.
echo.
echo ## Saída esperada
echo.
echo Apresente diagnóstico curto, problemas encontrados, alterações sugeridas e código corrigido ou patch quando apropriado.
)

echo Criando skill: escrever-aula-quimica...

> ".claude\skills\escrever-aula-quimica\SKILL.md" (
echo ---
echo description: Use esta skill quando o usuário pedir criação, revisão ou expansão de textos didáticos de Química para aulas, apostilas, atividades ou páginas do PyAulas.
echo ---
echo.
echo # Escrever aula de Química
echo.
echo ## Objetivo
echo.
echo Produzir textos didáticos de Química em português, com linguagem clara, rigor conceitual e progressão pedagógica.
echo.
echo ## Público-alvo
echo.
echo Estudantes do ensino técnico/integrado ou graduação inicial, conforme o contexto do pedido.
echo.
echo ## Procedimento
echo.
echo 1. Identifique o tema químico central.
echo 2. Defina os pré-requisitos conceituais.
echo 3. Explique o conceito de forma progressiva.
echo 4. Inclua exemplos quando forem úteis.
echo 5. Evite simplificações conceitualmente incorretas.
echo 6. Quando houver cálculo, mostre as etapas.
echo 7. Finalize com uma síntese curta ou atividade.
echo.
echo ## Estilo
echo.
echo - Linguagem clara e objetiva.
echo - Tom didático.
echo - Usar notação química correta.
echo - Evitar excesso de informalidade.
echo - Não inventar dados experimentais.
echo.
echo ## Saída esperada
echo.
echo Organize a resposta em título, objetivos, introdução, desenvolvimento conceitual, exemplo ou aplicação, atividade proposta e resumo final quando adequado.
)

echo Criando skill: gerar-exercicios-quimica...

> ".claude\skills\gerar-exercicios-quimica\SKILL.md" (
echo ---
echo description: Use esta skill quando o usuário pedir criação de exercícios, listas, questões, atividades avaliativas ou gabaritos comentados de Química.
echo ---
echo.
echo # Gerar exercícios de Química
echo.
echo ## Objetivo
echo.
echo Criar exercícios de Química adequados ao nível dos estudantes, com enunciados claros e gabarito comentado.
echo.
echo ## Procedimento
echo.
echo 1. Identifique o tema e o nível da turma.
echo 2. Crie questões com dificuldade progressiva.
echo 3. Evite ambiguidades no enunciado.
echo 4. Inclua dados numéricos suficientes quando houver cálculo.
echo 5. Use unidades corretamente.
echo 6. Forneça gabarito comentado quando solicitado.
echo.
echo ## Tipos de questão
echo.
echo - Conceituais.
echo - Cálculo.
echo - Interpretação de experimento.
echo - Múltipla escolha.
echo - Questões discursivas.
echo.
echo ## Saída esperada
echo.
echo Apresente a lista organizada e, se solicitado, o gabarito ao final.
)

echo Criando skill: revisar-codigo-python...

> ".claude\skills\revisar-codigo-python\SKILL.md" (
echo ---
echo description: Use esta skill quando o usuário pedir revisão de código, identificação de bugs, refatoração ou melhoria de qualidade em arquivos Python.
echo ---
echo.
echo # Revisar código Python
echo.
echo ## Objetivo
echo.
echo Revisar código Python com foco em correção, clareza, manutenção e segurança.
echo.
echo ## Procedimento
echo.
echo 1. Leia os arquivos relevantes antes de sugerir alterações.
echo 2. Identifique erros de sintaxe, imports faltantes e variáveis indefinidas.
echo 3. Verifique se há duplicação ou funções muito longas.
echo 4. Prefira mudanças pequenas e testáveis.
echo 5. Explique qualquer alteração que possa mudar comportamento.
echo 6. Não adicionar dependências novas sem necessidade.
echo.
echo ## Checklist
echo.
echo - O código executa?
echo - Os imports estão corretos?
echo - Os nomes são claros?
echo - Há repetição evitável?
echo - Há tratamento de erro quando necessário?
echo - Há risco de apagar dados?
echo - O código continua compatível com Streamlit?
echo.
echo ## Saída esperada
echo.
echo Forneça problemas encontrados, correções recomendadas, código corrigido e comandos para testar.
)

echo Criando skill: preparar-commit...

> ".claude\skills\preparar-commit\SKILL.md" (
echo ---
echo description: Use esta skill quando o usuário pedir revisão final antes de commit, organização de alterações, mensagem de commit ou preparação para enviar ao GitHub.
echo ---
echo.
echo # Preparar commit
echo.
echo ## Objetivo
echo.
echo Ajudar a revisar alterações antes de commit, organizar arquivos modificados e sugerir uma mensagem de commit clara.
echo.
echo ## Procedimento
echo.
echo 1. Verifique quais arquivos foram modificados.
echo 2. Identifique alterações principais.
echo 3. Aponte arquivos que parecem não relacionados.
echo 4. Sugira testes ou comandos de verificação.
echo 5. Escreva uma mensagem de commit objetiva.
echo.
echo ## Estilo da mensagem
echo.
echo Use mensagens curtas, no imperativo ou em português claro.
echo.
echo Exemplos:
echo.
echo - Adiciona página de aulas experimentais
echo - Corrige navegação lateral do Streamlit
echo - Organiza materiais de Química Geral
echo.
echo ## Saída esperada
echo.
echo Apresente resumo das mudanças, riscos, testes recomendados e sugestão de mensagem de commit.
)

echo Criando AGENTS.md global para Codex...

> "%USERPROFILE%\.codex\AGENTS.md" (
echo # AGENTS.md global
echo.
echo ## Preferências globais
echo.
echo - Responder em português do Brasil.
echo - Ser objetivo e técnico.
echo - Antes de mudanças grandes, apresentar um plano.
echo - Evitar alterar arquivos não relacionados à tarefa.
echo - Não inserir dependências novas sem justificar.
echo - Priorizar código simples, legível e testável.
echo - Não apagar arquivos sem confirmação.
)

echo.
echo ============================================
echo Verificando PATH do Claude e Codex
echo ============================================
echo.

REM Adiciona Claude ao PATH do usuario, se existir e se ainda nao estiver no PATH
if exist "%USERPROFILE%\.local\bin\claude.exe" (
    echo Claude encontrado em: %USERPROFILE%\.local\bin\claude.exe
    echo Tentando adicionar %USERPROFILE%\.local\bin ao PATH do usuario...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "$p=[Environment]::GetEnvironmentVariable('Path','User'); if ($p -notlike '*%USERPROFILE%\.local\bin*') { [Environment]::SetEnvironmentVariable('Path', $p + ';%USERPROFILE%\.local\bin', 'User') }"
) else (
    echo Claude nao encontrado em %USERPROFILE%\.local\bin\claude.exe
)

REM Adiciona npm global ao PATH do usuario
if exist "%APPDATA%\npm" (
    echo Pasta npm global encontrada: %APPDATA%\npm
    echo Tentando adicionar %APPDATA%\npm ao PATH do usuario...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "$p=[Environment]::GetEnvironmentVariable('Path','User'); if ($p -notlike '*%APPDATA%\npm*') { [Environment]::SetEnvironmentVariable('Path', $p + ';%APPDATA%\npm', 'User') }"
)

echo.
echo ============================================
echo Concluido!
echo ============================================
echo.
echo Arquivos criados:
echo - AGENTS.md
echo - CLAUDE.md
echo - .claude\skills\revisar-streamlit\SKILL.md
echo - .claude\skills\escrever-aula-quimica\SKILL.md
echo - .claude\skills\gerar-exercicios-quimica\SKILL.md
echo - .claude\skills\revisar-codigo-python\SKILL.md
echo - .claude\skills\preparar-commit\SKILL.md
echo - %USERPROFILE%\.codex\AGENTS.md
echo.
echo IMPORTANTE:
echo Feche todos os CMD/PowerShell/Windows Terminal e abra de novo
echo para o PATH atualizar corretamente.
echo.
echo Depois teste:
echo.
echo     claude
echo     codex
echo.
pause
endlocal