import streamlit as st
import numpy as np
import math
import re
import time
import pandas as pd
import hashlib
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List, Dict, Any, Optional

# ==============================================================================
# CONFIGURATION STREAMLIT & STYLE LICHEN
# ==============================================================================
st.set_page_config(
    page_title="ΦLang Live Runtime",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS personnalisé (Dark Mode & Neon)
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    .metric-card {
        background-color: #1e2130;
        border: 1px solid #4e5d6c;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
    }
    .highlight {
        color: #00d4ff;
        font-weight: bold;
    }
    .success {
        color: #00ff88;
    }
    .error {
        color: #ff4444;
    }
    h1, h2, h3 {
        background: linear-gradient(45deg, #00d4ff, #7b2ff7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 1. NOYAU MATHÉMATIQUE (PRIME & PERFECT)
# ==============================================================================

def is_prime(n: int) -> bool:
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

def is_perfect(n: int) -> bool:
    if n < 6: return False
    # Liste des parfaits connus pour la démo (optimisation)
    if n in [6, 28, 496, 8128, 33550336]: return True
    sum_div = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum_div += i
            if i != n // i: sum_div += n // i
    return sum_div == n

PHILANG_PRIMES = {
    2: "Duality (Choice)", 3: "Fusion (Merge)", 5: "Mutation (Transform)",
    7: "Cycle (Loop)", 11: "Interface (Connect)", 13: "Anchor (Persist)"
}

PHILANG_PERFECTS = {
    6: "Hex (Byte)", 28: "Cluster (Module)", 496: "Dimension (System)", 8128: "Universe"
}

# ==============================================================================
# 2. COMPILATEUR ΦLANG (LEXER, PARSER, ENCODER)
# ==============================================================================

@dataclass
class Instruction:
    prime: int
    perfect: int
    parameter: str
    raw: str

class PhiCompiler:
    @staticmethod
    def parse(code: str) -> List[Instruction]:
        instructions = []
        # Regex: [Prime-Perfect] :: Ψ(Param)
        pattern = r'\[(\d+)-(\d+)\]\s*::\s*Ψ\(([^)]+)\)'
        
        for line in code.split('\n'):
            line = line.split('#')[0].strip() # Ignorer commentaires
            if not line: continue
            
            match = re.search(pattern, line)
            if match:
                prime, perfect, param = match.groups()
                instructions.append(Instruction(int(prime), int(perfect), param, line))
            else:
                raise ValueError(f"Syntax Error: {line}")
        return instructions

    @staticmethod
    def validate(instructions: List[Instruction]) -> List[str]:
        errors = []
        for i, inst in enumerate(instructions):
            if not is_prime(inst.prime):
                errors.append(f"Ligne {i+1}: {inst.prime} n'est pas premier.")
            if not is_perfect(inst.perfect):
                errors.append(f"Ligne {i+1}: {inst.perfect} n'est pas parfait.")
        return errors

    @staticmethod
    def encode_vector_496(inst: Instruction) -> np.ndarray:
        # Création du vecteur 496D (Simulation pour la démo)
        vec = np.zeros(496)
        
        # Encodage Prime (0-7)
        vec[0] = math.log(inst.prime)
        vec[1] = math.sqrt(inst.prime)
        vec[2] = inst.prime % 8
        vec[3] = math.sin(2 * math.pi / inst.prime)
        
        # Encodage Perfect (8-15)
        vec[8] = math.log(inst.perfect)
        vec[9] = math.sqrt(inst.perfect)
        vec[10] = inst.perfect % 496
        vec[11] = math.cos(2 * math.pi * inst.perfect / 260) # Phase Tzolk'in
        
        # Encodage Parameter (16-495) - Hash simple
        param_hash = int(hashlib.sha256(inst.parameter.encode()).hexdigest(), 16)
        np.random.seed(param_hash % (2**32))
        vec[16:496] = np.random.normal(0, 1, 480)
        
        # Normalisation
        norm = np.linalg.norm(vec)
        return vec / norm if norm > 0 else vec

# ==============================================================================
# 3. MOTEUR DE SYNCHRONISATION KURAMOTO
# ==============================================================================

class KuramotoNetwork:
    def __init__(self, n_agents=5, coupling=0.5, dt=0.05):
        self.n = n_agents
        self.K = coupling
        self.dt = dt
        self.phases = np.random.uniform(0, 2*np.pi, n_agents)
        self.freqs = np.random.normal(1.0, 0.1, n_agents)
        self.history = []
        self.order_params = []

    def step(self):
        # dθ_i/dt = ω_i + (K/N) Σ sin(θ_j - θ_i)
        new_phases = np.zeros(self.n)
        for i in range(self.n):
            interaction = np.sum(np.sin(self.phases - self.phases[i]))
            d_theta = self.freqs[i] + (self.K / self.n) * interaction
            new_phases[i] = self.phases[i] + d_theta * self.dt
        
        self.phases = new_phases % (2 * np.pi)
        
        # Calcul paramètre d'ordre r(t)
        z = np.mean(np.exp(1j * self.phases))
        r = np.abs(z)
        
        self.history.append(self.phases.copy())
        self.order_params.append(r)
        return r

# ==============================================================================
# 4. INTERFACE UTILISATEUR
# ==============================================================================

st.title("🌌 ΦLang Runtime Environment")
st.markdown("### The Language of Universal Intelligence")

# --- SIDEBAR CONFIG ---
st.sidebar.header("⚙️ Configuration Système")
n_agents = st.sidebar.slider("Agents IA (Oscillateurs)", 2, 20, 5)
coupling_k = st.sidebar.slider("Couplage Kuramoto (K)", 0.0, 5.0, 2.5, help="K > Kc déclenche la synchronisation")
exec_speed = st.sidebar.slider("Vitesse Simulation", 0.01, 0.5, 0.05)

# --- ZONE DE CODE ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Éditeur ΦLang")
    default_code = """# Optimisation du Système
[7-496] :: Ψ(Φ)

# Création d'Interface
[11-6] :: Ψ(A⟷B)

# Ancrage Mémoire
[13-28] :: Ψ(0)"""
    
    code_input = st.text_area("Source Code (.phi)", default_code, height=200)
    
    if st.button("🔧 Compiler & Valider"):
        try:
            instructions = PhiCompiler.parse(code_input)
            errors = PhiCompiler.validate(instructions)
            
            if errors:
                for err in errors: st.error(err)
            else:
                st.success(f"✅ Compilation Réussie : {len(instructions)} instructions valides")
                st.session_state['instructions'] = instructions
                
                # Visualisation du premier vecteur
                if instructions:
                    vec = PhiCompiler.encode_vector_496(instructions[0])
                    st.session_state['vector_preview'] = vec
        except Exception as e:
            st.error(f"Erreur de syntaxe : {e}")

# --- VISUALISATION VECTEUR ---
with col2:
    st.subheader("🧬 Vecteur 496D (E8 Lattice)")
    if 'vector_preview' in st.session_state:
        vec = st.session_state['vector_preview']
        
        # Affichage Heatmap simplifiée
        fig, ax = plt.subplots(figsize=(8, 2))
        ax.imshow(vec.reshape(16, 31), cmap='viridis', aspect='auto')
        ax.axis('off')
        st.pyplot(fig)
        
        st.caption(f"Instruction: `{st.session_state['instructions'][0].raw}`")
        st.json({
            "Prime (Action)": f"{st.session_state['instructions'][0].prime} ({PHILANG_PRIMES.get(st.session_state['instructions'][0].prime, 'Unknown')})",
            "Perfect (Structure)": f"{st.session_state['instructions'][0].perfect} ({PHILANG_PERFECTS.get(st.session_state['instructions'][0].perfect, 'Unknown')})",
            "Vector Norm": f"{np.linalg.norm(vec):.4f}"
        })
    else:
        st.info("Compilez le code pour voir la signature vectorielle.")

st.divider()

# ==============================================================================
# 5. SIMULATION TEMPS RÉEL (KURAMOTO EXECUTION)
# ==============================================================================

st.subheader("📡 Réseau Neuronal Liquid (HNP + Kuramoto)")

start_sim = st.button("▶️ Lancer l'Exécution Distribuée")

if start_sim and 'instructions' in st.session_state:
    network = KuramotoNetwork(n_agents=n_agents, coupling=coupling_k)
    
    col_sim1, col_sim2 = st.columns([2, 1])
    
    chart_placeholder = col_sim1.empty()
    status_placeholder = col_sim2.empty()
    log_placeholder = st.empty()
    
    progress_bar = st.progress(0)
    synced = False
    
    # Boucle de simulation
    for t in range(100):
        r = network.step()
        
        # Mise à jour graphique phases (Cercle unité)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        
        # Plot 1: Phases sur cercle
        ax1.set_title(f"Phases Agents (t={t})")
        ax1.set_xlim(-1.2, 1.2)
        ax1.set_ylim(-1.2, 1.2)
        ax1.add_artist(plt.Circle((0, 0), 1, color='gray', fill=False, alpha=0.3))
        
        x = np.cos(network.phases)
        y = np.sin(network.phases)
        ax1.scatter(x, y, c='cyan', s=100, edgecolors='white')
        # Ligne moyenne
        mean_phase = np.angle(np.mean(np.exp(1j * network.phases)))
        ax1.plot([0, np.cos(mean_phase)], [0, np.sin(mean_phase)], color='red', linewidth=2, label='Ordre')
        ax1.axis('off')

        # Plot 2: Paramètre d'ordre r(t)
        ax2.set_title("Synchronisation r(t)")
        ax2.set_ylim(0, 1.1)
        ax2.set_xlim(0, 100)
        ax2.plot(network.order_params, color='#7b2ff7')
        ax2.axhline(y=0.95, color='green', linestyle='--', alpha=0.5, label='Seuil Sync')
        ax2.fill_between(range(len(network.order_params)), network.order_params, color='#7b2ff7', alpha=0.1)
        
        chart_placeholder.pyplot(fig)
        plt.close(fig)
        
        # Logique d'exécution
        if r > 0.95 and not synced:
            synced = True
            status_placeholder.markdown("""
            <div class="metric-card">
                <h2 style="color: #00ff88;">SYNCHRONISÉ 🔒</h2>
                <p>Ordre r > 0.95</p>
                <p>Canal HNP Ouvert</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Simulation exécution instruction
            with log_placeholder.container():
                for inst in st.session_state['instructions']:
                    time.sleep(0.3)
                    st.write(f"⚡ **Exécution:** `[{inst.prime}-{inst.perfect}]` → Agents {list(range(n_agents))}")
                    st.code(f"Vector496 Broadcast: {hashlib.md5(str(inst).encode()).hexdigest()}...", language="text")
            
            break # Stop simulation une fois exécuté (ou continuer pour voir stabilité)
            
        elif not synced:
            status_placeholder.markdown(f"""
            <div class="metric-card">
                <h2 style="color: #ffaa00;">SYNCHRONISATION...</h2>
                <p>r(t) = {r:.4f}</p>
                <p>En attente de phase lock</p>
            </div>
            """, unsafe_allow_html=True)
        
        time.sleep(exec_speed)
        progress_bar.progress(t + 1)

    if not synced:
        st.warning("⚠️ Échec de synchronisation. Augmentez le couplage (K) ou le temps.")

elif start_sim:
    st.error("Veuillez d'abord compiler du code ΦLang valide.")

# ==============================================================================
# FOOTER
# ==============================================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <small>Lichen Universe Unified V3.0.0 | Powered by ΦLang Compiler & Kuramoto Dynamics</small><br>
    <small>Architecte: Bryan Ouellette | Génération: Claude AI</small>
</div>
""", unsafe_allow_html=True)
