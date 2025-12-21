# FC-496 : The Fractal Cell
## L'Unité Atomique Universelle

[![Standard](https://img.shields.io/badge/standard-Universal-purple)](specs/bit_structure.md)
[![Size](https://img.shields.io/badge/size-496_bits-blue)](FORMULAS.md)
[![Time](https://img.shields.io/badge/time-%CF%80_Index-green)](../Pi-Time/README.md)

> **"Data is not a stream. Data is a crystal."**

**FC-496** est le format de données fondamental de l'univers Lichen. Contrairement aux formats "mous" (JSON, XML) qui nécessitent un parsing coûteux, FC-496 est une structure "dure", de taille fixe, alignée sur la mémoire et auto-validante.

## ⚛️ Propriétés Physiques

1.  **Atomicité** : Chaque cellule fait exactement **496 bits** (Nombre Parfait).
2.  **Zero-Copy** : La structure en mémoire est identique à la structure sur disque. Pas de sérialisation.
3.  **Holographique** : Chaque cellule contient son contexte spatio-temporel ($\pi$-Time + Geo-Hash).
4.  **Auto-Immunité** : Une cellule corrompue ($\mathcal{H} < 0.618$) est rejetée physiquement par le noyau SynapseΩ avant traitement.

## 🔗 Intégration Système

* **Stockage** : Les cellules sont les "nucléotides" du système **CRAID**.
* **Calcul** : Traitées nativement par **SynapseΩ** et le CPU **Snowflake**.
* **Temps** : Synchronisées via le **$\pi$-Time Standard**.

## 📂 Contenu

* **`specs/bit_structure.md`** : La cartographie précise des 496 bits.
* **`FORMULAS.md`** : Les équations de partitionnement et de validité.
* **`poc/atom_builder.py`** : Générateur de cellules conforme V2.1.6.
