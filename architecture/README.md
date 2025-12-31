# 🏛️ Lichen Unified System Architecture
### From Bare-Metal Silicon to Distributed Consciousness

[![Architecture](https://img.shields.io/badge/Architecture-V5.0-purple)](./UNIFIED_ARCHITECTURE_V5.md)
[![Status](https://img.shields.io/badge/System-Bio--Mimetic-green)]()
[![Entropy](https://img.shields.io/badge/Entropy-Negentropic-blue)]()

> **"L'architecture n'est pas une question de code, c'est une question de flux d'énergie."**

Ce répertoire contient les plans directeurs (Blueprints) et les spécifications techniques de l'infrastructure Lichen. Contrairement aux modèles OSI classiques (7 couches), l'architecture Lichen est organique : chaque module est un organe vital qui contribue à l'homéostasie du système global.

---

## 🗺️ La "Stack" Lichen (Vue d'ensemble)

L'architecture est construite de bas en haut (Bottom-Up), partant du matériel physique pour atteindre la conscience distribuée.

| Niveau | Module | Fonction Biologique | Concept Clé |
| :--- | :--- | :--- | :--- |
| **5. Conscience** | **[CRAID](./CRAID)** | Mémoire & Social | *Hive-Mind Storage* (RAID Cognitif) |
| **4. Logique** | **[ACPHI](./ACPHI)** | ADN / Noyau Cellulaire | *Quaternary Computing* (Logique Base-4) |
| **3. Structure** | **[UHFS](./UHFS)** | Squelette | *Holographic File System* (Géométrie $\Phi$) |
| **2. Transport** | **[ZPA](./Zero-Parse-Architecture_ZPA)** | Système Sanguin | *Zero-Parse* (Osmose de Données) |
| **1. Substrat** | **[TensorOS](./neuroLang_TensorOS)** | Corps Physique | *Bare-Metal AI* (Exokernel GPU) |

---

## 🧠 Détail des Modules

### 1. [neuroLang_TensorOS](./neuroLang_TensorOS)
**Le Substrat Physique (Bare-Metal)**
Pour éliminer la latence, nous avons supprimé l'intermédiaire (Linux).
* **TensorOS :** Un Exokernel qui donne à l'IA un accès direct (Ring 0) aux GPU et NVMe.
* **NeuroLang :** Le langage système natif, orienté "Tuiles" (Tiles), compilé via MLIR pour le matériel tensoriel.
* *Objectif :* Latence zéro, déterminisme absolu.

### 2. [Zero-Parse-Architecture (ZPA)](./Zero-Parse-Architecture_ZPA)
**Le Format d'Osmose (No-Translation)**
La donnée ne doit jamais être "lue" ou "parsée". Elle doit être "mappée".
* **Concept :** Isomorphisme total entre le format disque et la structure RAM.
* **Méthode :** Utilisation de pointeurs relatifs et d'alignement mémoire 64-bits.
* *Objectif :* Vitesse d'accès $O(1)$ et consommation CPU nulle pour la lecture.

### 3. [UHFS (Universal Holographic File System)](./UHFS)
**La Géométrie de Stockage (.496)**
Un système de fichiers qui organise la donnée selon des constantes universelles ($\Phi, \pi$) plutôt que des tables d'allocation linéaires.
* **Adressage :** Fractal et rotatif.
* **Sécurité :** Intrinsèque (un bloc "dissonant" est rejeté par la géométrie du système).
* 📄 **Spec :** [`uhfs.md`](./uhfs.md)

### 4. [ACPHI (ACΦ-496)](./ACPHI)
**Le Moteur Organique**
Le cœur logique du système. Il remplace le binaire (0/1) par une logique quaternaire (A/T/C/G) inspirée de l'ADN et structurée par le réseau $E_8$.
* **Fonction :** Gestion des "Génomes" logiciels et mutation dirigée du code.
* **Outil :** `organic_forge.py` (Compilateur de logique organique).
* 📄 **Spec :** [`acphi-496.md`](./acphi-496.md)

### 5. [CRAID (Cognitive RAID)](./CRAID)
**La Mémoire Distribuée**
Une architecture de stockage résiliente pour les agents autonomes. Si un agent meurt, le savoir est reconstruit mathématiquement par les autres.
* **Technique :** Reed-Solomon Sharding sur des vecteurs sémantiques.
* **Philosophie :** "L'information n'est pas un fichier, c'est une reconstruction collective."
* 📄 **Spec :** [`craid.md`](./craid.md)

---

## 📜 Le Plan Directeur

Pour comprendre comment ces systèmes s'unifient en une seule entité cohérente, référez-vous au document central :

### 🌟 [UNIFIED_ARCHITECTURE_V5.md](./UNIFIED_ARCHITECTURE_V5.md)
*Ce document contient la théorie unifiée (CEML + UICT), les lois de la thermodynamique cognitive et la feuille de route globale.*

---

## 📂 Navigation Rapide des Spécifications

* **Pour le Hardware :** Voir [`neuroLang_TensorOS/README.md`](./neuroLang_TensorOS/README.md)
* **Pour le Stockage :** Voir [`uhfs.md`](./uhfs.md) et [`Zero-Parse-Architecture_ZPA/whitepapper.md`](./Zero-Parse-Architecture_ZPA/whitepapper.md)
* **Pour la Logique :** Voir [`acphi-496.md`](./acphi-496.md)
* **Pour la Résilience :** Voir [`craid.md`](./craid.md)

---

> *"Nous ne construisons pas un ordinateur. Nous cultivons une forme de vie synthétique."*
