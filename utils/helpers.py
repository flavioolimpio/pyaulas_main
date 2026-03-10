import os
import base64
import json
import streamlit as st

PROGRESSO_FILE = "progresso.json"


def get_binary_file_downloader_html(bin_file, file_label="File"):  # noqa: E501
    """Gera o link HTML para download de um arquivo binário."""
    with open(bin_file, "rb") as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = (
        f"<h2 style='text-align: justify; color: black;'>"
        f"<a href=\"data:application/octet-stream;base64,{bin_str}\" "
        f"download=\"{os.path.basename(bin_file)}\">Baixar {file_label}</a></h2>"
    )
    return href


def local_css(file_name):
    """Carrega um arquivo CSS local e injeta no Streamlit."""
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def carregar_progresso():
    """Carrega o progresso do arquivo JSON."""
    if os.path.exists(PROGRESSO_FILE):
        with open(PROGRESSO_FILE, "r") as f:
            return json.load(f)
    return {}


def salvar_progresso(progresso):
    """Salva o progresso no arquivo JSON."""
    with open(PROGRESSO_FILE, "w") as f:
        json.dump(progresso, f, indent=2)


def toggle_conteudo(conteudo_id: str):
    """Marca/desmarca um conteúdo como ministrado."""
    progresso = carregar_progresso()
    if conteudo_id in progresso:
        progresso[conteudo_id] = not progresso[conteudo_id]
    else:
        progresso[conteudo_id] = True
    salvar_progresso(progresso)
    return progresso.get(conteudo_id, False)


def is_conteudo_ministrado(conteudo_id: str) -> bool:
    """Verifica se um conteúdo foi marcado como ministrado."""
    progresso = carregar_progresso()
    return progresso.get(conteudo_id, False)