# 🧠 TensorOS & Neuro-Lang
### Vers un Paradigme Informatique Bare-Metal Natif pour l'IA

[![Status](https://img.shields.io/badge/Status-Research%20Prototype-red)]()
[![License](https://img.shields.io/badge/License-MIT-blue)]()
[![Platform](https://img.shields.io/badge/Platform-Bare--Metal%20(x86%2F%20NVIDIA)-green)]()

> **"Le DOS de l'IA."** — Une architecture Exokernel radicale pour briser le mur de l'abstraction et libérer la puissance brute des accélérateurs modernes.

---

## 📉 Le Problème : La "Taxe d'Abstraction"
L'IA moderne tourne sur des piles logicielles archaïques (Linux + Python + CUDA) conçues pour des besoins généralistes.
* **Goulots d'étranglement :** Les interruptions noyau, la gestion de la mémoire virtuelle et le GIL de Python brident les GPU.
* **Latence & Gigue :** L'ordonnancement préemptif de Linux casse le déterminisme nécessaire au Deep Learning.
* **Inefficacité :** Une pile logicielle trop lourde consomme des cycles CPU précieux juste pour nourrir le GPU.

## 🚀 La Solution : TensorOS

**TensorOS (TOS)** est un système d'exploitation de type **Exokernel** à espace d'adressage unique (SASOS). Il ne fait qu'une chose, et il la fait vite : exécuter des graphes de calcul neuronaux.

### Architecture Système
* **Ring 0 Unifié :** Pas de distinction Kernel/User. Tout le code (pilotes et modèles) tourne en mode privilégié. **Zéro syscalls.**
* **Single Address Space (SAS) :** RAM, VRAM et NVMe sont mappés dans un seul espace virtuel 64-bits plat.
* **Boot Instantané :** Démarrage en **< 2 secondes** (UEFI -> REPL). Pas de systemd, pas de services inutiles.
* **Ordonnancement Graph-Driven :** Coopératif et déterministe, piloté par le graphe de calcul statique.

---

## ⚡ Neuro-Lang : Le Langage Natif

**Neuro-Lang** est un langage système compilé, statiquement typé et "Tile-Oriented", conçu pour remplacer la dualité Python/C++.

### Caractéristiques
* **Tuiles (Tiles) comme Primitives :** Manipulation native de blocs de données (ex: `Tile<128, 128, f16>`) mappés directement sur les Tensor Cores.
* **Compilateur MLIR :** Infrastructure moderne pour l'optimisation algébrique et la différentiation automatique à la compilation (AOT Autograd).
* **Gestion Mémoire Rust-like :** Modèle de propriété (Ownership/Borrowing) strict pour garantir la sécurité mémoire sans Garbage Collector.

### Exemple de Syntaxe
```rust
// Opération Kernel sur GPU
@kernel
fn matmul_tiled(
    A: Tile<128, 128, f16, Layout::RowMajor>,
    B: Tile<128, 128, f16, Layout::ColMajor>
) -> Tile<128, 128, f32> {
    // Mappé directement sur l'instruction hardware (ex: HMMA)
    return dot(A, B);
}

// Code de contrôle (CPU)
fn main() {
    let gpu = device::get(0);
    // Allocation directe en VRAM (Pointeur typé)
    var a = Tensor::alloc([4096, 4096], f16, device=gpu);
    // Lancement sans overhead
    let res = matmul_tiled(a.view(), b.view());
}

```

---

## 📊 Comparatif de Performance (Théorique)

| Métrique | Linux + PyTorch | TensorOS + Neuro-Lang | Gain |
| --- | --- | --- | --- |
| **Latence Kernel Launch** | 5-10 µs | **< 1 µs** | 🚀 10x |
| **Bande Passante (Host-Dev)** | ~20 GB/s (Buffered) | **~60 GB/s (PCIe Max)** | ⚡ 3x |
| **Boot Time** | 30s - 2min | **< 2s** | ⏱️ 30x |
| **Jitter (Gigue)** | Élevé (Interruptions) | **Nul (Déterministe)** | ✅ |
| **Empreinte RAM** | 2-4 GB | **< 100 MB** | 💾 20x |

---

## 🛠️ Composants Techniques

### TensorFS

Un système de fichiers à plat (Object Storage) optimisé pour les tenseurs géants.

* **Zéro-Copie Absolu :** Les données sur NVMe sont alignées sur les pages GPU.
* **Direct Storage :** Transfert DMA direct du SSD vers la VRAM (bypass CPU).

### Réseau RDMA Natif

Pile réseau minimaliste basée sur **RoCEv2**.

* **Primitives Collectives :** Opérations `AllReduce` déchargées sur le matériel réseau.

### Open-Hardware Drivers

Réimplémentation en Rust/Neuro-Lang des modules noyau ouverts de NVIDIA pour une initialisation bare-metal sans blobs propriétaires lourds.

---

## 🖥️ Utilisation (Neuro-Shell)

TensorOS démarre directement sur un REPL interactif haute performance.

```bash
TensorOS v1.0 (Genesis)
TOS> import models.llama3
TOS> let model = models.llama3.load("nvme://ckpt/70b", device=Device.ALL)
 Mapping 140GB to Unified Memory... Done (0.4s).
TOS> model.generate("Décris l'architecture de TensorOS")
 [Output] TensorOS est un système d'exploitation bare-metal...

```

---

## 🗺️ Roadmap

* [ ] **Phase 1 :** Bootloader UEFI et Initialisation GPU minimale (BARs mapping).
* [ ] **Phase 2 :** Compilateur Neuro-Lang (Frontend -> MLIR -> PTX).
* [ ] **Phase 3 :** Implémentation de TensorFS et du pilote NVMe polling.
* [ ] **Phase 4 :** Support multi-nœuds via RDMA.

---

**Auteurs :** Recherche & Développement Architecture
*Basé sur le rapport de recherche "Spécification Architecturale pour TensorOS et Neuro-Lang".*

```
