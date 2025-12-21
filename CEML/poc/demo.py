# LMEC_CEML/demo.py
# Moteur de Sélection Cognitive basé sur la Loi de Minimisation de l'Entropie Cognitive
# Auteur : Bryan Ouellette

import math
import numpy as np

# --- CONSTANTES ---
PHI = (1 + math.sqrt(5)) / 2  # Le Nombre d'Or
EPSILON = 1e-9                # Régularisation

class CognitiveSelector:
    def __init__(self, context_vector):
        self.context = np.array(context_vector)
        # Normalisation du contexte
        self.context = self.context / np.linalg.norm(self.context)

    def calculate_coherence(self, candidate_vector):
        """Calcule C(s|Ω) : Similarité Cosinus"""
        v = np.array(candidate_vector)
        norm = np.linalg.norm(v)
        if norm == 0: return 0.0
        v = v / norm
        return np.dot(self.context, v)

    def calculate_entropy(self, data_string):
        """Calcule H(s) : Entropie de Shannon approximée"""
        if not data_string: return 0.0
        # Probabilité par caractère
        prob = [float(data_string.count(c)) / len(data_string) for c in dict.fromkeys(list(data_string))]
        entropy = -sum([p * math.log2(p) for p in prob])
        # Normalisation (approx) pour rester entre 0 et 1 pour la démo
        return entropy / 8.0 

    def evaluate(self, candidates):
        results = []
        for cand in candidates:
            C = self.calculate_coherence(cand['vector'])
            H = self.calculate_entropy(cand['text'])
            
            # L'Équation Maîtresse CEML
            score = C / (H + EPSILON)
            
            # Classification
            status = "REJECT"
            if score > PHI: status = "SELECT (Resonance)"
            elif C > 0.9 and H < 0.1: status = "FLAG (Hallucination?)"
            
            results.append({
                "text": cand['text'],
                "C": round(C, 4),
                "H": round(H, 4),
                "Score": round(score, 4),
                "Status": status
            })
        
        # Tri par score décroissant (Sélection naturelle)
        return sorted(results, key=lambda x: x['Score'], reverse=True)

# --- EXEMPLE D'UTILISATION ---
if __name__ == "__main__":
    # Contexte : "Le ciel est..." (Vecteur simulé)
    selector = CognitiveSelector([0.8, 0.2, 0.1])
    
    candidates = [
        {"text": "bleu", "vector": [0.9, 0.1, 0.05]},       # Cohérent, Simple
        {"text": "une soupe quantique inversée", "vector": [0.1, 0.8, 0.1]}, # Incohérent, Complexe
        {"text": "bleu bleu bleu bleu", "vector": [0.9, 0.1, 0.05]} # Cohérent, mais redondant
    ]
    
    ranking = selector.evaluate(candidates)
    print("--- RÉSULTATS CEML ---")
    for r in ranking:
        print(f"J={r['Score']:.3f} | {r['Status']} | Text: {r['text']}")
