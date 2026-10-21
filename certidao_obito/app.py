import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title='Certidão de Óbito — Carapicuíba RP',
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title('Certidão de Óbito — Carapicuíba RP')
st.caption('Preenchimento de certidão de óbito para o servidor Carapicuíba RP.')

html_path = Path(__file__).parent / "index.html"
html_content = html_path.read_text(encoding="utf-8")

# O HTML mantém os formulários e a geração local do documento dentro do componente.
# Altura ampla para evitar cortar o formulário e a prévia.
components.html(html_content, height=1500, scrolling=True)
