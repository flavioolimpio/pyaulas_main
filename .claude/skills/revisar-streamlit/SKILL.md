---
description: Use esta skill quando o usuário pedir revisão, melhoria, refatoração ou diagnóstico de páginas Streamlit em Python.
---

# Revisar aplicação Streamlit

## Objetivo

Revisar código Streamlit com foco em legibilidade, organização, usabilidade e manutenção.

## Procedimento

1. Identifique o arquivo principal da aplicação, geralmente `app.py`, `main.py` ou arquivos dentro de `pages/`.
2. Verifique se há imports desnecessários, duplicação de código ou blocos muito longos.
3. Avalie se a interface está clara para o usuário final.
4. Preserve o comportamento existente, salvo se o usuário pedir mudança funcional.
5. Sugira alterações pequenas e incrementais.

## Critérios de qualidade

- Código legível.
- Separação entre lógica e interface.
- Uso adequado de `st.title`, `st.header`, `st.subheader`, `st.markdown` e `st.sidebar`.
- Evitar repetição.
- Evitar variáveis globais desnecessárias.
- Manter textos em português claro.

## Saída esperada

Apresente diagnóstico curto, problemas encontrados, alterações sugeridas e código corrigido ou patch quando apropriado.
