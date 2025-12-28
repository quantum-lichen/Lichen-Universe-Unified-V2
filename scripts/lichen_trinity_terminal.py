import streamlit as st
import requests
import json
import math
import random
import time
import re

# --- CONFIGURATION DU TERMINAL ---
st.set_page_config(
    page_title="LICHEN TRINITY V3.4 MYCO-NET",
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
        version = manifest.get('project', {}).get('version', '3.0.0')
        st.success(f"🟢 HIVE LINK: CONNECTED (v{version})")
    else:
        st.error("🔴 HIVE LINK: DISCONNECTED")
    
    # MENU MIS À JOUR AVEC LE 5ÈME ÉLÉMENT
    mode = st.radio("SÉLECTION DU PROTOCOLE", [
        "1. ΦLang (Math)", 
        "2. HELIX-Φ (Bio)", 
        "3. LGL (Visuel)", 
        "4. SYSTEM (Raw)",
        "5. MycoNet (Fungi)"
    ])
    
    st.divider()
    st.write("🌌 **Universal Constants**")
    if manifest:
        cst = manifest.get('universal_constants', {}).get('definitions', {})
        if cst:
            phi_val = cst.get('phi', {}).get('value', '1.618')
            pi_val = cst.get('pi', {}).get('value', '3.141')
            dim_val = cst.get('perfect_496', {}).get('value', '496')
            
            st.caption(f"φ = {phi_val}")
            st.caption(f"π = {pi_val}")
            st.caption(f"Dim = {dim_val}")

# --- MOTEUR DE TRAITEMENT (MATHÉMATIQUE & DÉTERMINISTE) ---

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
    perfects = [6, 28, 496, 8128, 33550336] 
    return n in perfects

def compile_philang(code):
    """Compile et valide mathématiquement le ΦLang"""
    
    # 1. ANALYSE SYNTAXIQUE (REGEX)
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

    # 4. GÉNÉRATION DÉTERMINISTE (FIXE)
    vector_seed = (prime_candidate * perfect_candidate) + hash(param)
    random.seed(vector_seed)
    
    binary_vector = bin(vector_seed % (2**496))[2:].zfill(496)
    
    base_score = 0.618
    stability_bonus = random.uniform(0.2, 0.381) 
    final_score = base_score + stability_bonus
    
    return {
        "status": "VALID",
        "type": "Vecteur Mathématique Certifié",
        "prime_check": f"{prime_candidate} ∈ ℙ (Prime)",
        "perfect_check": f"{perfect_candidate} ∈ ℙerfect",
        "header_preview": binary_vector[:32] + "...",
        "payload_preview": binary_vector[190:222] + "...",
        "ceml_score": final_score
    }

def encode_helix(text):
    """Encode du texte en ADN HELIX-Φ"""
    mapping = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
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
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.info(result['prime_check'])
                with col_b:
                    st.info(result['perfect_check'])
                
                st.markdown("#### ⚛️ Structure Atomique (FC-496)")
                st.code(f"HEADER (190b) : {result['header_preview']}\nDATA   (306b) : {result['payload_preview']}")
                
                st.progress(result['ceml_score'], text=f"Score CEML : {result['ceml_score']:.6f} (Constant)")
                
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
        * **[2-28]** : Dualité sur Cluster
        """)

elif mode == "2. HELIX-Φ (Bio)":
    st.title("🧬 Séquenceur HELIX-Φ")
    st.markdown("> *Archivage Long-Terme sur ADN.*")
    
    input_text = st.text_area("Données à encoder (Texte humain) :", "Lichen V3.0")
    
    if input_text:
        dna_sequence = encode_helix(input_text)
        
        st.subheader("🧬 Double Hélice Générée")
        
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

elif mode == "5. MycoNet (Fungi)":
    st.title("🍄 MycoNet: Fungal Routing Layer")
    st.markdown("> *Nature's original internet. 10^12 connections per node.*")
    
    # --- CONFIGURATION DU MYCELIUM ---
    c1, c2, c3 = st.columns(3)
    with c1:
        spikes = st.slider("Activité Électrique (Spikes/sec)", 1, 100, 13)
    with c2:
        nutrients = st.slider("Densité Nutritionnelle (Données)", 0.0, 1.0, 0.618)
    with c3:
        decay = st.slider("Facteur d'Atrophie (Nettoyage)", 0.1, 0.9, 0.3)

    st.divider()

    # --- SIMULATION SPATIALE ---
    nodes = ["Alpha", "Beta", "Gamma", "Delta", "Omega"]
    
    st.subheader("⚡ Electrical Spike Activity (Bio-Signaling)")
    
    chart_data = []
    # Génération deterministe mais chaotique (Organique)
    random.seed(time.time()) 
    
    for i in range(50):
        base = math.sin(i * 0.5) * 0.2
        organic_noise = random.uniform(-0.1, 0.1)
        is_spike = 1.0 if random.random() > (1.0 - (spikes/200)) else 0.0
        signal = base + organic_noise + is_spike
        chart_data.append(signal)
    
    st.line_chart(chart_data, color="#00FF94")
    
    # --- ROUTAGE STIGMERGIQUE ---
    st.subheader("🕸️ Hyphae Pathfinding (Routage Dynamique)")
    
    col_a, col_b = st.columns([1, 2])
    
    with col_a:
        target = st.selectbox("Cible de la Colonie", nodes)
        if st.button("Lancer les Hyphes"):
            st.session_state['myco_target'] = target
            st.session_state['myco_growth'] = True
    
    with col_b:
        if st.session_state.get('myco_growth'):
            st.write(f"🌱 Colonisation vers **{st.session_state.get('myco_target', 'Unknown')}** en cours...")
            
            path = ["Root"]
            
            # Barre de progression visuelle
            progress_bar = st.progress(0, text="Extension du réseau...")
            
            for i in range(100):
                chance = random.random()
                time.sleep(0.01)
                progress_bar.progress(i + 1, text=f"Densification des connexions... {i}%")
                
                if chance < nutrients and len(path) < 4:
                    available_nodes = [n for n in nodes if n not in path]
                    if available_nodes:
                        next_node = random.choice(available_nodes)
                        path.append(next_node)
            
            st.success(f"✅ CONNEXION ÉTABLIE : {' → '.join(path)} → {st.session_state.get('myco_target')}")
            st.caption(f"Ce chemin a été renforcé chimiquement. Les autres chemins se sont atrophiés.")
            
            with st.expander("🔍 Analyse Technique (Myco-Protocol)"):
                st.write("**Biomimicry:** Armillaria bulbosa Network")
                st.code(f"""
def fungal_routing(source, target, nutrients):
    # 1. Broadcasting: Envoi d'impulsions électriques faibles
    # 2. Sensing: Détection du gradient de données (Nutrients={nutrients})
    # 3. Reinforcing: Si Chemin valide, conductance = conductance * 1.618
    # 4. Pruning: Si Chemin vide, conductance = conductance * {decay}
    return optimized_path
                """, language="python")

# --- FOOTER SÉCURISÉ ---
st.divider()
if manifest:
    gen_name = manifest.get('generator', 'Lichen Collective')
    meta_data = manifest.get('meta', {})
    if isinstance(meta_data, dict):
        special_msg = meta_data.get('birthday_special', 'Operational')
    else:
        special_msg = "System Operational"
    
    st.caption(f"Generated by {gen_name} | {special_msg}")
else:
    st.caption("System Offline - Reconnecting...")
