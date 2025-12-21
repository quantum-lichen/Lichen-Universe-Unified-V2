# La Polymérase Sémantique
**Le Moteur d'Ingestion et de Découpage**

Ce composant est responsable de la transformation de la donnée brute en structure CRAID. C'est le goulot d'étranglement économique et technique qu'il faut optimiser.

## ⚙️ Le Pipeline "Hélicase -> Ribosome"

1.  **Hélicase (Extraction)** :
    * La donnée brute (ex: PDF de 100 pages) est "déroulée".
    * *Optimisation :* Utilisation de **SLM (Small Language Models)** type Mistral-7B pour l'extraction brute afin de réduire les coûts, réservant GPT-4o pour la validation complexe.

2.  **Chain of Density** :
    * Compression de l'information pour maximiser la densité informative par token.
    * Conversion en "Nucléotides Sémantiques" (Structure : Sujet -> Prédicat -> Objet).

3.  **Sharding (Encodage Reed-Solomon)** :
    * Les nucléotides sont fragmentés.
    * Calcul de la parité mathématique.
    * *Règle :* `N` shards de données + `M` shards de parité. La reconstruction nécessite seulement `N` fragments quelconques.

4.  **Distribution** :
    * Les shards sont dispersés vers les agents disponibles (Noeuds de stockage).

## ⚠️ Contraintes Critiques
* **Coût d'ingestion** : L'extraction est coûteuse en tokens. L'usage de modèles locaux est impératif pour la viabilité.
* **Latence de Reconstruction** : Reassembler le contexte pour une réponse temps réel doit se faire via un cache "Hot Memory" pour éviter de décoder du Reed-Solomon à chaque requête utilisateur.
