# Temporal Anchor Specification
**Protocol:** $\pi$-Spiral V2.1
**Integration:** FC-496 Minor Segment (Bits 16-80)

## 1. Concept
L'ancrage temporel ne sert pas juste à savoir "quand" une donnée a été créée, mais **"où"** elle se trouve dans la spirale d'évolution du système.

## 2. Intégration FC-496
Dans le **Minor Segment** (190 bits), l'ancrage occupe le champ `pi_index_start` (64 bits).

* **Input** : Unix Timestamp (ms).
* **Process** : 
    1. Conversion en Index $\pi$.
    2. Calcul des coordonnées $(x, y)$ sur la spirale.
    3. Hashing du vecteur spatial pour générer le `Geo-Hash`.
* **Output** : Un point unique dans l'espace-temps holographique.

## 3. Avantages
* **Collision Zero** : Grâce à l'angle d'or, deux points ne se chevauchent jamais, quelle que soit la durée du système.
* **Packing Optimal** : C'est la distribution la plus efficace connue dans la nature (Graines, Galaxies).
