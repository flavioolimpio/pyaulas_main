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

        # Apostila em PDF via download_pdfs
        download_pdfs("qge", {
            "📚 Baixar Apostila (PDF)": "Apostila_QGE.pdf"
        })

        # Template de Relatório em DOCX via helper
        download_docx("qge", "📝 Baixar Template de Relatório (Word)", "Template_Relatorio_QGE.docx")

# (Supondo que a classe TextsQI e a função download_pdfs já estão no seu código)

def show_qi():
    st.header("Química 1")

    # Plano de Ensino
    download_pdfs("qi", {
        "📄 Baixar Plano de Ensino": "PlanoEnsinoQuimica1.pdf"
    })

    # Template de Relatório em DOCX via helper
    download_docx("qi", "📝 Baixar Template de Relatório (Word)", "Template_Relatorio_QGE.docx")

    st.markdown("---")
    
    # A lista AULAS_QI já deve estar atualizada
    escolha = st.selectbox("Selecione a aula:", AULAS_QI)

    # Conteúdo do 1º Bimestre (sem alterações)
    if escolha == "1° Bimestre: Matéria e Modelos Atômicos":
        st.markdown(TextsQI().text1(), unsafe_allow_html=True)

        download_pdfs("qi", {
            "✏️ Baixar Lista de Exercícios 1° Bimestre": "ListaQuimica1BI_v01.pdf",
            "📄 Baixar Aula 01: Matéria": "Aula_01_Materia.pdf",
            "📄 Baixar Aula 02: Modelos Atômicos": "Aula_02_Modelos Atomicos.pdf",
        })

    # --- NOVO BLOCO PARA O 2º BIMESTRE ---
    elif escolha == "2° Bimestre: Propriedades periódicas e Ligações Químicas":
        # Chama o novo texto que criamos para o 2º Bimestre
        st.markdown(TextsQI().text2(), unsafe_allow_html=True)

        # Adicione aqui os arquivos PDF correspondentes ao 2º Bimestre
        download_pdfs("qi", {
            "✏️ Baixar Lista de Exercícios 2° Bimestre": "ListaQuimica2BI.pdf",
            "📄 Baixar Aula 03: Propriedades Periódicas": "Aula_Propriedades_Periodicas.pdf",
            "📄 Baixar Aula 04: Ligações Químicas": "Aula_Ligacoes_Quimicas_IFG.pdf",
            # adicione novos arquivos aqui conforme necessário...
        })

    # --- NOVO BLOCO PARA O 3º BIMESTRE ---
    elif escolha == "3° Bimestre: Geometria Molecular, Carga Formal, Ressonância, Polaridade e Forças Intermoleculares":
        st.markdown(TextsQI().text4(), unsafe_allow_html=True)

        download_pdfs("qi", {
            "✏️ Baixar Lista de Exercícios 3° Bimestre": "Lista_3_BI_Quimica_1.pdf",
            "📄 Baixar Aula: Geometria Molecular, Carga Formal, Ressonância, Polaridade e Forças Intermoleculares": "Aula_3BI.pdf",
        })

    # --- NOVO BLOCO PARA O 4º BIMESTRE ---
    elif escolha == "4° Bimestre: Estequiometria":
        st.markdown(TextsQI().text4(), unsafe_allow_html=True)

        download_pdfs("qi", {
            "✏️ Baixar Lista de Exercícios 4° Bimestre": "ListaQuimicai4BI.pdf",
            "📑 Baixar Slides de Estequiometria":       "Aula_Estequiometria.pdf"
        })

    # Mensagem padrão
    elif escolha != "Escolha uma Aula":
        st.info(f"Conteúdo de: {escolha}")


def show_qii():
    st.header("Química 2")

    # Plano de Ensino
    download_pdfs("qii", {
        "📄 Baixar Plano de Ensino": "PlanoEnsinoQuimica2.pdf"
    })

    download_docx("qii", "📝 Baixar Template de Relatório (Word)", "Template_Relatorio_QGE.docx")
    st.markdown("---")
    
    # A lista AULAS_QII já deve estar atualizada com a nova opção
    escolha = st.selectbox("Selecione a aula:", AULAS_QII)

    # --- Bloco do 1º Bimestre (sem alterações) ---
    if escolha == "1° Bimestre: Estequiometria e Estudos dos Gases":
        st.markdown(TextsQII().text1(), unsafe_allow_html=True)

        download_pdfs("qii", {
            "✏️ Baixar Lista de Exercícios 1° Bimestre": "ListaQuimicaii1BI.pdf",
            "📑 Baixar Slides de Estequiometria":       "Aula_Estequiometria.pdf"
        })

    # --- NOVO BLOCO PARA O 2º BIMESTRE ---
    elif escolha == "2° Bimestre: Termoquímica e Eletroquímica":
        st.markdown(TextsQII().text2(), unsafe_allow_html=True)

        # Adicione aqui os arquivos PDF correspondentes ao 2º Bimestre
        download_pdfs("qii", {
            "✏️ Baixar Lista de Exercícios 2° Bimestre": "ListaQuimicaii2BI.pdf",
            "📑 Baixar Slides de Termodinâmica":             "Aula_06_Termodinamica.pdf"
        })

    # --- NOVO BLOCO PARA O 3º BIMESTRE ---
    elif escolha == "3° Bimestre: Eletroquímica, Propriedades Coligativas":
        st.markdown(TextsQII().text3(), unsafe_allow_html=True)

        # Adicione aqui os arquivos PDF correspondentes ao 3º Bimestre
        download_pdfs("qii", {
            "✏️ Baixar Lista de Exercícios 3° Bimestre": "ListaQuimicaii3BI.pdf",
            "📑 Baixar Slides de Eletroquímica":             "Aula_07_Eletroquimica.pdf"
        })
    
    # --- NOVO BLOCO PARA O 4º BIMESTRE ---
    elif escolha == "4° Bimestre: Equilibrio Químico":  
        st.markdown(TextsQII().text4(), unsafe_allow_html=True)

        # Adicione aqui os arquivos PDF correspondentes ao 3º Bimestre
        download_pdfs("qii", {
            "✏️ Baixar Lista de Exercícios 4° Bimestre": "ListaQuimicaii4BI.pdf",
            "📑 Baixar Slides de Equilíbrio Químico":             "Aula_EquilibrioQuimico.pdf"
        })

    # --- Bloco final (sem alterações) ---
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
