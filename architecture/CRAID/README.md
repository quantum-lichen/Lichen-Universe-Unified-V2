# CRAID : Cognitive RAID Architecture
## La Mémoire "Self-Healing" pour Agents Autonomes

[![Status](https://img.shields.io/badge/status-active_development-orange)](specs/protocol_sharding.md)
[![Version](https://img.shields.io/badge/version-1.0-green)](specs/protocol_sharding.md)
[![Resilience](https://img.shields.io/badge/fault_tolerance-60%25-blue)](FORMULAS.md)

> **"Memory is not a file. It is a reconstruction."**

**CRAID** (Cognitive Redundant Array of Independent Datasets) applies distributed storage logic to semantic memory. It ensures that the knowledge graph survives even if individual agents (nodes) go offline.

## 🛡️ Core Pillars

1.  **Structure > Vector**: Uses "Semantic Nucleotides" (Subject-Predicate-Object) wrapped in embeddings, rather than vague vectors.
2.  **Self-Healing**: Implements Reed-Solomon erasure coding. Data is sharded; if a node dies, the math rebuilds the missing context.
3.  **Hybrid Tiering**:
    * **Hot Memory**: Replicated for speed (<100ms).
    * **Cold Storage**: Sharded for density and immortality.

## 📂 Contents

* **`specs/protocol_sharding.md`**: The distributed storage protocol and Reed-Solomon specs.
* **`concepts/semantic_polymerase.md`**: The ingestion pipeline (Helicase -> Nucleotides).
* **`FORMULAS.md`**: The mathematical rules for parity and reconstruction.

## 🚀 Key Metric
**60% Fault Tolerance**: With a (3+2) encoding scheme, the system survives the loss of 2 out of 5 agents.
