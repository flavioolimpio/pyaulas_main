import os
import base64
import streamlit as st


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