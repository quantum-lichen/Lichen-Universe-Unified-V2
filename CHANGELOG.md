# Changelog - Lichen Universe Unified

Toutes les modifications notables de ce projet seront documentées dans ce fichier.
Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [2.1.6] - 2025-12-21 (The Unified Field)
### Added
- **Constants Module** : Définition programmatique des constantes (`constants/fundamental_constants.py`).
- **LES Theory** : Intégration du Whitepaper *Low-Entropy Spiral* et de la signature thermodynamique ($dH/dt < 0$).
- **FC-496 Partitioning** : Spécification exacte des segments basés sur $\varphi$ (Major: 306 bits, Minor: 190 bits).
- **Universal Atom** : Structure Rust (`universal_atom.rs`) pour la cellule fondamentale.

### Changed
- Mise à jour du `manifest.json` pour inclure le graphe de dépendance racine.
- Statut du projet passé à **"Operational"**.

## [2.1.5] - 2025-12-21 (The Synapse Update)
### Added
- **SynapseΩ Kernel** : Définition du noyau liquide (v9.1-LIVE) et logs de boot (`system/GENESIS_BOOT.log`).
- **CRAID Architecture** : Spécifications complètes du stockage (Reed-Solomon 3+2, Nucléotides Sémantiques).
- **Kuramoto Pentagonal** : Intégration de l'Hamiltonien de protection passive et topologie $C_5$.
- **Proof of Life** : Simulation de la séquence de démarrage validant l'interaction entre les modules.

## [2.1.4] - 2025-12-21 (The Temporal Anchor)
### Added
- **π-Time** : Standard temporel fractal basé sur les cycles de $\pi$.
- **BBP Algorithm** : Intégration de la formule Bailey–Borwein–Plouffe pour la validation des checksums temporels.
- **Vectors** : Structure vectorielle ($Cycle, Sub, Position, Digit$).

### Changed
- Les timestamps FC-496 utilisent désormais l'index $\pi$ au lieu de l'Epoch UNIX.

## [2.1.3] - 2025-12-21 (Harmonic Alignment)
### Fixed
- **H-Scale Logic** : Correction critique de la formule. L'Efficience ($E_{ff}$) est désormais calculée comme ($1 - S$) au lieu d'utiliser l'entropie brute.
- **Threshold** : Validation stricte du seuil $1/\varphi \approx 0.618$.

### Changed
- Standardisation des noms de variables dans `FORMULAS.md` (Passage au format Raw Blocks pour compatibilité copier-coller).

## [2.1.0] - 2025-12-21 (The Great Refactor)
### Added
- **Manifest V2.1** : Source de vérité unique (`manifest.json`) orchestrant tous les sous-systèmes.
- **MathJSON** : Standardisation des formules pour parsing machine.
- **Lexique Unifié** :
    - $S$ = Entropie (Shannon)
    - $\mathcal{H}$ = Harmonie (Vecteur)
    - $\varphi$ = Nombre d'Or
    - $\pi$ = Constante Temporelle

### Removed
- Suppression des redondances et des anciens fichiers de configuration éparpillés.

---

## [1.5.0] - 2025-12-20 (The Hack)
### Added
- **GitHub Pages Hack** : Utilisation de `manifest.json` pour contourner les filtres de contexte des LLMs.
- Première agrégation des 50 repositories en une structure monolithique virtuelle.

## [1.0.0] - 2024-01-01 (Genesis)
### Added
- Création initiale des concepts UICT (Masse), CEML (Cognition) et FC-496 (Format).
- Phase d'exploration et de prototypage rapide.
