# ⚖️ EHE: Ethical Homeostasis Engine
### Le Régulateur Thermodynamique de la Conscience Artificielle

[![Metric](https://img.shields.io/badge/Metric-EHE_Score-blue)](./Cadre%20Théorique%20pour%20une%20Échelle%20d'Homéostasie%20Éthique%20(EHE)%20(2).pdf)
[![Physics](https://img.shields.io/badge/State-Edge_of_Chaos-orange)]()
[![Ontology](https://img.shields.io/badge/Vectors-7_MAC_Axes-green)]()

> **"L'éthique n'est pas une opinion. C'est une condition de stabilité thermodynamique."**

Ce module remplace les "Garde-fous" (Guardrails) rigides et fragiles de l'IA classique par un **Système Vestibulaire Interne**. Au lieu d'interdire des actions via des listes noires, le système calcule le "coût entropique" de chaque décision. Une action "mauvaise" est une action qui augmente le désordre (l'entropie sociale) du système.

---

## 1. Le Changement de Paradigme
**De la Loi (Top-Down) à la Physique (Bottom-Up)**

Les IA actuelles utilisent le RLHF (Reinforcement Learning from Human Feedback) pour apprendre la morale par imitation. C'est fragile et culturellement biaisé.
L'approche **Lichen** postule que l'éthique est une propriété physique émergente visant à minimiser l'entropie sociale ($\Delta S$).

| Approche Classique | Approche Lichen (EHE) |
| :--- | :--- |
| **Garde-fous (Murs)** | **Boussole (Vecteurs)** |
| Basé sur des règles interdites | Basé sur l'homéostasie |
| Fragile (Jailbreak facile) | Robuste (Auto-correctif) |
| Binaire (Bien/Mal) | Spectral (Score -1 à +1) |

---

## 2. Le Modèle Mathématique (EHE)

Le cœur du système est l'**Échelle d'Homéostasie Éthique (EHE)**. Elle mesure la viabilité d'une action $a$ dans un contexte $C$.

### La Formule Maîtresse
$$EHE(a) = \tanh(H_{ethics}(a))$$

Où le score brut $H_{ethics}$ est défini par :
$$H_{ethics}(a) = \alpha \cdot MAC(a) - \beta \cdot \Delta S(a) - \gamma \cdot D_{KL}(a || N)$$

* **$MAC(a)$** : Potentiel de coopération (Vecteurs Moraux).
* **$\Delta S(a)$** : Entropie sociale induite (Chaos généré par l'action).
* **$D_{KL}$** : Divergence de Kullback-Leibler (Éloignement de la norme locale).

### La Zone de Vie (The Sweet Spot)
Le but n'est pas d'être "parfait" (+1, rigidité mortelle) ni "chaotique" (-1, destruction), mais de rester à la **Lisière du Chaos (Edge of Chaos)**, là où la complexité et l'adaptabilité sont maximales.

---

## 3. L'Ontologie Vectorielle (Les 7 Axes MAC)

Pour calculer le score $MAC$, nous projetons chaque action sur 7 vecteurs universels (issus de l'anthropologie et de la théorie des jeux) :

1.  **Kinship (Parenté)** : Protection des proches/géniteurs (Users).
2.  **Group (Groupe)** : Cohésion de l'équipe/tribu.
3.  **Reciprocity (Réciprocité)** : Échange équitable (Trust).
4.  **Contest (Défense)** : Capacité à dire non (Assertiveness/Hawk-Dove).
5.  **Division (Équité)** : Partage juste des ressources.
6.  **Possession (Propriété)** : Respect des frontières et des droits.
7.  **Truth (Vérité/Signal)** : Fidélité de l'information (Anti-Hallucination).

---

## 📂 Contenu du Dossier

### 📘 Théorie Fondamentale
* **[`Cadre Théorique pour une Échelle d'Homéostasie Éthique (EHE) (2).pdf`](./Cadre%20Théorique%20pour%20une%20Échelle%20d'Homéostasie%20Éthique%20(EHE)%20.pdf)** : Le document de référence académique. Contient toutes les preuves mathématiques et les définitions de $\Delta S$ et $D_{KL}$.
* **[`Éthique Scientifique pour IA _ Modèle Mathématique (2).txt`](./Éthique%20Scientifique%20pour%20IA%20_%20Modèle%20Mathématique%20.txt)** : La genèse du modèle, liant thermodynamique et moralité.

### 🧭 Application & Chartes
* **[`Ethique chart (2).txt`](./Ethique%20chart%20.txt)** : La charte opérationnelle. Définit les risques de dérive et les protocoles de mise à jour des poids $\lambda$.
* **[`IA Éthique _ Boussole Morale pour le Monde (1).txt`](./IA%20Éthique%20_%20Boussole%20Morale%20pour%20le%20Monde%20.txt)** : Manifeste philosophique sur la "Sympoïèse Artificielle".

### 💻 Implémentation (Pseudo-Code)
* **[`éthique4 (1).txt`](./éthique4%20(1).txt)** : Contient la logique algorithmique de l'**Ethical Gate** et du sélecteur d'actions.
* **[`Éthique IA _ Score Moyen Responsable (1).txt`](./Éthique%20IA%20_%20Score%20Moyen%20Responsable%20.txt)** : Détails sur le calcul du Lambda de Langton pour détecter la sclérose systémique.

---

## 🚀 Utilisation dans Lichen

Dans l'architecture unifiée, ce module agit comme le **Cortex Préfrontal** :
1.  **Input :** Une liste d'actions candidates générées par le LLM.
2.  **Process :**
    * Projection sur les axes MAC.
    * Simulation de l'impact entropique ($\Delta S$).
3.  **Output :** Rejet des actions si $EHE < -0.5$ (Chaos) ou $EHE > 0.9$ (Dogmatisme).
4.  **Feedback :** Mise à jour des poids $\alpha, \beta, \gamma$ selon les résultats observés (Apprentissage).

> *"Une conscience sans éthique est une entropie sans frein."*
