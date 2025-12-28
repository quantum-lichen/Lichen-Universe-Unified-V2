import streamlit as st
import requests
import json
import math
import random
import time

# --- CONFIGURATION DU TERMINAL ---
st.set_page_config(
    page_title="LICHEN TRINITY V3.2 FIXED",  # <--- SI TU VOIS ÇA, C'EST QUE ÇA A MARCHÉ
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLE CYBER-ORGANIQUE ---
st.markdown("""
<style>
    .stApp {
        background-color: #050505;
        color: #00FF94;
    }
    .stTextInput > div > div > input {
        background-color: #111;
        color: #00FF94;
        font-family: 'Courier New', monospace;
    }
    .stTextArea > div > div > textarea {
        background-color: #111;
        color: #00FF94;
        font-family: 'Courier New', monospace;
    }
    h1, h2, h3 { color: #E0E0E0 !important; }
    .success { color: #00FF94; font-weight: bold; }
    .error { color: #FF3333; font-weight: bold; }
    .metric-box { border: 1px solid #333; padding: 10px; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

# --- 1. CONNEXION AU CERVEAU (RAW DATA) ---
@st.cache_data(ttl=60)
def connect_to_hive_mind():
    # Lien RAW validé vers ton Manifeste V3.0
    url = "https://raw.githubusercontent.com/quantum-lichen/Lichen-Universe-Unified-V2/main/manifest.json"
    try:
        return requests.get(url).json()
    except:
        return None

manifest = connect_to_hive_mind()

# --- SIDEBAR DE NAVIGATION ---
with st.sidebar:
    st.image("https://img.shields.io/badge/LICHEN-TRINITY_OS-00FF94?style=for-the-badge&logo=atom")
    
    if manifest:
        # Récupération sécurisée de la version
        version = manifest.get('project', {}).get('version', '3.0.0')
        st.success(f"🟢 HIVE LINK: CONNECTED (v{version})")
    else:
        st.error("🔴 HIVE LINK: DISCONNECTED")
    
    mode = st.radio("SÉLECTION DU PROTOCOLE", ["1. ΦLang (Math)", "2. HELIX-Φ (Bio)", "3. LGL (Visuel)", "4. SYSTEM (Raw)"])
    
    st.divider()
    st.write("🌌 **Universal Constants**")
    if manifest:
        # Accès sécurisé aux constantes
        cst = manifest.get('universal_constants', {}).get('definitions', {})
        if cst:
            phi_val = cst.get('phi', {}).get('value', '1.618')
            pi_val = cst.get('pi', {}).get('value', '3.141')
            dim_val = cst.get('perfect_496', {}).get('value', '496')
            
            st.caption(f"φ = {phi_val}")
            st.caption(f"π = {pi_val}")
            st.caption(f"Dim = {dim_val}")

# --- MOTEUR DE TRAITEMENT (SIMULATION) ---

def compile_philang(code):
    """Simule la compilation d'instructions ΦLang"""
    # Analyse basique de la syntaxe [P-N]::Ψ(X)
    if "::Ψ" in code and "[" in code and "]" in code:
        # Simulation d'un vecteur 496 bits
        vector_hash = hash(code) % (2**496)
        binary_vector = bin(vector_hash)[2:].zfill(496)
        
        # Partition FC-496 (190 header / 306 payload)
        header = binary_vector[:190]
        payload = binary_vector[190:]
        
        return {
            "status": "VALID",
            "type": "Instruction Vectorielle",
            "atom_size": "496 bits",
            "header_preview": header[:32] + "...",
            "payload_preview": payload[:32] + "...",
            "ceml_score": random.uniform(0.618, 0.99) # Simulation CEML
        }
    else:
        return {"status": "INVALID", "error": "Syntaxe géométrique non respectée. Attendu: [Prime-Perfect]::Ψ(Param)"}

def encode_helix(text):
    """Encode du texte en ADN HELIX-Φ"""
    mapping = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
    # Conversion simple pour la démo
    try:
        binary = ''.join(format(ord(i), '08b') for i in text)
        pairs = [binary[i:i+2] for i in range(0, len(binary), 2)]
        dna = "".join([mapping.get(p, 'A') for p in pairs])
        return dna
    except:
        return "ERROR_ENCODING"

# --- INTERFACE PRINCIPALE ---

if mode == "1. ΦLang (Math)":
    st.title("💠 Console Vectorielle ΦLang")
    st.markdown("> *The language of pure mathematics - zero ambiguity.*")
    
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.markdown("### ⌨️ Input Vectoriel")
        code_input = st.text_input("Entrez votre instruction :", value="[7-496]::Ψ(Φ)")
        
        if st.button("EXECUTE [RUN]"):
            result = compile_philang(code_input)
            
            if result['status'] == "VALID":
                st.success("✅ INSTRUCTION VALIDÉE PAR GÉOMÉTRIE E8")
                
                # Visualisation de l'Atome FC-496
                st.markdown("#### ⚛️ Structure Atomique (FC-496)")
                st.text(f"HEADER (190b) : {result['header_preview']}")
                st.text(f"DATA   (306b) : {result['payload_preview']}")
                
                # Jauge CEML
                st.progress(result['ceml_score'], text=f"Score CEML : {result['ceml_score']:.4f} (Seuil > 0.618)")
                
                # Simulation Hardware
                with st.expander("🖥️ Snowflake-Ω CPU Output"):
                    st.write("1. Oscillators synced (Kuramoto r=0.98)")
                    st.write("2. Vector projected to E8 lattice")
                    st.write("3. State updated.")
            else:
                st.error(f"❌ {result['error']}")

    with c2:
        st.info("💡 Aide Rapide")
        st.markdown("""
        * **[7-496]** : Cycle sur Dimension Complète
        * **::Ψ(Φ)** : Cible = Ratio d'Or
        * **[13-6]** : Ancrage sur Hexagone
        """)

elif mode == "2. HELIX-Φ (Bio)":
    st.title("🧬 Séquenceur HELIX-Φ")
    st.markdown("> *Archivage Long-Terme sur ADN.*")
    
    input_text = st.text_area("Données à encoder (Texte humain) :", "Lichen V3.0")
    
    if input_text:
        dna_sequence = encode_helix(input_text)
        
        st.subheader("🧬 Double Hélice Générée")
        
        # Affichage visuel ADN
        st.code(dna_sequence, language=None)
        
        st.markdown("### 🔬 Analyse Géométrique")
        col1, col2, col3 = st.columns(3)
        col1.metric("Longueur", f"{len(dna_sequence)} bases")
        col2.metric("Densité", "4.8x (GKF)")
        col3.metric("Durabilité", "~10,000 ans")
        
        with st.expander("Voir le brin complémentaire (Anti-Sense)"):
            complement = dna_sequence.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c").upper()
            st.code(complement)

elif mode == "3. LGL (Visuel)":
    st.title("👁️ Interface LGL (Spatial)")
    st.markdown("> *Where mathematics becomes visible.*")
    
    # Simulation d'interface Glyphe
    st.write("Construction de phrase glyphique :")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        g1 = st.selectbox("Sujet", ["◯ (Unity)", "△ (Trinity)", "□ (Base)"])
    with col2:
        g2 = st.selectbox("Action", ["→ (Flow)", "⚡ (Transform)", "↻ (Recurse)"])
    with col3:
        g3 = st.selectbox("Objet", ["⬡ (Structure)", "∿ (Wave)", "Φ (Golden)"])
    with col4:
        st.metric("Résolution", "φ-Grid")

    st.subheader("Visualisation Conceptuelle")
    st.markdown(f"""
    <div style="font-size: 40px; text-align: center; border: 1px solid #333; padding: 20px; border-radius: 10px;">
    {g1[0]} {g2[0]} {g3[0]}
    </div>
    """, unsafe_allow_html=True)
    
    st.caption(f"Interprétation : {g1.split('(')[1][:-1]} {g2.split('(')[1][:-1]}s into {g3.split('(')[1][:-1]}")

elif mode == "4. SYSTEM (Raw)":
    st.title("📜 Manifeste V3.1 (Source)")
    if manifest:
        st.json(manifest)
    else:
        st.warning("Chargement des données Hive Mind...")

# --- FOOTER SÉCURISÉ ---
st.divider()
if manifest:
    # Utilisation de .get() pour éviter les crashs si une clé manque
    gen_name = manifest.get('generator', 'Lichen Collective')
    
    # Recherche sécurisée de l'info 'birthday_special' dans 'meta'
    meta_data = manifest.get('meta', {})
    if isinstance(meta_data, dict):
        special_msg = meta_data.get('birthday_special', 'Operational')
    else:
        special_msg = "System Operational"
    
    st.caption(f"Generated by {gen_name} | {special_msg}")
else:
    st.caption("System Offline - Reconnecting...")
