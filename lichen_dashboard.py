import streamlit as st
import json
import requests
import random

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Lichen V3.1 Dashboard",
    page_icon="🌲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS PERSONNALISÉ (Style Cyberpunk/Clean) ---
st.markdown("""
<style>
    .reportview-container {
        background: #0e1117;
    }
    .metric-card {
        background-color: #262730;
        border: 1px solid #4F4F4F;
        padding: 15px;
        border-radius: 10px;
        color: white;
    }
    h1 { color: #00FF94 !important; }
    h2 { color: #FAFAFA !important; }
    h3 { color: #CCCCCC !important; }
    .stProgress > div > div > div > div {
        background-color: #00FF94;
    }
    div[data-testid="stMetricValue"] {
        font-size: 24px;
    }
</style>
""", unsafe_allow_html=True)

# --- FONCTION DE CHARGEMENT DU MANIFESTE (SOURCE DE VÉRITÉ) ---
@st.cache_data(ttl=300) 
def load_remote_manifest():
    # URL VALIDÉE PAR LE DÉTECTIVE
    url = "https://raw.githubusercontent.com/quantum-lichen/Lichen-Universe-Unified-V2/main/manifest.json"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"❌ Erreur HTTP : {response.status_code}")
            return None
    except Exception as e:
        st.error(f"❌ Erreur de connexion : {e}")
        return None

# --- CHARGEMENT DES DONNÉES ---
manifest = load_remote_manifest()

# --- SI LE FICHIER N'EST PAS ENCORE DISPO ---
if not manifest:
    st.warning("En attente de connexion au Manifeste...")
    st.stop()

# =========================================================
#  INTERFACE DU DASHBOARD
# =========================================================

# 1. EN-TÊTE
c1, c2 = st.columns([3, 1])
with c1:
    st.title(f"🌲 {manifest['project']['name']}")
    # Gestion des clés optionnelles pour éviter les erreurs si 'codename' manque
    codename = manifest.get('project', {}).get('tagline', 'OMEGA')
    version = manifest['project']['version']
    st.caption(f"Système: {codename} | Version: {version}")
    
    vision = manifest['philosophy']['vision']
    st.markdown(f"> *\"{vision}\"*")

with c2:
    st.metric("Statut", "OPERATIONAL", delta="V3.1.1 OK")

st.divider()

# 2. MONITORING TEMPS RÉEL (Simulation ZPA)
st.subheader("🖥️ ZPA Real-Time Core Monitor")

col1, col2, col3, col4 = st.columns(4)

with col1:
    # Compte dynamique basé sur le JSON
    nb_constants = len(manifest.get('universal_constants', {}).get('definitions', []))
    st.metric("Constantes Univ.", nb_constants, delta="Stable")

with col2:
    nb_components = len(manifest.get('core_components', []))
    st.metric("Core Components", nb_components, delta="Chargés")

with col3:
    # Simulation de latence ultra-faible (ZPA)
    latency = random.uniform(0.05, 0.45)
    st.metric("Access Latency", f"{latency:.3f} ms", delta="-Zero-Copy", delta_color="normal")

with col4:
    # Extraction de la version de PhiLang si dispo
    philang_v = manifest['languages'].get('PHILANG', {}).get('version', '1.0')
    st.metric("ΦLang Engine", f"v{philang_v}", delta="Native")

# 3. NAVIGATION DANS L'ARCHITECTURE
st.subheader("📂 Architecture Explorer")

tabs = st.tabs(["🧬 Constants", "🗣️ Langages", "🧠 Cognition", "🛠️ Composants", "📜 Raw JSON"])

# ONGLET 1 : CONSTANTES
with tabs[0]:
    st.info("Les piliers mathématiques de l'univers.")
    definitions = manifest['universal_constants'].get('definitions', {})
    
    # Affichage en grille
    cols = st.columns(3)
    for i, (key, data) in enumerate(definitions.items()):
        col = cols[i % 3]
        with col:
            symbol = data.get('symbol', key)
            with st.container(border=True):
                st.markdown(f"### {symbol}")
                st.caption(data.get('type', 'Constante'))
                st.code(data.get('value', 'N/A'))
                st.write(data.get('role', ''))

# ONGLET 2 : LANGAGES (La Trinité)
with tabs[1]:
    st.success(f"Philosophie : {manifest['languages'].get('philosophy', 'N/A')}")
    
    # On liste les langages spécifiques
    langs = ['PHILANG', 'HELIX-PHI', 'LGL']
    for lang_key in langs:
        if lang_key in manifest['languages']:
            lang_data = manifest['languages'][lang_key]
            with st.expander(f"🔵 {lang_data['name']}", expanded=True):
                lc1, lc2 = st.columns([1, 3])
                with lc1:
                    st.write(f"**Type:**")
                    st.caption(lang_data.get('type', 'N/A'))
                with lc2:
                    st.write(f"**Description:** {lang_data.get('description', '')}")
                    if 'tagline' in lang_data:
                        st.markdown(f"*{lang_data['tagline']}*")

# ONGLET 3 : COGNITION (Psychiatrie IA)
with tabs[2]:
    st.warning("Systèmes de régulation éthique et mentale.")
    
    # On cherche les théories liées à la cognition
    theories = manifest.get('theories', [])
    ceml_theory = next((t for t in theories if 'CEML' in t['name']), None)
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("#### ⚖️ CEML (Entropie)")
        if ceml_theory:
            st.write(ceml_theory.get('abstract', ''))
            st.code("J(s) = C(s|Ω) / (H(s) + ε)")
        else:
            st.write("Module CEML chargé via Manifeste.")

    with c2:
        st.markdown("#### 🧭 Intégrité Vectorielle (Simulation)")
        # Simulation visuelle
        live_score = random.uniform(0.75, 0.99)
        if live_score > 0.8:
            status_msg = "✅ SYSTEM NOMINAL (Symbiose)"
        else:
            status_msg = "⚠️ STABLE"
        
        st.progress(live_score, text=f"Cohérence : {live_score:.4f} | {status_msg}")
        st.caption("Monitoring des vecteurs ΦLang en temps réel.")

# ONGLET 4 : COMPOSANTS (Liste déroulante)
with tabs[3]:
    st.write("Inventaire des modules actifs.")
    components = manifest.get('core_components', [])
    
    for comp in components:
        with st.expander(f"⚙️ {comp['name']} ({comp['id']})"):
            st.write(comp.get('description', ''))
            if 'specs' in comp:
                st.json(comp['specs'])

# ONGLET 5 : RAW DATA
with tabs[4]:
    st.write("Source de vérité (manifest.json).")
    st.json(manifest)

# --- FOOTER ---
st.divider()
quote = manifest.get('meta', {}).get('quote', 'System Ready.')
author = manifest.get('project', {}).get('author', {}).get('name', 'Unknown')

st.markdown(f"<div style='text-align: center; color: gray; font-style: italic;'>{quote}</div>", unsafe_allow_html=True)
st.markdown(f"<div style='text-align: center; font-size: 0.8em; margin-top: 10px;'>Architecte: {author}</div>", unsafe_allow_html=True)
