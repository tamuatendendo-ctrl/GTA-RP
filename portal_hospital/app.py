import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Hospital Carapicuíba RP - UNIMED",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "logo_unimed.png"
CURRICULO_PATH = ASSETS_DIR / "curriculo_maridao.jpeg"

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    :root { --green: #008b5a; --dark: #12372d; --muted: #60756e; --line: #dce8e2; }
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    [data-testid="stAppViewContainer"] { background: #f5f8f6; }
    [data-testid="stHeader"] { background: transparent; }
    .block-container { max-width: 1100px; padding-top: 1.5rem; padding-bottom: 3rem; }
    .hero {
        background: linear-gradient(135deg, #ffffff 0%, #eef8f2 100%);
        border: 1px solid var(--line); border-radius: 24px;
        padding: 28px 32px; margin-bottom: 24px;
        box-shadow: 0 12px 35px rgba(18,55,45,.05);
    }
    .eyebrow { color: var(--green); text-transform: uppercase; letter-spacing: .14em; font-size: .75rem; font-weight: 800; }
    .hero h1 { color: var(--dark); font-size: clamp(2rem, 4vw, 3rem); line-height: 1.12; margin: 10px 0 12px; font-weight: 800; }
    .hero p { color: var(--muted); font-size: 1rem; line-height: 1.7; max-width: 700px; margin-bottom: 0; }
    .section-title { color:var(--dark); font-size:1.35rem; font-weight:800; margin: 28px 0 5px; }
    .section-sub { color:var(--muted); margin-bottom:18px; }
    .service-card {
        background:#fff; border:1px solid var(--line); border-radius:20px; padding:24px;
        min-height: 250px; box-shadow:0 8px 24px rgba(18,55,45,.04);
    }
    .service-icon { width:48px; height:48px; display:flex; align-items:center; justify-content:center; background:#e8f5ee; border-radius:14px; font-size:1.5rem; margin-bottom:18px; }
    .service-card h3 { color:var(--dark); font-size:1.2rem; font-weight:800; margin:0 0 8px; }
    .service-card p { color:var(--muted); line-height:1.6; min-height:50px; }
    .status { display:inline-block; border-radius:999px; padding:5px 10px; background:#e8f5ee; color:#08764e; font-size:.75rem; font-weight:800; margin-bottom:14px; }
    .portal-footer { text-align:center; color:#71847d; font-size:.8rem; padding:26px 0 8px; }
    a.portal-button { display:inline-flex; align-items:center; justify-content:center; text-decoration:none; background:var(--green); color:white !important; padding:12px 17px; border-radius:10px; font-weight:700; }
    a.portal-button:hover { background:#006e48; }
    .curriculum-intro { color:var(--muted); line-height:1.7; }
    @media (max-width: 650px) {
      .hero { padding:20px; border-radius:18px; }
      .block-container { padding-left:1rem; padding-right:1rem; }
      .service-card { padding:20px; }
    }
</style>
""", unsafe_allow_html=True)

# Cabeçalho com a identidade do hospital e a logo original fornecida pelo usuário.
with st.container():
    title_col, logo_col = st.columns([3, 1.15], vertical_alignment="center")
    with title_col:
        st.markdown("""
        <div class="hero">
          <div class="eyebrow">Portal de serviços hospitalares</div>
          <h1>Hospital Carapicuíba RP</h1>
          <p>Acesse os formulários administrativos do hospital em um só lugar. Selecione abaixo o documento que deseja preencher e gerar.</p>
        </div>
        """, unsafe_allow_html=True)
    with logo_col:
        if LOGO_PATH.exists():
            st.image(str(LOGO_PATH), use_container_width=True)
        else:
            st.markdown("**UNIMED**")

st.markdown("""
<div class="section-title">Sistemas disponíveis</div>
<div class="section-sub">Escolha uma das opções para continuar.</div>
""", unsafe_allow_html=True)

left, right = st.columns(2, gap="large")
with left:
    st.markdown("""
    <div class="service-card">
      <div class="service-icon">📄</div>
      <div class="status">DISPONÍVEL</div>
      <h3>Certidão de Óbito</h3>
      <p>Preencha os dados necessários e gere a certidão pelo formulário do hospital.</p>
      <a class="portal-button" href="https://gta-rp-obito.streamlit.app" target="_blank" rel="noopener noreferrer">Abrir formulário&nbsp; ↗</a>
    </div>
    """, unsafe_allow_html=True)
with right:
    st.markdown("""
    <div class="service-card">
      <div class="service-icon">🧠</div>
      <div class="status">DISPONÍVEL</div>
      <h3>Laudo Psicológico</h3>
      <p>Preencha os campos do laudo psicológico e gere o documento correspondente.</p>
      <a class="portal-button" href="https://gta-rp-psicologico.streamlit.app/" target="_blank" rel="noopener noreferrer">Abrir formulário&nbsp; ↗</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="section-title">Diretoria do hospital</div>
<div class="section-sub">Currículo profissional do Diretor Geral HP — Maridão.</div>
""", unsafe_allow_html=True)

if CURRICULO_PATH.exists():
    st.image(str(CURRICULO_PATH), use_container_width=True)
else:
    st.warning("A imagem do currículo não foi encontrada. Confira se o arquivo assets/curriculo_maridao.jpeg está no repositório.")

st.markdown("""
<div class="portal-footer">
  Hospital Carapicuíba RP - UNIMED · Portal de acesso aos formulários do GTA-RP
</div>
""", unsafe_allow_html=True)
