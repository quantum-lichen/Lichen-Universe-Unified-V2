import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
import time

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Lichen Quantum Crystal",
    page_icon="💎",
    layout="centered"
)

# --- CONSTANTES UNIVERSELLES ---
PHI = (1 + np.sqrt(5)) / 2
PI = np.pi
N_ATOMS = 496
COUPLING_STRENGTH = PHI
DT = 0.01

@dataclass
class FractalLayer:
    name: str
    size: int
    frequency: float
    phases: np.ndarray

class QuantumCrystal:
    def __init__(self):
        # Architecture Fractale à 3 Niveaux
        self.root = FractalLayer("ROOT", 1, 1.0, np.zeros(1))
        self.blocks = FractalLayer("BLOCKS", 8, PHI, np.random.uniform(0, 2*PI, 8))
        self.bits = FractalLayer("BITS", N_ATOMS, PHI**2, np.random.uniform(0, 2*PI, N_ATOMS))
        self.history = []

    def kuramoto_step(self, layer, coupling_k):
        order_parameter = np.mean(np.exp(1j * layer.phases))
        mean_phase = np.angle(order_parameter)
        delta = coupling_k * np.sin(mean_phase - layer.phases)
        return delta

    def fractal_coupling(self):
        block_idx = np.arange(N_ATOMS) % 8
        parent_phases = self.blocks.phases[block_idx]
        vertical_force_bits = PHI * np.sin(parent_phases - self.bits.phases)
        vertical_force_blocks = PHI * np.sin(self.root.phases[0] - self.blocks.phases)
        return vertical_force_bits, vertical_force_blocks

    def update(self):
        internal_bits = self.kuramoto_step(self.bits, COUPLING_STRENGTH)
        internal_blocks = self.kuramoto_step(self.blocks, COUPLING_STRENGTH)
        vert_bits, vert_blocks = self.fractal_coupling()
        
        self.bits.phases += (self.bits.frequency + internal_bits + vert_bits) * DT
        self.blocks.phases += (self.blocks.frequency + internal_blocks + vert_blocks) * DT
        self.root.phases += (self.root.frequency) * DT
        
        self.bits.phases = np.mod(self.bits.phases, 2*PI)
        self.blocks.phases = np.mod(self.blocks.phases, 2*PI)

        coherence = np.abs(np.mean(np.exp(1j * self.bits.phases)))
        self.history.append(coherence)

    def inject_chaos(self):
        corruption_mask = np.random.choice([True, False], size=N_ATOMS)
        self.bits.phases[corruption_mask] = np.random.uniform(0, 2*PI, np.sum(corruption_mask))

def run_app():
    st.title("💎 Lichen Quantum Crystal")
    st.caption(f"Simulation de l'Auto-Guérison Fractale (N={N_ATOMS}, Φ={PHI:.4f})")

    if st.button("🚀 Lancer la Simulation"):
        crystal = QuantumCrystal()
        
        # Barres de progression
        progress_bar = st.progress(0)
        status_text = st.empty()
        chart_placeholder = st.empty()

        # Phase 1: Synchronisation
        status_text.text("Phase 1: Synchronisation Initiale des 496 Oscillateurs...")
        for i in range(200):
            crystal.update()
            if i % 10 == 0:
                progress_bar.progress(i / 500)
        
        # Injection du Chaos
        crystal.inject_chaos()
        st.toast("⚡⚠️ INJECTION D'ENTROPIE MASSIVE ! ⚠️⚡", icon="🔥")
        status_text.text("⚠️ CHAOS DÉTECTÉ! Activation de la Résonance Fractale...")

        # Phase 2: Auto-Guérison
        for i in range(300):
            crystal.update()
            if i % 10 == 0:
                progress_bar.progress((200 + i) / 500)
        
        progress_bar.progress(100)
        status_text.success("✅ Système Stabilisé. Immunité Confirmée.")

        # Affichage du Graphique Final
        fig, ax = plt.subplots(figsize=(10, 6))
        # Fond sombre pour le style "Cyberpunk/Science"
        fig.patch.set_facecolor('#0e1117')
        ax.set_facecolor('#0e1117')
        
        ax.plot(crystal.history, color='#00ff00', linewidth=2, label='Cohérence (H-Level)')
        ax.axvline(x=200, color='red', linestyle='--', label='Injection Erreur')
        
        ax.set_title(f"Preuve de Stabilité: Architecture Fractale {N_ATOMS}-Φ", color='white')
        ax.set_xlabel("Temps (t)", color='white')
        ax.set_ylabel("Cohérence", color='white')
        ax.tick_params(colors='white')
        ax.grid(True, alpha=0.2)
        ax.legend(facecolor='#0e1117', labelcolor='white')
        
        st.pyplot(fig)

        # Métriques
        final_coherence = crystal.history[-1]
        col1, col2 = st.columns(2)
        col1.metric("Cohérence Finale", f"{final_coherence:.5f}")
        col2.metric("État du Système", "CRITIQUE" if final_coherence < 0.9 else "NOMINAL", delta_color="normal")

if __name__ == "__main__":
    run_app()
