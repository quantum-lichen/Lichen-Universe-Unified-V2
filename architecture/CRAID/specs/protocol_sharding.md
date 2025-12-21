# Protocole de Sharding & Reconstruction

## 1. L'Approche "Structure > Vecteur"
Contrairement aux RAG classiques qui se basent sur une similarité vectorielle floue, CRAID force une structure.
* **Entrée** : Hypergraphe de connaissances.
* **Traitement** : Le monde n'est pas binaire. CRAID gère les relations complexes (ex: Alice envoie un mail à Bob à propos du Projet X).

## 2. Mutabilité & Édition (Le Défi LSM)
Avec Reed-Solomon, on ne peut pas modifier un bit sans tout recalculer.
* **Solution** : Architecture **LSM (Log-Structured Merge-tree)**.
* Les nouvelles informations s'empilent ("Log") par-dessus les anciennes.
* Un processus de fond ("Compaction") fusionne périodiquement les logs pour mettre à jour les shards "froids" de manière asynchrone.

## 3. Topologie de Réseau
* **Nœuds** : Chaque Agent (instance de SynapseΩ) agit comme un nœud de stockage potentiel.
* **Protocole** : Communication via vecteurs d'états (State Vectors) pour vérifier l'intégrité des shards voisins.
