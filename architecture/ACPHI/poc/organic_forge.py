"""
ACΦ-496 ORGANIC FORGE
Version: 2.2-ORGANIC
Author: Lichen Collective

Implémente la logique Quaternaire Rotative et le Système Immunitaire.
"""

import random

# --- CONSTANTES ---
BASES = ['Φ₀', 'Φ₁', 'Π₀', 'Π₁'] # 00, 01, 10, 11
PHI = 1.61803398875

class QuaternaryStrand:
    def __init__(self, data_bytes):
        self.raw_data = data_bytes
        self.bases = []
        self.immune_status = "HEALTHY"
        
        # 1. Transmutation Binaire -> Quaternaire Rotatif
        self._transmute()
        
        # 2. Génération du brin complémentaire (Double Hélice)
        self.complementary = self._generate_antisense()

    def _transmute(self):
        """Encodage Différentiel Rotatif (Anti-Homopolymère)"""
        current_state = 0 # Start at Φ₀
        
        # On lit les bits par paires (0-3)
        # Note: Dans une vraie implém, on utiliserait un flux de bits continu
        # Ici on simule pour la démo
        byte_stream = int.from_bytes(self.raw_data, 'big')
        bit_length = len(self.raw_data) * 8
        
        for i in range(0, bit_length, 2):
            # Extraction de 2 bits (valeur 0-3)
            # On mappe 3 sur une séquence d'échappement en prod, 
            # ici on utilise modulo 3 pour garantir la rotation.
            val = (byte_stream >> i) & 0b11
            move = val % 3 # 0=+1, 1=+2, 2=+3
            
            # Rotation : On ne reste jamais sur place
            next_state = (current_state + move + 1) % 4
            
            self.bases.append(next_state)
            current_state = next_state

    def _generate_antisense(self):
        """Génère le brin miroir (Bitwise Invert)"""
        return [(b ^ 0b11) for b in self.bases]

    def immune_scan(self):
        """
        Système Immunitaire Artificiel (Sélection Négative)
        Détecte les séquences interdites (Non-Soi).
        """
        print("🛡️  SYSTEM IMMUNE SCAN INITIATED...")
        
        # Règle 1: Pas de répétition (Homopolymère)
        for i in range(len(self.bases)-1):
            if self.bases[i] == self.bases[i+1]:
                self.immune_status = "INFECTED (Homopolymer Error)"
                print(f"   ⚠️  ANOMALY DETECTED at index {i}: Stagnation.")
                return False

        # Règle 2: Résonance Phi (Simulation)
        # Dans la théorie, on vérifierait l'alignement E8.
        # Ici on vérifie la cohérence dimensionnelle.
        if len(self.bases) % 2 != 0: # Doit être pair pour la symétrie
             # Correction génétique (Genetic Improvement)
             self.bases.append(0) 
             print("   🧬 GENETIC REPAIR: Padding added.")

        print("   ✅ SCAN COMPLETE. Tissue is Healthy.")
        return True

    def visualize(self):
        """Affiche la double hélice"""
        res = ""
        for i in range(min(10, len(self.bases))): # Show first 10
            s = BASES[self.bases[i]]
            a = BASES[self.complementary[i]]
            res += f"{s}═{a}\n"
        return res

# --- DEMO ---
if __name__ == "__main__":
    print("🧬 ACΦ-496 ORGANIC FORGE BOOTING...\n")
    
    # Donnée : "Lichen"
    data = b"Lichen" 
    organism = QuaternaryStrand(data)
    
    print(f"📥 Input: {data}")
    print(f"🧬 Bases générées: {len(organism.bases)} Quits")
    
    # Affichage Hélice
    print("\nDouble Helix Structure (Fragment):")
    print(organism.visualize())
    
    # Scan Immunitaire
    is_safe = organism.immune_scan()
    
    print(f"\n🏥 Status: {organism.immune_status}")
