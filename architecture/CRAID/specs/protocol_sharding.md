# CRAID Protocol: Sharding & Resilience
**Version:** 1.0
**Scope:** Distributed Semantic Storage

---

## 1. The Semantic Nucleotide
Unlike standard RAID which stripes bits, CRAID stripes **Semantic Nucleotides**.
Each shard contains a piece of the knowledge graph, ensuring that even a partial reconstruction yields usable meaning.

## 2. Erasure Coding (Reed-Solomon)
We use an $(N, M)$ scheme where:
* $N$ = Data Shards (Content)
* $M$ = Parity Shards (Redundancy)
* **Total Shards** = $N + M$
* **Reconstruction Requirement** = Any $N$ shards.

**Standard Configuration:** $(3, 2)$
* Splits data into 3 parts.
* Adds 2 parity blocks.
* Distributes across 5 Agents.
* *Result:* Can lose any 2 agents and still recover 100% of the memory.

## 3. The LSM Tree (Mutability)
To handle the "Write Once" nature of Reed-Solomon:
1.  **MemTable**: New memories enter a RAM buffer (Hot).
2.  **Immutable SSTables**: When full, buffer is flushed to disk as sharded SSTables (Cold).
3.  **Compaction**: Background process merges old tables and discards obsolete facts.
