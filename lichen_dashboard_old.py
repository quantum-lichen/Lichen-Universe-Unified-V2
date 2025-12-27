import streamlit as st
import json
import requests
import time
import random

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Lichen V3.1 Dashboard",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS PERSONNALISÉ (Pour le look Cyberpunk/Clean) ---
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
</style>
""", unsafe_allow_html=True)

# --- FONCTION DE CHARGEMENT DU MANIFESTE (SOURCE DE VÉRITÉ) ---
@st.cache_data(ttl=300) # Cache de 5 minutes pour pas spammer GitHub
def load_remote_manifest():
    # C'est ICI que je mets le chemin exact vers TON repo
    url = "https://raw.githubusercontent.com/quantum-lichen/Lichen-Universe-Unified-V2/main/manifest.json"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"❌ Impossible de charger le Manifeste. Code erreur: {response.status_code}")
            st.warning(f"Lien testé : {url}")
            return None
    except Exception as e:
        st.error(f"❌ Erreur de connexion : {e}")
        return None

# --- CHARGEMENT DES DONNÉES ---
manifest = load_remote_manifest()

# --- SI LE FICHIER N'EST PAS ENCORE SUR GITHUB ---
if not manifest:
    st.title("⚠️ Initialisation du Système...")
    st.write("Le fichier `manifest.json` n'est pas encore détecté à la racine du dépôt.")
    st.info("Action requise : Uploadez le fichier JSON final sous le nom 'manifest.json' dans GitHub.")
    st.stop() # On arrête l'exécution ici

# --- DÉBUT DU DASHBOARD ---

# En-tête
c1, c2 = st.columns([3, 1])
with c1:
    st.title(f"🌲 {manifest['project']['name']}")
    st.caption(f"Codename: {manifest.get('project', {}).get('codename', 'OMEGA')} | Version: {manifest['project']['version']}")
    st.markdown(f"> *\"{manifest['philosophy']['vision']}\"*")

with c2:
    st.image("https://img.shields.io/badge/Architecture-ZPA%20Unified-green?style=for-the-badge")
    st.image("https://img.shields.io/badge/Language-PhiLang-blue?style=for-the-badge")

st.divider()

# --- SECTION 1: SANTÉ DU SYSTÈME (LIVE MONITORING) ---
st.subheader("🖥️ ZPA Real-Time Core Monitor")

# Simulation de données temps réel (puisque c'est une démo)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Constantes", len(manifest['universal_constants']), delta="Stable")
with col2:
    st.metric("Core Components", len(manifest['core_components']), delta="+2 (V3.1)")
with col3:
    # Calcul dynamique de la latence simulée
    latency = random.uniform(0.1, 0.45)
    st.metric("Access Latency", f"{latency:.3f} ms", delta="-Zero-Copy", delta_color="normal")
with col4:
    st.metric("Logic", "Base-5 (TzBit)", delta="Quantique")

# --- SECTION 2: NAVIGATION DANS L'ARCHITECTURE ---
st.subheader("📂 Architecture Explorer")

tabs = st.tabs(["🧬 Constants", "🗣️ Langages", "🧠 Cognition", "🛠️ Composants", "📜 Raw JSON"])

# ONGLET 1 : CONSTANTES
with tabs[0]:
    st.info("Les piliers mathématiques de l'univers.")
    cols = st.columns(len(manifest['universal_constants']))
    for idx, (key, data) in enumerate(manifest['universal_constants'].items()):
        with cols[idx]:
            st.markdown(f"### {data.get('symbol', key)}")
            st.write(f"**Type:** {data['type']}")
            if 'value' in data:
                st.code(data['value'])
            st.caption(data['role'])

# ONGLET 2 : LANGAGES
with tabs[1]:
    st.success("La Trinité Linguistique Unifiée.")
    
    for lang_key, lang_data in manifest['languages'].get('suite', {}).items():
        with st.expander(f"🔵 {lang_data['name']} ({lang_data['type']})", expanded=True):
            lc1, lc2 = st.columns([1, 2])
            with lc1:
                st.write(f"**Target:** {lang_data['target']}")
                st.code(lang_data.get('syntax', 'N/A'))
            with lc2:
                st.write("**Propriétés:**")
                st.write(", ".join(lang_data['properties']))

# ONGLET 3 : COGNITION & ÉTHIQUE (La partie "Psychiatrie")
with tabs[2]:
    st.warning("Systèmes de régulation éthique et mentale.")
    
    cog = manifest.get('cognitive_psychology', {})
    
    cc1, cc2 = st.columns(2)
    with cc1:
        st.markdown("#### ⚖️ CEML (Entropie)")
        st.latex(r"J(s) = \frac{\mathcal{C}(s|\Omega)}{S(s) + \epsilon}")
        st.write("Seuil de validation : **J ≥ 0.618**")
    
    with cc2:
        st.markdown("#### 🧭 EHE (Éthique)")
        st.latex(r"EHE = \tanh(k \cdot (\alpha \Delta \beta + \dots))")
        st.write("Thermostat moral actif.")

    # VISUALISATION DE LA SANTÉ (Ton bloc préféré)
    st.divider()
    st.write("**Simulation d'Intégrité Vectorielle (Test Live)**")
    
    # Simulation d'un score
    live_score = random.uniform(0.6, 0.99)
    
    if live_score > 0.8:
        status_msg = "✅ SYSTEM NOMINAL (Symbiose)"
        bar_color = "green"
    elif live_score > 0.618:
        status_msg = "⚠️ STABLE (Surveillance Active)"
        bar_color = "orange"
    else:
        status_msg = "⛔ CRITICAL (Dissonance Détectée)"
        bar_color = "red"
        
    st.progress(live_score, text=f"Niveau de Cohérence Actuel : {live_score:.4f} | {status_msg}")

# ONGLET 4 : COMPOSANTS
with tabs[3]:
    st.write("Inventaire des modules actifs.")
    for comp_category, comp_data in manifest['core_architecture'].items():
        st.markdown(f"### {comp_category.upper()}")
        st.json(comp_data, expanded=False)

# ONGLET 5 : RAW DATA
with tabs[4]:
    st.write("Source de vérité (manifest.json chargé depuis GitHub).")
    st.json(manifest)

# --- FOOTER ---
st.divider()
st.markdown(f"<div style='text-align: center; color: gray;'>{manifest['meta']['quote']}</div>", unsafe_allow_html=True)
st.markdown(f"<div style='text-align: center; font-size: 0.8em;'>Architecture: {manifest['project']['author']['name']} | Hash: {manifest['meta']['hash'][:16]}...</div>", unsafe_allow_html=True)
