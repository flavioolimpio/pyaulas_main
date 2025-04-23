import streamlit as st
import os
from streamlit_option_menu import option_menu
from utils.helpers import get_binary_file_downloader_html, local_css
from constants import AULAS_QI, AULAS_QII, AULAS_QGE
from texts import Texts
from texts_qge import TextsQGE
from texts_qi import TextsQI
from texts_qii import TextsQII


def setup_page():
    st.set_page_config(
        page_title="PyAulas", layout="wide", initial_sidebar_state="expanded"
    )
    local_css("style/style.css")


def sidebar_navigation():
    with st.sidebar:
        selected = option_menu(
            "Navegação",
            [
                "Página Inicial",
                "Química Geral Experimental",
                "Química 1",
                "Química 2",
                "Contato",
            ],
            icons=[
                "house-fill",
                "book",
                "book-fill",
                "book",
                "chat-left-text",
            ],
            menu_icon="cast",
            default_index=0,
        )
    return selected


def download_pdfs(folder: str, files: dict):
    """
    Gera botões de download para vários PDFs.
    `folder` é a pasta onde estão os arquivos.
    `files` é um dict no formato { 
        "Label do Botão": "nome_do_arquivo.pdf",
        ...
    }
    """
    for label, filename in files.items():
        path = os.path.join(folder, filename)
        if os.path.exists(path):
            with open(path, "rb") as f:
                data = f.read()
            st.download_button(
                label=label,
                data=data,
                file_name=filename,
                mime="application/pdf",
            )
        else:
            st.warning(f"Arquivo não encontrado: `{folder}/{filename}`")

def download_docx(folder: str, label: str, filename: str):
    """Helper para baixar um .docx"""
    path = os.path.join(folder, filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
        st.download_button(
            label=label,
            data=data,
            file_name=filename,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
    else:
        st.warning(f"Arquivo não encontrado: `{folder}/{filename}`")

def show_home():
    texts = Texts()
    st.header("Informações Gerais")
    for attr in ["text1", "text2", "text3"]:
        st.markdown(getattr(texts, attr)(), unsafe_allow_html=True)

def show_qge():
    st.header("Química Geral Experimental")

    # Plano de Aula (é só chamar download_pdfs)
    download_pdfs("qge", {
        "📄 Baixar Plano de Aula": "PlanodeEnsinoQGE.pdf"
    })

    st.markdown("---")
    aula = st.selectbox("Selecione a aula:", AULAS_QGE)
    if aula == "Escolha uma Aula":
        return

    # Conteúdo da aula
    try:
        texts = TextsQGE()
        st.markdown(texts.text1(), unsafe_allow_html=True)
    except Exception:
        st.error("Não foi possível carregar o conteúdo da aula.")

    # Se for a primeira aula, adiciona Apostila (PDF) e Template (DOCX)
    if aula == "Aula 1: Apresentação da disciplina e normas de segurança":
        st.subheader("Links úteis e material de apoio")

        # Apostila em PDF via download_pdfs
        download_pdfs("qge", {
            "📚 Baixar Apostila (PDF)": "Apostila_QGE.pdf"
        })

        # Template de Relatório em DOCX via helper
        download_docx("qge", "📝 Baixar Template de Relatório (Word)", "Template_Relatorio_QGE.docx")

def show_qi():
    st.header("Química 1")

    # Plano de Ensino
    download_pdfs("qi", {
        "📄 Baixar Plano de Ensino": "PlanoEnsinoQuimica1.pdf"
    })

    st.markdown("---")
    escolha = st.selectbox("Selecione a aula:", AULAS_QI)

    if escolha == "1° Bimestre: Matéria e Modelos Atômicos":
        st.markdown(TextsQI().text1(), unsafe_allow_html=True)

        download_pdfs("qi", {
            "✏️ Baixar Lista de Exercícios 1° Bimestre":   "ListaQuimica1BI_v01.pdf",
            "📄 Baixar Aula 01: Matéria":                  "Aula_01_Materia.pdf",
            "📄 Baixar Aula 02: Modelos Atômicos":         "Aula_02_Modelos Atomicos.pdf",
            # adicione novos arquivos aqui sem repetir código...
        })

    elif escolha != "Escolha uma Aula":
        st.info(f"Conteúdo de: {escolha}")


def show_qii():
    st.header("Química 2")

    # Plano de Ensino
    download_pdfs("qii", {
        "📄 Baixar Plano de Ensino": "PlanoEnsinoQuimica2.pdf"
    })

    st.markdown("---")
    escolha = st.selectbox("Selecione a aula:", AULAS_QII)

    if escolha == "1° Bimestre: Estequiometria e Estudos dos Gases":
        st.markdown(TextsQII().text1(), unsafe_allow_html=True)

        download_pdfs("qii", {
            "✏️ Baixar Lista de Exercícios 1° Bimestre": "ListaQuimicaii1BI.pdf",
            "📑 Baixar Slides de Estequiometria":       "Aula_Estequiometria.pdf"
        })

    elif escolha != "Escolha uma Aula":
        st.info(f"Conteúdo de: {escolha}")



def show_contact():
    st.header("Entre em contato comigo!!")
    contact_form = """
    <form action="https://formsubmit.co/flavio.neto@ifg.edu.br" method="post">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Seu nome" required>
        <input type="email" name="email" placeholder="Seu email" required>
        <textarea name="message" placeholder="Digite sua mensagem aqui"></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)


def main():
    setup_page()
    choice = sidebar_navigation()

    if choice == "Página Inicial":
        show_home()
    elif choice == "Química Geral Experimental":
        show_qge()
    elif choice == "Química 1":
        show_qi()
    elif choice == "Química 2":
        show_qii()
    elif choice == "Contato":
        show_contact()


if __name__ == "__main__":
    main()
