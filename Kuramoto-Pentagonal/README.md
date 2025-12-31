# Kuramoto Pentagonal : Spin-Locking Protection
## Architecture de Correction d'Erreur Quantique Passive

<img width="2816" height="1536" alt="Gemini_Generated_Image_y46y1iy46y1iy46y" src="https://github.com/user-attachments/assets/815b7ed4-b617-4f43-aa78-0075d892fe0d" />


[![Status](https://img.shields.io/badge/status-theoretical_validation-blue)](docs/theory_spin_locking.md)
[![Version](https://img.shields.io/badge/version-1.0-green)](docs/theory_spin_locking.md)
[![Topology](https://img.shields.io/badge/topology-Pentagonal_C5-orange)](poc/pentagonal_sim.py)

> **"Error is not a bug. It is a loss of synchronization."**

**Kuramoto Pentagonal** is the quantum error correction layer of the Lichen architecture. Instead of costly active error correction (measuring and flipping bits), it uses **passive synchronization** (Kuramoto coupling) in a pentagonal topology to prevent errors from occurring in the first place.

## 🛡️ Core Principles

1.  **Passive Synchronization**: Spontaneous phase-locking via the Kuramoto Hamiltonian prevents decoherence.
2.  **Pentagonal Topology**: The $C_5$ symmetry creates a "frustrated" ground state that is robust against local perturbations.
3.  **CRAID Integration**: Provides 60% fault tolerance (data survives the loss of 2/5 qubits).

## 📂 Contents

* **`docs/theory_spin_locking.md`**: The full physics manifesto explaining the Hamiltonian and topological protection.
* **`poc/pentagonal_sim.py`**: A Python/QuTiP simulation script demonstrating the auto-correction mechanism.
* **`FORMULAS.md`**: The immutable mathematical reference (Hamiltonians).

## 🧪 Key Validations
* **Self-Healing**: Simulation shows spins realigning after noise injection.
* **Fault Tolerance**: Information persists with 2 dead qubits.
---
