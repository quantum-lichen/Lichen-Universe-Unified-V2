"""
CHRONOS SPIRAL: Pi-Time Anchoring Module
Version: 2.1.6
Author: Lichen Collective

Transforme le temps linéaire (Unix) en temps spiralé (Pi-Index + Phi-Coords).
"""

import math
import time
import decimal

# --- CONSTANTES UNIVERSELLES ---
PHI = (1 + math.sqrt(5)) / 2  # 1.618...
PI  = math.pi                 # 3.141...
GOLDEN_ANGLE = 2 * PI * (1 - 1/PHI) # ~2.399 radians (137.5°)

class PiTimeAnchor:
    def __init__(self, unix_timestamp=None):
        self.timestamp = unix_timestamp if unix_timestamp else time.time()
        
        # 1. Conversion Temps -> Index Pi (Simulation)
        # Dans la prod, on utiliserait une BDD de Pi ou l'algo BBP.
        # Ici, on projette le timestamp sur un espace de 10^12 digits.
        self.pi_index = int(self.timestamp * PI * 1000)
        
        # 2. Calcul de la Spirale (Espace)
        self.r, self.theta = self._calculate_spiral_coords()
        self.x, self.y = self._polar_to_cartesian()

    def _calculate_spiral_coords(self):
        """
        Modelisation Phyllotaxis (Tournesol).
        Chaque tick de temps est une nouvelle graine dans la spirale.
        """
        # Le rayon grandit avec la racine carrée du temps (distribution uniforme)
        radius = math.sqrt(self.pi_index)
        
        # L'angle avance selon l'Angle d'Or pour éviter les répétitions
        theta = self.pi_index * GOLDEN_ANGLE
        
        return radius, theta

    def _polar_to_cartesian(self):
        x = self.r * math.cos(self.theta)
        y = self.r * math.sin(self.theta)
        return x, y

    def get_anchor_vector(self):
        """Retourne le vecteur complet pour le Header FC-496 (Minor Segment)"""
        return {
            "u_timestamp": self.timestamp,
            "pi_index": self.pi_index,  # Va dans le champ 'pi_index_start'
            "spiral_coords": {
                "r": round(self.r, 4),
                "theta": round(self.theta, 4),
                "x": round(self.x, 4),
                "y": round(self.y, 4)
            },
            "stability_factor": self._check_stability()
        }

    def _check_stability(self):
        # Vérifie si l'ancrage est sur un nœud harmonique (proche d'un entier de Phi)
        divergence = abs((self.r % PHI) - (PHI / 2))
        return 1.0 - divergence  # 1.0 = Parfaitement stable

# --- DEMO ---
if __name__ == "__main__":
    print(f"🌀 INITIALIZING CHRONOS SPIRAL...")
    print(f"   Golden Angle: {math.degrees(GOLDEN_ANGLE):.4f}°")
    
    # Simuler une séquence d'événements
    for i in range(5):
        now = time.time() + (i * 1000) # +1000 secondes par saut
        anchor = PiTimeAnchor(now)
        vec = anchor.get_anchor_vector()
        
        print(f"\n⏱️  Event #{i+1}")
        print(f"   Unix: {vec['u_timestamp']:.0f} -> π-Index: {vec['pi_index']}")
        print(f"   Coords (x,y): ({vec['spiral_coords']['x']}, {vec['spiral_coords']['y']})")
        print(f"   Harmonic Stability: {vec['stability_factor']:.4f}")
