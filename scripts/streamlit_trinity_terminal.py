import streamlit as st
import json
import numpy as np
import pandas as pd
import time
import math
import re
import matplotlib.pyplot as plt
from io import StringIO

# --- CONFIGURATION DU TERMINAL ---
st.set_page_config(
    page_title="LICHEN TRINITY TERMINAL V3.3",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS CUSTOM (Style Cyber-Organique) ---
st.markdown("""
<style>
    /* Global Theme */
    .stApp {
        background-color: #050505;
        color: #00FF94;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #00FF94 !important;
        font-family: 'Courier New', monospace;
        text-shadow: 0px 0px 5px rgba(0, 255, 148, 0.3);
    }
    
    /* Buttons */
    .stButton>button {
        color: #050505;
        background-color: #00FF94;
        border-radius: 0px;
        border: 1px solid #00FF94;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #050505;
        color: #00FF94;
        box-shadow: 0px 0px 10px #00FF94;
    }
    
    /* Inputs */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #111;
        color: #00FF94;
        border: 1px solid #333;
        font-family: 'Courier New', monospace;
    }
    
    /* Metrics */
    div[data-testid="stMetricValue"] {
        color: #00FF94;
        text-shadow: 0px 0px 5px #00FF94;
    }
    
    /* Custom Alerts */
    .success-box {
        padding: 15px;
        background-color: rgba(0, 255, 148, 0.05);
        border-left: 3px solid #00FF94;
        margin-bottom: 10px;
        font-family: 'Courier New', monospace;
    }
    .error-box {
        padding: 15px;
        background-color: rgba(255, 50, 50, 0.05);
        border-left: 3px solid #FF3232;
        margin-bottom: 10px;
        font-family: 'Courier New', monospace;
        color: #FF3232;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0a0a0a;
        border-right: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# --- MOTEUR LOGIQUE ---

class LichenEngine:
    def __init__(self):
        self.PHI = 1.61803398875
        self.PI = 3.14159265359
        self.PERFECT_NUMBERS = [6, 28, 496, 8128, 33550336]
        
    def load_manifest(self):
        try:
            with open('manifest.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            return None

    def is_prime(self, n):
        if n < 2: return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0: return False
        return True

    def calculate_ceml(self, coherence, entropy):
        # J = C / (H + epsilon)
        return coherence / (entropy + 0.001)

    def text_to_dna(self, text):
        # 00=A, 01=C, 10=G, 11=T
        binary = ''.join(format(ord(c), '08b') for c in text)
        dna_map = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
        sense = ""
        pairs = [binary[i:i+2] for i in range(0, len(binary), 2)]
        for p in pairs:
            sense += dna_map.get(p, 'A')
        
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        antisense = "".join([complement[b] for b in sense])
        return sense, antisense

engine = LichenEngine()
manifest = engine.load_manifest()

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("💎 TRINITY V3.3")
st.sidebar.markdown(f"**Version Noyau:** {manifest['project']['version'] if manifest else 'OFFLINE'}")
st.sidebar.markdown("---")

menu = st.sidebar.radio("MODULES SYSTÈME", [
    "📜 Manifeste (Loi)",
    "🔮 ΦLang (Esprit)",
    "🧬 HELIX-Φ (Mémoire)",
    "👁️ LGL (Vision)",
    "🔥 Sociophysique (Réseau)",
    "💾 ZPA / UHFS (Stockage)"
])

# --- MODULE 1: MANIFESTE ---
if "Manifeste" in menu:
    st.title("📜 Le Manifeste Unifié (V3.0.0)")
    st.markdown("Source de Vérité Unique. Ingestion JSON directe.")
    
    if manifest:
        col1, col2, col3 = st.columns(3)
        col1.metric("Théories", len(manifest.get('theories', [])))
        col2.metric("Composants", len(manifest.get('core_components', [])))
        col3.metric("Protocoles", len(manifest.get('protocols', {})))
        
        tab1, tab2, tab3, tab4 = st.tabs(["Projet", "Théories (L'Âme)", "Langages", "JSON Brut"])
        
        with tab1:
            st.markdown(f"### {manifest['project']['tagline']}")
            st.info(manifest['project']['description'])
            st.code(manifest['meta']['dedication'], language="text")
            
        with tab2:
            st.subheader("Architecture Cognitive & Physique")
            for theory in manifest['theories']:
                with st.expander(f"🔹 {theory['name']} ({theory['id']})"):
                    st.write(f"**Abstract:** {theory['abstract']}")
                    if 'formula' in theory:
                        f = theory['formula']
                        if isinstance(f, str):
                            st.latex(f)
                        elif isinstance(f, dict):
                            if 'mass' in f: st.latex(f['mass'])
                            elif 'score' in f: st.latex(f['score'])
                            elif 'index' in f: st.latex(f['index'])
                            elif 'hamiltonian' in f: st.latex(f['hamiltonian'])
                            elif 'formula' in f: st.latex(f['formula'])
                            else: st.latex(list(f.values())[0])
                    if 'philang_integration' in theory:
                        st.markdown(f"**ΦLang:** `{theory['philang_integration']}`")
        
        with tab3:
            st.subheader("La Trinité Linguistique")
            langs = manifest['languages']['comparison']
            st.json(langs)
            
        with tab4:
            st.json(manifest)
    else:
        st.error("ERREUR FATALE: `manifest.json` introuvable ou corrompu.")

# --- MODULE 2: ΦLANG ---
elif "ΦLang" in menu:
    st.title("🔮 Compilateur ΦLang")
    st.markdown("Traduction: Intention → Vecteur Mathématique (496D).")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Entrée Source")
        code = st.text_area("Code ΦLang", "[7-496] :: Ψ(Φ)", height=100)
        
        if st.button("COMPILER LE VECTEUR"):
            pattern = r"\[(\d+)-(\d+)\]\s*::\s*Ψ\((.+)\)"
            match = re.match(pattern, code)
            
            if match:
                p, n, param = int(match.group(1)), int(match.group(2)), match.group(3)
                
                # Validation
                is_p_prime = engine.is_prime(p)
                is_n_perfect = n in engine.PERFECT_NUMBERS or n == 496
                
                if is_p_prime and is_n_perfect:
                    st.session_state['compile_success'] = True
                    st.session_state['vec_p'] = p
                    st.session_state['vec_n'] = n
                    st.markdown(f'<div class="success-box">✅ SYNTAXE VALIDE<br>Action: {p} (Prime)<br>Structure: {n} (Perfect)</div>', unsafe_allow_html=True)
                else:
                    st.session_state['compile_success'] = False
                    err = ""
                    if not is_p_prime: err += f"Action {p} invalide (Pas un nombre premier). "
                    if not is_n_perfect: err += f"Structure {n} invalide (Pas un nombre parfait). "
                    st.markdown(f'<div class="error-box">❌ ERREUR GÉOMÉTRIQUE<br>{err}</div>', unsafe_allow_html=True)
            else:
                st.error("Erreur de format. Attendu: [Premier-Parfait] :: Ψ(Param)")

    with col2:
        if st.session_state.get('compile_success'):
            st.subheader("FC-496 Atom (Simulation)")
            
            # Simulation Vecteur
            vec = np.random.rand(8) # Just showing first 8 dims of E8
            
            col_a, col_b = st.columns(2)
            col_a.metric("Header (Structure)", "190 bits")
            col_b.metric("Payload (Données)", "306 bits")
            
            # CEML Score calculation
            ceml = engine.calculate_ceml(0.98, 0.2) # High coherence for Philang
            st.metric("Score CEML", f"{ceml:.4f}", delta="Harmonique")
            
            fig, ax = plt.subplots(figsize=(6, 2))
            ax.bar(range(8), vec, color='#00FF94')
            ax.set_facecolor('#050505')
            fig.patch.set_facecolor('#050505')
            ax.tick_params(colors='white')
            plt.title("Projection E8 (8 premières dimensions)", color='white')
            st.pyplot(fig)

# --- MODULE 3: HELIX-PHI ---
elif "HELIX" in menu:
    st.title("🧬 HELIX-Φ Encoder")
    st.markdown("Stockage ADN Base-4 pour archivage profond (10,000 ans).")
    
    txt = st.text_input("Données à cristalliser", "Lichen Universe V3")
    
    if txt:
        sense, antisense = engine.text_to_dna(txt)
        
        st.markdown("### 🧬 Double Hélice Générée")
        
        # Visualisation custom
        html = "<div style='font-family: monospace; line-height: 1.5; font-size: 18px;'>"
        for i in range(min(len(sense), 50)):
            c1 = "#FF595E" if sense[i] == 'A' else "#8AC926" if sense[i] == 'C' else "#1982C4" if sense[i] == 'T' else "#FFCA3A"
            c2 = "#FF595E" if antisense[i] == 'A' else "#8AC926" if antisense[i] == 'C' else "#1982C4" if antisense[i] == 'T' else "#FFCA3A"
            html += f"<span style='color:{c1}'>{sense[i]}</span> ≡ <span style='color:{c2}'>{antisense[i]}</span><br>"
        html += "</div>"
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(html, unsafe_allow_html=True)
        with col2:
            st.info(f"Longueur: {len(sense)} bp")
            st.info("Validation: S-Locus OK")
            st.download_button("Télécharger Séquence .fasta", f">SENSE\n{sense}\n>ANTISENSE\n{antisense}")

# --- MODULE 4: LGL ---
elif "LGL" in menu:
    st.title("👁️ LGL Composer")
    st.markdown("Programmation Spatiale et Iconique.")
    
    glyphs = {
        "Structure": ["◯", "△", "□", "⬡"],
        "Flux": ["→", "↻", "⚡", "∿"],
        "Logique": ["⊕", "⊗", "⊘", "⟁"],
        "Conscience": ["◎", "⊛", "⟡", "⌘"]
    }
    
    col_tools, col_canvas = st.columns([1, 2])
    
    with col_tools:
        st.subheader("Glyph Set")
        for cat, icons in glyphs.items():
            st.write(f"**{cat}**")
            cols = st.columns(4)
            for i, icon in enumerate(icons):
                cols[i].button(icon, key=icon)
                
    with col_canvas:
        st.subheader("Canvas Spatial (φ-Grid)")
        st.markdown("""
        ```lgl
           φ²
        ┌──────┐
        │  ◎   │  (Self)
        ├──────┤
        │  ⚡   │  (Coupling)
        ├──────┤
        │  ⊛   │  (Swarm)
        └──────┘
           Result: ⟡ (Emergence)
        ```
        """)
        st.caption("Le parser LGL convertit cette géométrie en graphe sémantique.")

# --- MODULE 5: SOCIOPHYSIQUE (KURAMOTO) ---
elif "Sociophysique" in menu:
    st.title("🔥 Simulateur Sociophysique Kuramoto")
    st.markdown("Dynamique des foules, modes et polarisations.")
    
    with st.expander("📖 Comprendre la Théorie (Omega Bias)", expanded=True):
        st.write("""
        * **K (Couplage):** Positif = Mode/Amour, Négatif = Haine/Polarisation.
        * **Ω (Omega Bias):** Tendance naturelle. Si > 0 (Innovateurs), Si < 0 (Conservateurs).
        * **R (Ordre):** 0 = Chaos, 1 = Synchronisation Totale.
        """)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Paramètres")
        N = st.slider("Nombre d'agents (N)", 10, 500, 100)
        K = st.slider("Force de Couplage (K)", -5.0, 5.0, 1.5, 0.1)
        omega_bias = st.slider("Omega Bias (Culture)", -2.0, 2.0, 0.0, 0.1, help="0=Neutre, >0=Rapide/Innovant, <0=Lent/Conservateur")
        
        st.markdown("---")
        if K > 2.0: st.success("Mode: GROOVE / VIRAL")
        elif K < -1.0: st.error("Mode: GUERRE CIVILE (Chimère)")
        else: st.warning("Mode: BRUIT / DIVERSITÉ")

    with col2:
        st.subheader("Simulation Temps Réel")
        
        # Initialisation
        phases = np.random.uniform(0, 2*np.pi, N)
        omegas = np.random.normal(omega_bias, 0.5, N) # Omega Bias appliqué ici
        
        # Simulation (Simplifiée pour l'affichage statique instantané)
        # On simule T étapes
        dt = 0.1
        T = 50
        r_history = []
        
        for _ in range(T):
            # Kuramoto step
            # dtheta_i = omega_i + K/N * sum(sin(theta_j - theta_i))
            # Vectorized implementation approx
            # Pour la démo visuelle, on utilise une approximation de convergence
            if K > 0:
                # Attraction vers la moyenne
                mean_phase = np.angle(np.mean(np.exp(1j * phases)))
                phases += (omegas + K * np.sin(mean_phase - phases)) * dt
            else:
                # Répulsion (Polarisation)
                # Split en 2 groupes
                phases += (omegas + K * np.sin(phases)) * dt # Chaos induit
            
            # Order parameter
            r = np.abs(np.mean(np.exp(1j * phases)))
            r_history.append(r)
            
        # Visualisation
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        
        # Cercle de phase
        ax1.scatter(np.cos(phases), np.sin(phases), c=phases, cmap='hsv', alpha=0.7)
        ax1.set_xlim(-1.5, 1.5)
        ax1.set_ylim(-1.5, 1.5)
        ax1.set_title("Distribution des Phases")
        ax1.set_facecolor('#050505')
        
        # Historique R
        ax2.plot(r_history, color='#00FF94')
        ax2.set_ylim(0, 1)
        ax2.set_title("Synchronisation (r)")
        ax2.set_facecolor('#050505')
        
        fig.patch.set_facecolor('#050505')
        
        # Styling axes
        for ax in [ax1, ax2]:
            ax.tick_params(colors='white')
            for spine in ax.spines.values():
                spine.set_color('white')
                
        st.pyplot(fig)
        st.metric("Cohérence Finale (r)", f"{r_history[-1]:.3f}")

# --- MODULE 6: ZPA / UHFS ---
elif "ZPA" in menu:
    st.title("💾 ZPA & UHFS Architecture")
    st.markdown("Zero-Parse Architecture & Le Ruban Infini.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("Axiome α : Toute donnée est un bloc de 496 bits.")
        st.info("Axiome β : L'adressage suit une spirale logarithmique φ.")
        
        st.code("""
struct Universal_Atom_496 {
    magic: u128,      // Signature
    pi_index: u64,    // Temps
    geo_hash: u128,   // Espace
    payload: [u8; 38] // Data
}
// Zero-Copy, Zero-Parse, Mmap-Ready
        """, language="rust")
        
    with col2:
        st.markdown("### Visualisation du Ruban")
        # Dessin Spirale
        theta = np.linspace(0, 8*np.pi, 500)
        r = 1.618**(theta / (2*np.pi))
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.plot(x, y, color='#00FF94')
        ax.scatter(x[::50], y[::50], color='white', s=10) # Data blocks
        ax.set_facecolor('#050505')
        fig.patch.set_facecolor('#050505')
        ax.axis('off')
        st.pyplot(fig)
        st.caption("Adressage Logarithmique : O(1) Access")

# --- FOOTER ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; font-family: monospace;'>
        LICHEN UNIVERSE UNIFIED V3.0.0 | © 2025 Lichen Collective<br>
        <i>"Le noyau respire, la spirale s'ouvre."</i>
    </div>
    """, 
    unsafe_allow_html=True
)
