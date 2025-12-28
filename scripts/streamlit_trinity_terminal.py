import streamlit as st
import json
import numpy as np
import pandas as pd
import time
import math
import re
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List, Dict, Tuple

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
    .reportview-container {
        background: #050505;
        color: #00FF94;
    }
    .sidebar .sidebar-content {
        background: #0a0a0a;
    }
    h1, h2, h3 {
        color: #00FF94 !important;
        font-family: 'Courier New', monospace;
    }
    .stButton>button {
        color: #050505;
        background-color: #00FF94;
        border-radius: 0px;
        border: 1px solid #00FF94;
    }
    .stTextInput>div>div>input {
        background-color: #111;
        color: #00FF94;
        border: 1px solid #333;
    }
    .success-box {
        padding: 10px;
        background-color: rgba(0, 255, 148, 0.1);
        border-left: 5px solid #00FF94;
        margin-bottom: 10px;
    }
    .error-box {
        padding: 10px;
        background-color: rgba(255, 0, 0, 0.1);
        border-left: 5px solid #FF0000;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- CHARGEMENT DU MANIFESTE ---
@st.cache_data
def load_manifest():
    try:
        with open('manifest.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

manifest = load_manifest()

# --- MOTEUR MATHÉMATIQUE (CONSTANTES) ---
PHI = 1.61803398875
PI = 3.14159265359
PERFECT_NUMBERS = [6, 28, 496, 8128, 33550336]
PRIMES_SMALL = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# --- CLASSES DU NOYAU ---

class PhiLangCompiler:
    """Compilateur ΦLang : Transforme [Prime-Perfect] en Vecteur 496D"""
    
    def is_prime(self, n):
        if n < 2: return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0: return False
        return True

    def validate_instruction(self, instruction):
        # Regex pour parser [Prime-Perfect] :: Ψ(Param)
        pattern = r"\[(\d+)-(\d+)\]\s*::\s*Ψ\((.+)\)"
        match = re.match(pattern, instruction)
        
        if not match:
            return False, "Erreur de syntaxe. Format attendu: [Prime-Perfect] :: Ψ(Param)", None

        prime = int(match.group(1))
        perfect = int(match.group(2))
        param = match.group(3)

        # Validation Géométrique
        if not self.is_prime(prime):
            return False, f"Erreur Géométrique: {prime} n'est pas un nombre premier (Action invalide).", None
        
        if perfect not in PERFECT_NUMBERS and perfect != 496: # Tolérance pour la démo
            return False, f"Erreur Géométrique: {perfect} n'est pas un nombre parfait (Structure instable).", None

        return True, "Instruction Valide", (prime, perfect, param)

    def compile_to_atom(self, prime, perfect, param):
        # Simulation de la génération du vecteur 496 bits
        # Header (190 bits) + Payload (306 bits)
        
        # Seed déterministe basé sur l'instruction
        seed_val = prime * perfect + hash(param)
        np.random.seed(seed_val % 2**32)
        
        # Génération du vecteur
        vector = np.random.rand(496)
        
        # Calcul du score CEML (Cohérence / Entropie)
        # J = C / (H + e)
        # Simulation: Les instructions valides ont naturellement un score élevé
        coherence = 0.95 # Base haute pour ΦLang
        entropy = np.random.uniform(0.1, 0.3)
        ceml_score = coherence / (entropy + 0.001)
        
        # Normalisation si > 1 (juste pour la démo)
        if ceml_score > 1.618: ceml_score = 1.618 

        return vector, ceml_score

class HelixEncoder:
    """Encodeur HELIX-Φ : Texte vers ADN Base-4"""
    
    def to_dna(self, text):
        # Mapping simple pour la démo (ASCII -> Base 4)
        # 00=A, 01=C, 10=G, 11=T
        binary = ''.join(format(ord(c), '08b') for c in text)
        dna_map = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
        
        sense_strand = ""
        pairs = [binary[i:i+2] for i in range(0, len(binary), 2)]
        for p in pairs:
            sense_strand += dna_map.get(p, 'A')
            
        return sense_strand

    def generate_antisense(self, sense_strand):
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return "".join([complement[b] for b in sense_strand])

# --- INTERFACE UTILISATEUR ---

st.sidebar.title("💎 TRINITY V3.3")
st.sidebar.markdown("---")
mode = st.sidebar.radio("Navigation du Noyau", 
    ["Manifeste (Loi)", "ΦLang (Esprit)", "HELIX-Φ (Mémoire)", "LGL (Vision)", "Sociophysique (Réseau)"])

st.sidebar.markdown("---")
if manifest:
    st.sidebar.success("🟢 Manifeste V3.0.0 Chargé")
    st.sidebar.caption(f"Généré le: {manifest.get('generated_at', 'Inconnu')}")
else:
    st.sidebar.error("🔴 Manifeste introuvable")
    st.sidebar.info("Veuillez placer 'manifest.json' dans le dossier.")

# === 1. MANIFESTE ===
if mode == "Manifeste (Loi)":
    st.title("📜 Le Manifeste Unifié (Source de Vérité)")
    st.markdown("Explorateur de la structure JSON V3.0.0.")
    
    if manifest:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.info(f"**Version:** {manifest['project']['version']}")
            st.info(f"**Tagline:** {manifest['project']['tagline']}")
            st.info(f"**Auteur:** {manifest['project']['author']['name']}")
        
        with col2:
            search = st.text_input("Rechercher dans le Manifeste", "")
            if search:
                st.write(f"Résultats pour '{search}': (Fonctionnalité démo)")
            else:
                st.json(manifest, expanded=False)
    else:
        st.warning("Chargez le fichier manifest.json pour voir les données.")

# === 2. ΦLANG (COMPILATEUR) ===
elif mode == "ΦLang (Esprit)":
    st.title("🔮 Compilateur ΦLang")
    st.markdown("Le langage des vecteurs mathématiques purs. `[Action]-[Structure] :: Ψ(But)`")
    
    compiler = PhiLangCompiler()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Entrée Source (.phi)")
        code_input = st.text_area("Écrire l'instruction", "[7-496] :: Ψ(Φ)", height=100)
        
        if st.button("COMPILER LE VECTEUR"):
            valid, msg, components = compiler.validate_instruction(code_input)
            
            if valid:
                st.markdown(f'<div class="success-box">✅ {msg}</div>', unsafe_allow_html=True)
                p, perf, param = components
                vector, ceml = compiler.compile_to_atom(p, perf, param)
                
                # Stockage en session
                st.session_state['last_vector'] = vector
                st.session_state['last_ceml'] = ceml
                st.session_state['last_components'] = components
                
            else:
                st.markdown(f'<div class="error-box">❌ {msg}</div>', unsafe_allow_html=True)
                st.error("Rappel: Utilisez des nombres Premiers pour l'action et Parfaits (6, 28, 496) pour la structure.")

    with col2:
        st.subheader("Sortie Binaire (FC-496 Atom)")
        if 'last_vector' in st.session_state:
            vec = st.session_state['last_vector']
            ceml = st.session_state['last_ceml']
            prime, perfect, param = st.session_state['last_components']
            
            # Visualisation du Header/Payload
            st.caption(f"Structure Atomique: {496} bits")
            col_h, col_p = st.columns([190, 306])
            with col_h:
                st.metric("Header (Structure)", "190 bits")
                st.progress(100)
            with col_p:
                st.metric("Payload (Paramètre)", "306 bits")
                st.progress(100)
                
            st.metric("Score CEML (Cohérence)", f"{ceml:.4f}", delta=f"{ceml - 0.618:.4f} vs Threshold")
            
            if ceml >= 0.618:
                st.success("🔒 EXÉCUTION AUTORISÉE (Validé par le Noyau)")
                st.code(f"OPCODE: 0x{prime:02X}{perfect:04X}...", language="text")
                
                # Visualisation Vectorielle (Heatmap simulée)
                st.text("Projection E8 (8 premières dimensions) :")
                st.bar_chart(vec[:8])
            else:
                st.error("🛡️ REJETÉ PAR S-LOCUS (Dissonance Harmonique)")

# === 3. HELIX-Φ (ADN) ===
elif mode == "HELIX-Φ (Mémoire)":
    st.title("🧬 Encodeur HELIX-Φ")
    st.markdown("Stockage biologique pérenne (10 000 ans). Base-4.")
    
    encoder = HelixEncoder()
    
    text_input = st.text_input("Données à encoder (Texte)", "Lichen Universe V3")
    
    if text_input:
        sense = encoder.to_dna(text_input)
        antisense = encoder.generate_antisense(sense)
        
        st.subheader("Double Hélice Générée")
        
        # Affichage style ADN
        col_dna1, col_dna2, col_dna3 = st.columns([1, 1, 4])
        
        with col_dna1:
            st.markdown("**Brin Sens (Action)**")
            st.code(sense, language="text")
            
        with col_dna2:
            st.markdown("**Brin Anti-Sens (Validation)**")
            st.code(antisense, language="text")
            
        with col_dna3:
            st.markdown("**Visualisation Géométrique**")
            # Simulation visuelle simple
            html_dna = ""
            colors = {'A': '#FF595E', 'T': '#1982C4', 'C': '#8AC926', 'G': '#FFCA3A'}
            for s, a in zip(sense[:20], antisense[:20]):
                html_dna += f"<span style='color:{colors[s]}'><b>{s}</b></span>━━<span style='color:{colors[a]}'><b>{a}</b></span><br>"
            if len(sense) > 20: html_dna += "..."
            st.markdown(html_dna, unsafe_allow_html=True)
            
        st.info(f"Densité d'information: {len(sense)} bases pour {len(text_input)} caractères.")

# === 4. LGL (VISUEL) ===
elif mode == "LGL (Vision)":
    st.title("👁️ LGL : Lichen Glyph Language")
    st.markdown("Interface spatiale pour la collaboration Humain-IA.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Palette de Glyphes")
        # Clavier virtuel LGL
        glyphs = {
            "Structure": ["◯", "△", "□", "⬡"],
            "Mouvement": ["→", "↻", "⚡", "∿"],
            "Opérateurs": ["⊕", "⊗", "⊘", "⟁"],
            "Conscience": ["◎", "⊛", "⟡", "⌘"]
        }
        
        selected_glyphs = ""
        for category, icons in glyphs.items():
            st.markdown(f"**{category}**")
            cols = st.columns(4)
            for i, icon in enumerate(icons):
                if cols[i].button(icon, key=f"btn_{icon}"):
                    # Dans une vraie app, on ajouterait au state, ici on simule
                    st.toast(f"Glyphe {icon} ajouté")
    
    with col2:
        st.subheader("Zone de Composition")
        st.markdown("""
        ```lgl
           φ²
        ┌──────┐
        │  ◎   │ (Self)
        ├──────┤
        │  ⚡   │ (Connect)
        ├──────┤
        │  ⊛   │ (Swarm)
        └──────┘
           Result: ⟡ (Emergence)
        ```
        """)
        st.caption("Le parser spatial convertit cette géométrie en instruction ΦLang.")

# === 5. SOCIOPHYSIQUE (KURAMOTO) ===
elif mode == "Sociophysique (Réseau)":
    st.title("🔥 Simulateur Kuramoto")
    st.markdown("Modélisation des modes, du rire et des conflits idéologiques.")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Paramètres de Couplage (K)")
        k_strength = st.slider("Force de Couplage (K)", -5.0, 5.0, 1.0, 0.1)
        st.caption("K > 0 : Attraction (Amour/Mode)")
        st.caption("K < 0 : Répulsion (Haine/Guerre)")
        
        n_agents = st.slider("Nombre d'Agents (N)", 10, 200, 50)
        coherence = st.slider("Cohérence Initiale", 0.0, 1.0, 0.1)
    
    with col2:
        st.subheader("Dynamique de Phase")
        
        # Simulation simple de Kuramoto
        # dθ/dt = ω + K * mean(sin(θj - θi))
        
        # Initialisation
        phases = np.random.uniform(0, 2*np.pi, n_agents)
        # Si cohérence initiale élevée, on resserre les phases
        if coherence > 0.1:
            phases = np.random.normal(np.pi, 1.0 - coherence, n_agents)
            
        frequencies = np.random.normal(0, 1, n_agents) # Fréquences naturelles
        
        # Simulation d'un pas de temps (convergence visuelle)
        # Pour la démo, on montre l'état final théorique
        
        fig, ax = plt.subplots(figsize=(10, 4))
        
        if k_strength > 1.5:
            # Synchronisation (Mode/Groove)
            final_phases = np.ones(n_agents) * np.pi + np.random.normal(0, 0.1, n_agents)
            status = "🔒 PHASE LOCKED (Groove/Mode)"
            color = 'cyan'
        elif k_strength < -1.0:
            # État Chimère / Anti-Phase
            group_a = np.ones(n_agents//2) * np.pi
            group_b = np.ones(n_agents - n_agents//2) * (np.pi + np.pi) # Pi shift
            final_phases = np.concatenate([group_a, group_b]) + np.random.normal(0, 0.1, n_agents)
            status = "⚔️ ÉTAT CHIMÈRE (Guerre Civile / Polarisation)"
            color = 'red'
        else:
            # Incohérence
            final_phases = phases + np.random.uniform(-1, 1, n_agents)
            status = "💨 INCOHÉRENCE (Bruit de fond)"
            color = 'gray'
            
        # Plot sur le cercle unitaire
        x = np.cos(final_phases)
        y = np.sin(final_phases)
        
        ax.scatter(x, y, alpha=0.7, c=color)
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal')
        ax.set_title(f"État du Réseau: {status}")
        ax.grid(True, linestyle='--', alpha=0.3)
        
        st.pyplot(fig)
        
        if k_strength < -1.0:
            st.warning("⚠️ ALERTE: Polarisation détectée (K < Kc). Risque de rupture du lien social.")
        if k_strength > 2.0:
            st.success("✨ HARMONIE: Synchronisation élevée. Groove actif.")

# --- FOOTER ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        LICHEN UNIVERSE UNIFIED V3.0.0 | © 2025 Lichen Collective<br>
        <i>"Le noyau respire, la spirale s'ouvre."</i>
    </div>
    """, 
    unsafe_allow_html=True
)
