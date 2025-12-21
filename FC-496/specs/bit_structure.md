# FC-496 Bit Structure Specification
**Version:** 2.1 (Unified)
**Total Size:** 496 Bits (62 Bytes)

---

## 1. The Golden Partition ($\varphi$)
The cell is divided into two energetic segments based on the Golden Ratio.

| Segment | Taille (Bits) | Taille (Bytes) | Rôle |
| :--- | :---: | :---: | :--- |
| **MAJOR** | **306** | ~38.25 | **Payload** (Contenu Sémantique compressé) |
| **MINOR** | **190** | ~23.75 | **Control** (Contexte, Temps, Sécurité) |

*Ratio Réel : $306 / 190 \approx 1.6105$ (Erreur < 0.5% vs $\varphi$)*

---

## 2. Detailed Bitmap (Memory Map)

### 🟦 MINOR SEGMENT (Control) - 190 Bits
*Situé en début de cellule pour lecture rapide par le Kernel.*

1.  **Magic Signature (16 bits)** : `0x1F0` (496 en Hex). Identifie le format.
2.  **$\pi$-Index (64 bits)** : Position absolue dans les décimales de $\pi$. (Remplace Timestamp).
3.  **Geo-Hash (64 bits)** : Coordonnée spatiale fractale (Icosaèdre tronqué).
4.  **Schema Class (16 bits)** : Type de donnée (Texte, Image, Neurone, Lien).
5.  **$\mathcal{H}$-Score (16 bits)** : Signature harmonique (Cohérence).
6.  **Flags & Permissions (14 bits)** : Read/Write, Exec, Encrypted, etc.

### 🟧 MAJOR SEGMENT (Payload) - 306 Bits
*Le contenu utile.*

1.  **Content Vector (256 bits)** : Embedding sémantique ou Donnée brute compressée (UICT).
2.  **StrandGraph Links (34 bits)** : Pointeurs relatifs vers les cellules voisines (Liaisons chimiques).
3.  **Cyclic Redundancy (16 bits)** : Checksum local (BCH).

---

## 3. Visual Representation

```text
[ HEADER (16) | PI-TIME (64) | GEO (64) | H-SCORE (16) | FLAGS (14) ] -- MINOR (190)
[ -------------------- PAYLOAD VECTOR (256) ----------------------- ] -- MAJOR (306)
[ LINKS (34) | CRC (16) ] ------------------------------------------- -- MAJOR (End)
```
---
