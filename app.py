import streamlit as st
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


def show_home():
    texts = Texts()
    st.header("Informações Gerais")
    for attr in ["text1", "text2", "text3"]:
        st.markdown(getattr(texts, attr)(), unsafe_allow_html=True)


def show_qge():
    st.header("Química Geral Experimental")
    aula = st.selectbox("Selecione a aula:", AULAS_QGE)
    if aula == "Escolha uma Aula":
        return
    try:
        texts = TextsQGE()
        st.write(texts.text1(), unsafe_allow_html=True)
        st.subheader("Recursos para esta aula:")
        st.markdown(
            "- Consulte a página correspondente na apostila\n"
            "- Revise o template de relatório\n"
            "- Dúvidas? Contate o professor via E-mail"
        )
        st.markdown(
            get_binary_file_downloader_html(
                "QGE/Apostila_QGE_2022_2.pdf", "Apostila"
            ),
            unsafe_allow_html=True,
        )
        st.markdown(
            get_binary_file_downloader_html(
                "QGE/Template_Relatorio_QGE.pdf", "Template Relatório"
            ),
            unsafe_allow_html=True,
        )
    except ImportError:
        st.error("Módulo de textos não encontrado!")


def show_qi():
    st.header("Química 1")
    escolha = st.selectbox("Selecione a aula:", AULAS_QI)
    if escolha == "1° Bimestre: Matéria e Modelos Atômicos":
        # Carrega e exibe o texto completo de verificação do 1º bimestre
        textos_qi = TextsQI()
        st.markdown(textos_qi.text1(), unsafe_allow_html=True)
    elif escolha != "Escolha uma Aula":
        st.info(f"Conteúdo de: {escolha}")


def show_qii():
    st.header("Química 2")
    escolha = st.selectbox("Selecione a aula:", AULAS_QII)
    if escolha == "1° Bimestre: Estequiometria e Estudos dos Gases":
        # Carrega e exibe o texto completo de verificação do 1º bimestre
        textos_qi = TextsQI()
        st.markdown(TextsQII().text1(), unsafe_allow_html=True)
        st.markdown(TextsQII().text2(), unsafe_allow_html=True)
        st.markdown(TextsQII().text3(), unsafe_allow_html=True)

    elif escolha != "Escolha uma Aula":
        # TODO: implementar conteúdo de Química 2
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
