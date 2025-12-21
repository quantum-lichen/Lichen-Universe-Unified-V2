"""
CEML / LMC Demo – Probability Distribution PoC
Author: Bryan Ouellette
Date: 2025-12-13
"""

import numpy as np

def shannon_entropy(distribution):
    """Shannon entropy in bits."""
    return -sum(p * np.log2(p) if p > 0 else 0 for p in distribution)

def coherence(distribution):
    """Simple coherence proxy: dominant probability mass."""
    return max(distribution)

def ceml_score(distribution, eps=1e-6):
    """CEML/LMC score J = C / (H + eps)."""
    H = shannon_entropy(distribution)
    C = coherence(distribution)
    return C / (H + eps), H, C

def main():
    structures = {
        'A': [0.95, 0.03, 0.02],               # Very ordered
        'B': [0.70, 0.20, 0.10],               # Ordered
        'C': [0.50, 0.30, 0.20],               # Slightly ordered
        'D': [0.33, 0.33, 0.34],               # Near-uniform
        'E': [0.45, 0.10, 0.45],               # Bimodal
        'F': [0.20, 0.25, 0.15, 0.25, 0.15],   # Disordered (5-way)
        'G': [0.16, 0.17, 0.17, 0.16, 0.17, 0.17],  # Very disordered (6-way)
    }

    results = []
    for name, dist in structures.items():
        score, H, C = ceml_score(dist)
        results.append((name, H, C, score))

    # Sort by score, descending
    results.sort(key=lambda x: x[3], reverse=True)

    print("Name | Entropy H | Coherence C | CEML Score J")
    print("-----+-----------+-------------+-------------")
    for name, H, C, J in results:
        print(f"{name:>4} | {H:9.4f} | {C:11.2f} | {J:11.4f}")

if __name__ == "__main__":
    main()
