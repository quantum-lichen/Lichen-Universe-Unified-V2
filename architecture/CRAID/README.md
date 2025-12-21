# CRAID : Cognitive RAID Architecture
## La Mémoire "Self-Healing" pour Agents Autonomes

> **"Le mariage du Hard Engineering (RAID, Reed-Solomon) et de la Soft AI (Embeddings, Sémantique)."**

### 🎯 Le Problème
Dans les systèmes IA actuels, la mémoire est fragile. Si on perd l'instance d'un agent ou son index vectoriel (`index.faiss`), l'IA devient amnésique.

### 💡 La Solution CRAID
CRAID applique la logique du stockage distribué (RAID 5/6) à la sémantique.
Au lieu de stocker un fichier complet à un endroit, nous décomposons l'information en **"Shards Sémantiques"** distribués à travers le réseau d'agents (via FC-496).

### 🔥 Les 3 Piliers du Système
1.  **Résilience (Self-Healing)** : Si un agent meurt, les autres détiennent assez de fragments (parity shards) pour reconstruire mathématiquement l'information manquante sans perte de sens.
2.  **Atomicité (FC-496)** : L'unité de base n'est pas le bit, mais le [Nucléotide Sémantique] (Sujet -> Prédicat -> Objet + Embedding).
3.  **Hybridité (Hot/Cold)** :
    * **Hot Memory (Cache)** : Répliquée pour la vitesse (<100ms).
    * **Cold Storage (CRAID)** : Shardée et encodée pour l'immortalité et la densité.

---
