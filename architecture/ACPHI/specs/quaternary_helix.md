# Spécification de l'Hélice Quaternaire
**Protocole:** GKF-496 (Genomic Kernel Framework)
**Unité:** Le Codon (248 Quits = 496 Bits)

---

## 1. Les 4 Bases Géométriques
Nous remplaçons ATCG par des constantes mathématiques pour l'universalité.

| Base | Symbole | Valeur Binaire | Rôle Métaphysique |
| :--- | :---: | :---: | :--- |
| **$\Phi_0$** | `00` | Identité | Fondation, Neutre ($\varphi^0$) |
| **$\Phi_1$** | `01` | Expansion | Croissance Fractale ($\varphi^1$) |
| **$\Pi_0$** | `10` | Cycle | Boucle Temporelle ($\pi/\varphi$) |
| **$\Pi_1$** | `11` | Transcendance | Abstraction ($\pi$) |

## 2. Encodage Différentiel Rotatif
Pour éviter les erreurs de lecture (glissement), la valeur n'est pas dans la base, mais dans la **transition**.

* État actuel : $B_t$
* Donnée à écrire (0, 1, 2) : $\Delta$ (3 est interdit/réservé contrôle)
* État suivant : $B_{t+1} = (B_t + \Delta + 1) \pmod 4$

> **Règle d'Or :** Une base ne peut jamais être suivie par elle-même. (Pas de $\Phi_0 \to \Phi_0$).

## 3. La Double Hélice $\Phi$ (Validation)
Chaque brin "Sens" ($S$) est accompagné d'un brin "Anti-Sens" ($A$).
Contrairement à Watson-Crick (A-T), notre complémentarité est mathématique :
$$A[i] = S[i] \oplus \text{0b11} \quad (\text{Inversion Bitwise})$$

La validité du génome est vérifiée par la **Résonance** :
$$\text{Resonance} = \frac{\sum (S[i] \cdot A[i])}{\text{Total}} \approx \frac{1}{\varphi}$$
