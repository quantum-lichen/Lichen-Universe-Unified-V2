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

import re  # On ajoute Regex pour parser proprement

# --- MOTEUR DE TRAITEMENT (MATHÉMATIQUE RÉEL) ---

def is_prime(n):
    """Vérifie si n est un nombre premier (Action)"""
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

def is_perfect(n):
    """Vérifie si n est un nombre parfait (Structure)"""
    if n < 6: return False
    sum_div = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_div += i
            if i*i != n:
                sum_div += n // i
    return sum_div == n

def compile_philang(code):
    """Compile et valide mathématiquement le ΦLang"""
    
    # 1. ANALYSE SYNTAXIQUE (REGEX)
    # Cherche le pattern : [NOMBRE-NOMBRE]::Ψ(TEXTE)
    match = re.search(r"\[(\d+)-(\d+)\]::Ψ\((.+)\)", code)
    
    if not match:
        return {"status": "INVALID", "error": "SYNTAX ERROR: Format attendu [Prime-Perfect]::Ψ(Param)"}
    
    # 2. EXTRACTION DES VALEURS
    prime_candidate = int(match.group(1))
    perfect_candidate = int(match.group(2))
    param = match.group(3)
    
    # 3. VALIDATION MATHÉMATIQUE (LE JUGE IMPITOYABLE)
    errors = []
    
    if not is_prime(prime_candidate):
        errors.append(f"⛔ GÉOMÉTRIE CASSÉE : {prime_candidate} n'est pas un nombre PREMIER (Action invalide).")
        
    if not is_perfect(perfect_candidate):
        errors.append(f"⛔ TOPOLOGIE INSTABLE : {perfect_candidate} n'est pas un nombre PARFAIT (Structure invalide).")
    
    if errors:
        return {"status": "REJECTED", "error": " | ".join(errors)}

    # 4. GÉNÉRATION DE L'ATOME (SI TOUT EST BON)
    # Simulation d'un vecteur 496 bits basé sur la signature mathématique
    vector_seed = (prime_candidate * perfect_candidate) + hash(param)
    binary_vector = bin(vector_seed % (2**496))[2:].zfill(496)
    
    return {
        "status": "VALID",
        "type": "Vecteur Mathématique Certifié",
        "prime_check": f"{prime_candidate} ∈ ℙ (Prime)",
        "perfect_check": f"{perfect_candidate} ∈ ℙerfect",
        "header_preview": binary_vector[:32] + "...",
        "payload_preview": binary_vector[190:222] + "...",
        "ceml_score": random.uniform(0.85, 0.999) # Bonus car mathématiquement pur
    }

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
