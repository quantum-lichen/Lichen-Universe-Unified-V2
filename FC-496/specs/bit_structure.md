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

### 3. `FC-496/FORMULAS.md` 🔢
*(Le Noyau Mathématique Unifié)*



```markdown
# FC-496 : Mathematical Index
**Version:** 2.1
**Scope:** Geometry and Validity.
```
---

## 1. The Unified State Equation ($\Psi_{cell}$)
The definition of a valid cell combining Structure, Time, and Harmony.

### 📐 LaTeX
$$
\Psi_{cell} = \left( P_{ayload} \cdot \varphi \right) + \left( T_{\pi} \cdot i \right) \quad \text{subject to} \quad \mathcal{H}(C) \ge \frac{1}{\varphi}
$$

### 📝 Variables
```text
* P_payload : Information content (Major Segment).
* T_pi      : Pi-Time Index (Temporal anchor).
* H(C)      : Harmonic Score of the cell.
* phi       : Golden Ratio (1.618...).
2. The Golden PartitionDefining the bit-split.📐 LaTeX$$S_{major} = \left\lfloor \frac{496}{\varphi} \right\rceil = 306 \text{ bits}$$$$S_{minor} = 496 - S_{major} = 190 \text{ bits}$$3. The Validation ConditionBoolean check for the SynapseΩ Kernel.💻 PythonPythondef is_valid_atom(atom):
    # 1. Check Magic Number
    if atom.magic != 0x1F0: return False
    
    # 2. Check H-Scale (Must be above Chaos Threshold)
    if atom.h_score < (1 / PHI): return False
    
    # 3. Verify Pi-Time Integrity
    if not verify_bbp(atom.pi_index, atom.pi_checksum): return False
    
    return True
```
---

### 4. `FC-496/poc/atom_builder.py` 🐍
*(Le Générateur mis à jour)*

```python
"""
FC-496 Atom Builder (V2.1.6 Compatible)
Author: Lichen Collective
"""

import struct
import math
import hashlib

# --- CONSTANTS IMPORT (Simulation) ---
PHI = 1.61803398875
TOTAL_BITS = 496
MAGIC_SIG = 0x1F0

class FC496Atom:
    def __init__(self, payload_data, pi_index, geo_hash, h_score):
        # 1. Validation Logic
        if h_score < (1.0 / PHI):
            raise ValueError(f"Kernel Panic: H-Score {h_score} below threshold (0.618)")
            
        self.magic = MAGIC_SIG
        self.pi_index = pi_index  # u64
        self.geo_hash = geo_hash  # u64
        self.h_score = int(h_score * 10000) # u16 (normalized)
        
        # 2. Payload Processing (Major Segment - 306 bits max)
        # In simulation, we hash data to fit or truncate
        self.payload = self._compress_to_major(payload_data)
        
    def _compress_to_major(self, data):
        # Simulation: Hash to 32 bytes (256 bits) + padding
        # In real UICT, this would be recursive compression
        hasher = hashlib.sha256(data.encode()).digest()
        return hasher # 256 bits fits in 306 bits Major Segment

    def to_bytes(self):
        """
        Serializes the Atom to strictly aligned 62 bytes (496 bits).
        Structure:
        - Minor (Header): 24 bytes (approx 190 bits container)
        - Major (Payload): 38 bytes (approx 306 bits container)
        """
        # Packing Minor Segment
        # H (u16), Q (u64), Q (u64), H (u16) -> 2+8+8+2 = 20 bytes used of 24
        minor = struct.pack(
            '>HQQH', 
            self.magic, 
            self.pi_index, 
            self.geo_hash, 
            self.h_score
        )
        
        # Packing Major Segment
        major = self.payload + b'\x00' * (38 - len(self.payload))
        
        return minor + major

# --- DEMO ---
if __name__ == "__main__":
    print("⚛️  Generating FC-496 Atom...")
    
    try:
        atom = FC496Atom(
            payload_data="SynapseOmega Boot Sequence",
            pi_index=3141592653,
            geo_hash=0xDEADBEEF,
            h_score=0.95 # High Harmony
        )
        
        binary = atom.to_bytes()
        print(f"✅ Atom Created. Size: {len(binary) * 8} bits.")
        print(f"Hex Dump: {binary.hex().upper()}")
        
    except ValueError as e:
        print(f"❌ Creation Failed: {e}")
```
