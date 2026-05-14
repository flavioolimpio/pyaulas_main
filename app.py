from pathlib import Path

import streamlit as st
from streamlit_option_menu import option_menu
from constants import AULAS_QI, AULAS_QII, AULAS_QGE, AULAS_OBQ, BIMESTRES_QIII
from texts import Texts
from texts_qge import TextsQGE
from texts_qi import TextsQI
from texts_qii import TextsQII
from texts_qiii import TextsQIII
from texts_obq import TextsOBQ
from utils.helpers import carregar_progresso, local_css, toggle_conteudo


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
                "Química 1",
                "Química 2",
                "Química III",
                "Química Geral",
                "OBQ",
                "Contato",
            ],
            icons=[
                "house-fill",
                "book-fill",
                "book",
                "book",
                "flask-fill",
                "trophy-fill",
                "chat-left-text",
            ],
            menu_icon="cast",
            default_index=0,
        )
    return selected


@st.cache_data(show_spinner=False)
def read_binary_file(path: str) -> bytes:
    """Le um arquivo binario local para uso em botoes de download."""
    return Path(path).read_bytes()


def download_file(folder: str, label: str, filename: str, mime: str) -> None:
    """Renderiza um botao de download para um arquivo local."""
    path = Path(folder) / filename
    if not path.exists():
        st.warning(f"Arquivo nao encontrado: `{path.as_posix()}`")
        return

    st.download_button(
        label=label,
        data=read_binary_file(str(path)),
        file_name=filename,
        mime=mime,
    )


def download_pdfs(folder: str, files: dict[str, str]) -> None:
    """Gera botoes de download para varios PDFs."""
    for label, filename in files.items():
        download_file(folder, label, filename, "application/pdf")


def download_docx(folder: str, label: str, filename: str) -> None:
    """Gera botao de download para documentos Word."""
    download_file(
        folder,
        label,
        filename,
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )

def show_home():
    texts = Texts()
    st.header("Informações Gerais")
    for attr in ["text1", "text2", "text3"]:
        st.markdown(getattr(texts, attr)(), unsafe_allow_html=True)

def show_qge():
    st.header("Química Geral Experimental")

    st.markdown(
        """
        <div class="course-hero">
            <span class="course-badge">Laboratório</span>
            <h2>Química Geral Experimental</h2>
            <p style="text-align: justify; color: black;">
            Esta área reúne plano de ensino, apostila, orientações de segurança,
            roteiros e materiais de apoio para as atividades experimentais.
            Use os conteúdos como preparação para as práticas e como referência
            para elaboração dos relatórios.
            </p>
        </div>
        <div class="course-grid">
            <div class="course-card">
                <h3>Antes da aula</h3>
                <ul class="course-list">
                    <li>Leia o roteiro experimental.</li>
                    <li>Revise os conceitos teóricos envolvidos.</li>
                    <li>Anote dúvidas para discutir no laboratório.</li>
                </ul>
            </div>
            <div class="course-card">
                <h3>Durante a prática</h3>
                <ul class="course-list">
                    <li>Registre dados com atenção às unidades.</li>
                    <li>Observe normas de segurança e descarte.</li>
                    <li>Trabalhe com organização na bancada.</li>
                </ul>
            </div>
            <div class="course-card">
                <h3>Depois da aula</h3>
                <ul class="course-list">
                    <li>Organize resultados e cálculos.</li>
                    <li>Discuta fontes de erro experimental.</li>
                    <li>Use o template para estruturar o relatório.</li>
                </ul>
            </div>
        </div>
        <div class="course-alert">
            <h3>Atenção</h3>
            <p style="text-align: justify; color: black;">
            Em atividades experimentais, siga sempre as orientações do professor,
            utilize os equipamentos de proteção indicados e não execute procedimentos
            sem autorização.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

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
        st.markdown(TextsQI().text3(), unsafe_allow_html=True)

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


def show_qiii():
    st.header("Química III - Ensino Médio")
    
    texts = TextsQIII()
    conteudos_qiii = {
        "T1: Características do Carbono e Hibridização": (texts.text1, "1"),
        "T2: Estruturas Carbônicas": (texts.text2, "2"),
        "T3: Hidrocarbonetos": (texts.text3, "3"),
        "T4: Funções Oxigenadas": (texts.text4, "4"),
        "T5: Funções Nitrogenadas": (texts.text5, "5"),
        "T6: Isomeria": (texts.text6, "6"),
        "T7: Reações de Substituição": (texts.text7, "7"),
        "T8: Reações de Adição": (texts.text8, "8"),
        "T9: Oxirredução, Desidratação e Esterificação": (texts.text9, "9"),
        "P1: Aromatizador de Ambientes e Sachês Perfumados": (
            texts.text_pratico1,
            "pratico1",
        ),
        "P2: Teste da Proveta - Teor de Álcool na Gasolina": (
            texts.text_pratico2,
            "pratico2",
        ),
        "P3: Síntese de Ésteres (Essência de Frutas)": (
            texts.text_pratico3,
            "pratico3",
        ),
        "P4: Síntese do AAS (Ácido Acetilsalicílico)": (
            texts.text_pratico4,
            "pratico4",
        ),
    }
    
    with st.sidebar:
        st.markdown("---")
        st.subheader("Lembrete de Conteúdo")
        st.markdown("Marque os conteúdos já ministrados:")
        
        for numero_bimestre, (bimestre, aulas) in enumerate(BIMESTRES_QIII.items(), 1):
            st.caption(bimestre)
            for numero_aula, aula in enumerate(aulas, 1):
                conteudo_id = f"qiii_b{numero_bimestre}_a{numero_aula}"
                estado = carregar_progresso().get(conteudo_id, False)
                if st.checkbox(aula, value=estado, key=conteudo_id):
                    if not estado:
                        toggle = st.button("✓", key=f"btn_{conteudo_id}")
                        if toggle:
                            toggle_conteudo(conteudo_id)
                            st.rerun()
                else:
                    if estado:
                        toggle = st.button("↺", key=f"btn_{conteudo_id}")
                        if toggle:
                            toggle_conteudo(conteudo_id)
                            st.rerun()

    download_pdfs("qiii", {
        "📄 Baixar Plano de Ensino": "Plano_de_Ensino-Quimicalll-Aut2026.pdf"
    })
    
    download_docx("qiii", "📝 Baixar Template de Relatório (Word)", "Template_Relatorio_QGE.docx")
    
    st.markdown("---")
    
    bimestre = st.selectbox("Selecione o bimestre:", list(BIMESTRES_QIII))
    escolha = st.selectbox("Selecione o conteúdo:", BIMESTRES_QIII[bimestre])

    render_texto, topico = conteudos_qiii[escolha]
    st.markdown(render_texto(), unsafe_allow_html=True)
    mostrar_recursos(topico)


def mostrar_recursos(topico):
    """Mostra os recursos complementares para cada tópico."""
    texts = TextsQIII()
    recursos = texts.get_recursos(topico)
    
    if not recursos:
        return
    
    st.markdown("### 📚 Recursos Complementares")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**🔬 PHET Interativos**")
        if recursos.get("phet"):
            for titulo, url in recursos["phet"]:
                st.markdown(f"[{titulo}]({url})")
        else:
            st.markdown("*Em breve*")
            
    with col2:
        st.markdown("**📖 Khan Academy**")
        if recursos.get("khan"):
            for titulo, url in recursos["khan"]:
                st.markdown(f"[{titulo}]({url})")
        else:
            st.markdown("*Em breve*")
            
    with col3:
        st.markdown("**🎬 YouTube**")
        if recursos.get("youtube"):
            for titulo, url in recursos["youtube"]:
                st.markdown(f"[{titulo}]({url})")
        else:
            st.markdown("*Em breve*")


def show_obq():
    st.header("OBQ - Olimpiadas Brasileira de Química")
    
    escolha = st.selectbox("Selecione uma opção:", AULAS_OBQ)
    
    if escolha == "Sobre a OBQ":
        st.markdown(TextsOBQ().sobre(), unsafe_allow_html=True)
        
    elif escolha == "Videos de Resolução Comentada":
        st.markdown(TextsOBQ().videos(), unsafe_allow_html=True)
        
        st.markdown("### 📺 Vídeos Recomendados")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        st.info("Em breve: coleção completa de vídeos com resoluções comentadas!")
        
    elif escolha == "Cronograma 2026":
        st.markdown(TextsOBQ().cronograma(), unsafe_allow_html=True)
        
    elif escolha == "Materiais de Estudo":
        st.markdown(TextsOBQ().materiais(), unsafe_allow_html=True)
        
    elif escolha == "Recursos Complementares":
        st.markdown(TextsOBQ().recursos(), unsafe_allow_html=True)


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
    elif choice == "Química III":
        show_qiii()
    elif choice == "OBQ":
        show_obq()
    elif choice == "Química Geral":
        show_qge()
    elif choice == "Química 1":
        show_qi()
    elif choice == "Química 2":
        show_qii()
    elif choice == "Contato":
        show_contact()


if __name__ == "__main__":
    main()
