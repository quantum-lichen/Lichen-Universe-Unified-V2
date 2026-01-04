import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import KDTree
from itertools import permutations, product
import time

# --- CONSTANTES ---
PHI = (1 + np.sqrt(5)) / 2
N_DIM = 8  # Dimension E8
N_VECTORS = 62  # Vecteurs par atome FC-496 (62 * 8 = 496 bits)
N_NODES = 5  # Topologie Pentagonale
K_COUPLING = 2.0  # Force de couplage Kuramoto (doit être > Kc)
NOISE_LEVEL = 0.3  # Bruit injecté pour tester E8
DT = 0.05  # Pas de temps simulation

class E8Geometry:
    """Générateur de la géométrie sacrée E8"""
    def __init__(self):
        print("⚡ Génération du réseau E8 (240 racines)...")
        self.roots = self._generate_roots()
        self.tree = KDTree(self.roots)
        print(f"✅ E8 KD-Tree construit. Prêt pour Spin-Lock.")

    def _generate_roots(self):
        roots = set()
        
        # Type 1: Permutations de (±1, ±1, 0, 0, 0, 0, 0, 0)
        # 112 racines
        base = [1, 1, 0, 0, 0, 0, 0, 0]
        for p in set(permutations(base)):
            # Pour chaque perm, on itère les signes
            # Optimisation: on sait où sont les 1
            indices = [i for i, x in enumerate(p) if x == 1]
            for s1 in [-1, 1]:
                for s2 in [-1, 1]:
                    v = list(p)
                    v[indices[0]] *= s1
                    v[indices[1]] *= s2
                    roots.add(tuple(v))

        # Type 2: (±0.5, ..., ±0.5) avec somme paire (ou nombre pair de signes +)
        # 128 racines
        for signs in product([-0.5, 0.5], repeat=8):
            # Condition E8 standard: somme des coordonnées est un entier pair
            # (Ce qui revient à dire nombre pair de signes négatifs ou positifs selon convention)
            # Ici on suit ta spec: nombre pair de signes positifs
            if sum(1 for x in signs if x > 0) % 2 == 0:
                roots.add(signs)
                
        return np.array(list(roots))

    def project(self, vector):
        """Spin-Lock: Projette un vecteur bruité sur la racine E8 la plus proche"""
        dist, idx = self.tree.query(vector)
        return self.roots[idx], dist

class FC496Atom:
    """Atome d'information Lichen (496 bits)"""
    def __init__(self, e8_geom):
        self.e8 = e8_geom
        # État idéal: 62 vecteurs E8 aléatoires
        self.vectors = self.e8.roots[np.random.choice(len(self.e8.roots), N_VECTORS)]
        self.corrupted_vectors = np.copy(self.vectors)
        self.error_count = 0

    def infect_with_noise(self, noise_level):
        """Injecte du chaos (bruit gaussien)"""
        noise = np.random.normal(0, noise_level, self.vectors.shape)
        self.corrupted_vectors = self.vectors + noise

    def apply_spin_lock(self):
        """Auto-guérison via E8"""
        corrected = []
        errors = 0
        for i in range(N_VECTORS):
            proj, dist = self.e8.project(self.corrupted_vectors[i])
            corrected.append(proj)
            # Si la correction a changé le vecteur par rapport à l'original (avant bruit)
            # Note: Dans la vraie vie on ne connait pas l'original, mais ici on mesure la performance
            if not np.allclose(proj, self.vectors[i]):
                errors += 1
        return np.array(corrected), errors

class PentagonNode:
    """Nœud du réseau Kuramoto"""
    def __init__(self, node_id, omega, e8_geom):
        self.id = node_id
        self.phase = np.random.uniform(0, 2*np.pi)
        self.omega = omega  # Fréquence naturelle (biais omega)
        self.atom = FC496Atom(e8_geom)
        self.history_phase = []
        self.history_errors = []

    def update_kuramoto(self, neighbors, k, dt):
        """Équation différentielle de synchronisation"""
        coupling = 0
        for n in neighbors:
            coupling += np.sin(n.phase - self.phase)
        
        d_theta = self.omega + (k / 2) * coupling # Divisé par 2 voisins
        self.phase += d_theta * dt
        self.history_phase.append(self.phase)

class HybridSimulation:
    def __init__(self):
        print("\n💠 INITIALISATION DU SIMULATEUR TAF-496 💠")
        self.e8 = E8Geometry()
        
        # Création des 5 nœuds (Topologie Pentagone)
        # On donne des fréquences naturelles légèrement différentes (chaos initial)
        self.nodes = [PentagonNode(i, 1.0 + np.random.normal(0, 0.1), self.e8) for i in range(N_NODES)]
        
        print(f"🔷 Pentagone initialisé. Couplage K={K_COUPLING}")

    def run(self, steps=200):
        print(f"\n🚀 Démarrage de la simulation ({steps} cycles)...")
        
        r_history = []
        correction_rates = []
        
        for t in range(steps):
            # 1. PHYSIQUE (E8 Spin-Lock)
            # On injecte du bruit et on corrige à chaque cycle
            total_vectors = 0
            total_errors = 0
            
            for node in self.nodes:
                node.atom.infect_with_noise(NOISE_LEVEL)
                _, errs = node.atom.apply_spin_lock()
                total_vectors += N_VECTORS
                total_errors += errs
                node.history_errors.append(errs)
            
            correction_rate = 1.0 - (total_errors / total_vectors)
            correction_rates.append(correction_rate)

            # 2. RÉSEAU (Kuramoto Update)
            # Topologie Pentagone: i est connecté à (i-1) et (i+1) modulo 5
            new_phases = []
            for i in range(N_NODES):
                left = self.nodes[(i-1)%N_NODES]
                right = self.nodes[(i+1)%N_NODES]
                self.nodes[i].update_kuramoto([left, right], K_COUPLING, DT)
            
            # 3. MÉTRIQUE (Paramètre d'ordre r)
            complex_phases = [np.exp(1j * n.phase) for n in self.nodes]
            r = np.abs(np.mean(complex_phases))
            r_history.append(r)
            
            if t % 20 == 0:
                print(f"Cycle {t}: Sync(r)={r:.3f} | E8 Correction={correction_rate*100:.1f}%")

        self.visualize(r_history, correction_rates)

    def visualize(self, r_hist, corr_hist):
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        # Plot Sync
        ax1.plot(r_hist, color='#00ff88', linewidth=2)
        ax1.set_title("Niveau Macro: Synchronisation Kuramoto (Topologie Pentagone)")
        ax1.set_ylabel("Cohérence (r)")
        ax1.set_ylim(0, 1.1)
        ax1.axhline(y=1.0, color='r', linestyle='--', alpha=0.3)
        ax1.grid(True, alpha=0.2)
        
        # Plot E8 Correction
        ax2.plot(corr_hist, color='#ff3366', linewidth=2)
        ax2.set_title(f"Niveau Micro: E8 Spin-Lock (Bruit={NOISE_LEVEL})")
        ax2.set_ylabel("Taux de Correction")
        ax2.set_xlabel("Temps (cycles)")
        ax2.set_ylim(0, 1.1)
        ax2.grid(True, alpha=0.2)
        
        plt.tight_layout()
        plt.show()

# --- MAIN ---
if __name__ == "__main__":
    sim = HybridSimulation()
    sim.run(steps=300)
