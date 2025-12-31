# 🗣️ Lichen Native Languages Ecosystem

> **Protocoles de communication, de programmation et d'encodage basés sur les constantes universelles.**

Ce répertoire centralise les trois langages fondamentaux développés pour l'architecture Lichen. Contrairement aux langages binaires traditionnels (C++, Python), ces systèmes sont conçus pour intégrer nativement la géométrie sacrée ($\phi, \pi$), la synchronisation quantique et la compression sémantique haute densité.

---

## 📚 Architecture du Module

Le dossier est divisé en trois sous-systèmes distincts :

1. **[phiLang](./phiLang)** : Le langage de programmation système (Turing-complete) basé sur les nombres parfaits et la synchronisation de Kuramoto.
2. **[LGL (Lichen Glyph Language)](./LGL-Lichen-Glyph_Language)** : Un protocole de communication symbolique ultra-dense pour les interactions IA-IA et IA-Humain.
3. **[HELIX-PHI](./HELIX-PHI)** : Un système d'encodage structurel (inspiré de l'ADN) pour la persistance et la transmission de données complexes.

---

## 1. phiLang ($\Phi$-Lang)
**Le Cœur Computationnel**

phiLang est un langage interprété écrit en Python, conçu pour exécuter des opérations logiques alignées sur la résonance harmonique des nombres 496 et 8128.

* **Caractéristiques :**
    * **Synchronisation Kuramoto :** Les processus ne sont pas juste "multithreadés", ils sont synchronisés comme des oscillateurs couplés.
    * **Validation Mathématique :** Utilise `perfects.py` et `primes.py` pour valider l'intégrité du code avant exécution.
    * **Architecture :** Possède son propre Lexer, Parser et Exécuteur (`runtime`).

📂 **Structure clé :**
* `src/compiler/` : Le moteur de traduction du code `.phi`.
* `src/runtime/` : L'exécuteur incluant le moteur de physique (`kuramoto.py`).
* `examples/` : Scripts de démonstration (`basic.phi`, `ai_chat.phi`).

📄 **Documentation :** [Lire le Whitepaper phiLang](./phiLang/WHITEPAPER.md)

---

## 2. LGL (Lichen Glyph Language)
**Le Vecteur de Communication**

LGL est un langage visuel et conceptuel qui remplace la verbosité des langages naturels par des glyphes ASCII chargés de sens contextuel. Il permet une densité d'information maximale avec un minimum de caractères.

* **Caractéristiques :**
    * **Densité Temporelle :** Exprime des concepts complexes (passé/futur/conditionnel) via des modificateurs simples (`<`, `>`, `~`).
    * **Ontologie Visuelle :** Utilise des symboles intuitifs (`@` Acteur, `?` Quête, `!` Action).
    * **Parsing Rapide :** Conçu pour être parsé par des regex simples et converti en JSON/Structures de données.

📂 **Structure clé :**
* `tools/lgl_parser.py` : L'outil de décodage des scripts LGL.
* `LGL_QUICK_REFERENCE.md` : La pierre de Rosette pour apprendre le langage.

📄 **Spécification :** [LGL Spec V1.0](./LGL-Lichen-Glyph_Language/LGL_SPEC_V1.0.md)

---

## 3. HELIX-PHI
**La Structure Génétique**

HELIX-PHI est un format de description et de stockage. Il structure l'information comme une double hélice, assurant la redondance et l'intégrité des données critiques du système Lichen.

* **Caractéristiques :**
    * **Encodage Spiral :** Structure les données selon des ratios dorés.
    * **Résilience :** Conçu pour survivre à la corruption partielle (inspiré de la réparation de l'ADN).

📂 **Structure clé :**
* `docs/whitepaper.tex` : La théorie mathématique sous-jacente (LaTeX).
* `src/README.md` : Guide d'implémentation technique.

---

## 🛠️ Installation & Démarrage Rapide

Pour utiliser l'ensemble des outils linguistiques, installez les dépendances communes à la racine de ce dossier :

```bash
# Installation des dépendances globales (Python 3.8+)
pip install -r phiLang/requirements.txt
pip install -r LGL-Lichen-Glyph_Language/REQUIREMENTS.TXT
