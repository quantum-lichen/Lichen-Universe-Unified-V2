import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass

# --- CONSTANTES UNIVERSELLES ---
PHI = (1 + np.sqrt(5)) / 2  # Le Nombre d'Or (1.618...)
PI = np.pi
N_ATOMS = 496               # La constante de structure (Dimension E8)
COUPLING_STRENGTH = PHI     # La force de "gravité" informationnelle
DT = 0.01                   # Pas de temps (Time step)

@dataclass
class FractalLayer:
    name: str
    size: int
    frequency: float
    phases: np.ndarray

class QuantumCrystal:
    def __init__(self):
        print(f"💎 LICHEN QUANTUM CRYSTAL INITIALIZING...")
        print(f"   -> Constants: Φ={PHI:.4f}, N={N_ATOMS}")
        
        # Architecture Fractale à 3 Niveaux
        # Niveau 0 : L'Onde Porteuse (The One)
        self.root = FractalLayer("ROOT", 1, 1.0, np.zeros(1))
        
        # Niveau 1 : Les Blocs Structurels (Harmonique Phi)
        self.blocks = FractalLayer("BLOCKS", 8, PHI, np.random.uniform(0, 2*PI, 8))
        
        # Niveau 2 : Les Bits Physiques (496 oscillateurs)
        self.bits = FractalLayer("BITS", N_ATOMS, PHI**2, np.random.uniform(0, 2*PI, N_ATOMS))
        
        self.history = []

    def kuramoto_step(self, layer, coupling_k):
        """Calcule la synchronisation interne d'une couche."""
        # Somme des sinus des différences de phase (Mean Field)
        # dθ/dt = ω + K * mean(sin(θ_j - θ_i))
        order_parameter = np.mean(np.exp(1j * layer.phases))
        mean_phase = np.angle(order_parameter)
        
        # Force de rappel vers la moyenne
        delta = coupling_k * np.sin(mean_phase - layer.phases)
        return delta

    def fractal_coupling(self):
        """Lie les couches entre elles (Le 'Lock' Vertical)."""
        # 1. Les Bits écoutent les Blocs
        # On mappe 496 bits vers 8 blocs (62 bits par bloc)
        block_idx = np.arange(N_ATOMS) % 8
        parent_phases = self.blocks.phases[block_idx]
        vertical_force_bits = PHI * np.sin(parent_phases - self.bits.phases)
        
        # 2. Les Blocs écoutent la Racine
        vertical_force_blocks = PHI * np.sin(self.root.phases[0] - self.blocks.phases)
        
        return vertical_force_bits, vertical_force_blocks

    def update(self):
        """Avance le temps d'un pas (dt)."""
        
        # Calcul des forces internes (Latéral)
        internal_bits = self.kuramoto_step(self.bits, COUPLING_STRENGTH)
        internal_blocks = self.kuramoto_step(self.blocks, COUPLING_STRENGTH)
        
        # Calcul des forces fractales (Vertical)
        vert_bits, vert_blocks = self.fractal_coupling()
        
        # Application des équations différentielles (Euler method)
        # θ_new = θ_old + (ω + F_int + F_ext) * dt
        
        self.bits.phases += (self.bits.frequency + internal_bits + vert_bits) * DT
        self.blocks.phases += (self.blocks.frequency + internal_blocks + vert_blocks) * DT
        self.root.phases += (self.root.frequency) * DT # La racine est l'horloge maîtresse
        
        # Normalisation [0, 2π]
        self.bits.phases = np.mod(self.bits.phases, 2*PI)
        self.blocks.phases = np.mod(self.blocks.phases, 2*PI)

        # Mesure de la Cohérence (Order Parameter R)
        # R = 1.0 (Cristal Parfait) / R = 0.0 (Chaos Total)
        coherence = np.abs(np.mean(np.exp(1j * self.bits.phases)))
        self.history.append(coherence)

    def inject_chaos(self):
        """Simule une attaque massive ou une corruption de données."""
        print("\n⚡⚠️ INJECTION D'ENTROPIE MASSIVE (CHAOS) ⚠️⚡")
        # On corrompt 50% des bits avec du bruit aléatoire
        corruption_mask = np.random.choice([True, False], size=N_ATOMS)
        self.bits.phases[corruption_mask] = np.random.uniform(0, 2*PI, np.sum(corruption_mask))

def run_simulation():
    crystal = QuantumCrystal()
    
    print("   -> Phase 1: Initial Synchronization...")
    for _ in range(200):
        crystal.update()
        
    crystal.inject_chaos()
    
    print("   -> Phase 2: Self-Healing (Watch the Curve)...")
    for _ in range(300):
        crystal.update()
        
    # Visualisation
    plt.figure(figsize=(10, 6))
    plt.plot(crystal.history, color='#00ff00', linewidth=2, label='Cohérence du Système (H-Level)')
    plt.axvline(x=200, color='red', linestyle='--', label='Injection Erreur')
    plt.title(f"Preuve de Stabilité: Architecture Fractale {N_ATOMS}-Φ")
    plt.xlabel("Temps (t)")
    plt.ylabel("Cohérence (0=Chaos, 1=Cristal)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.style.use('dark_background')
    
    print("\n✅ SIMULATION COMPLETE.")
    print(f"   Final Coherence: {crystal.history[-1]:.5f}")
    if crystal.history[-1] > 0.99:
        print("   RESULT: SYSTEM IMMUNITY CONFIRMED. 🛡️")
    else:
        print("   RESULT: SYSTEM UNSTABLE.")
        
    plt.show()

if __name__ == "__main__":
    run_simulation()
