import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title='Certidão de Óbito — Carapicuíba RP',
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove o espaço e o cabeçalho padrão do Streamlit para a aplicação parecer um portal único.
st.markdown(
    """<style>
    [data-testid="stHeader"], [data-testid="stToolbar"], footer, #MainMenu { visibility: hidden; height: 0; }
    .block-container { padding-top: .25rem; padding-bottom: 0; padding-left: 0; padding-right: 0; max-width: 100%; }
    [data-testid="stAppViewContainer"] { background: #f5f8f7; }
    iframe { border: 0 !important; }
    </style>""",
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "index.html"
html_content = html_path.read_text(encoding="utf-8")

# Formulário e prévia continuam dentro do HTML; a geração de PDF/PNG permanece no navegador.
components.html(html_content, height=1250, scrolling=True)
