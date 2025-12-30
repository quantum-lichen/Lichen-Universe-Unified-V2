# **Rapport de Recherche : Spécification Architecturale pour TensorOS et Neuro-Lang – Vers un Paradigme Informatique Bare-Metal Natif pour l'IA**

## **1\. Introduction : La Crise de l'Abstraction dans le Calcul Haute Performance**

L'histoire de l'informatique moderne est celle d'une sédimentation progressive de couches d'abstraction. Depuis les premiers systèmes de traitement par lots jusqu'aux systèmes d'exploitation (OS) multi-utilisateurs préemptifs actuels comme Linux et Windows, chaque évolution a visé à virtualiser les ressources matérielles pour en faciliter le partage et la sécurité. Cependant, l'avènement de l'Intelligence Artificielle (IA), et plus particulièrement de l'apprentissage profond (Deep Learning), a provoqué une rupture fondamentale dans les besoins computationnels. Nous assistons aujourd'hui à une divergence croissante entre les capacités théoriques du matériel – accélérateurs massivement parallèles (GPU, TPU) – et l'efficacité réelle des piles logicielles conçues pour des architectures généralistes axées sur la latence.1

La problématique centrale réside dans le fait que les systèmes d'exploitation conventionnels sont optimisés pour l'équité (fairness) entre les processus et la réactivité des interfaces utilisateur, des objectifs diamétralement opposés aux exigences de l'IA qui requiert un débit soutenu (throughput), un déterminisme absolu et un accès exclusif aux ressources matérielles.3 Le paradigme actuel, qui consiste à empiler Python, des frameworks lourds comme PyTorch, des bibliothèques d'exécution C++, et des pilotes propriétaires au-dessus d'un noyau Linux monolithique, introduit une "taxe d'abstraction" insoutenable. Cette taxe se manifeste par des goulots d'étranglement au niveau de l'ingestion des données, de la gigue (jitter) introduite par l'ordonnanceur de l'OS, et d'une gestion inefficace de la mémoire virtuelle.2

Ce rapport propose une refonte radicale de cette architecture à travers deux concepts novateurs : **TensorOS**, un système d'exploitation de type "Exokernel" à espace d'adressage unique (SASOS), conçu comme l'équivalent moderne du DOS pour l'IA ; et **Neuro-Lang**, un langage de programmation "orienté tuiles" (tile-oriented) compilé directement pour ce nouvel environnement bare-metal. L'objectif est de créer un système situé "à mi-chemin entre le BIOS et l'OS", capable d'exposer la puissance brute des accélérateurs sans l'interférence d'une gestion de ressources généraliste.

## **2\. Analyse des Goulots d'Étranglement dans la Pile Logicielle Actuelle**

Pour justifier la nécessité d'un nouveau système d'exploitation et d'un nouveau langage, il convient d'abord de disséquer rigoureusement les pathologies de la pile technologique actuelle (Linux/Python/CUDA).

### **2.1 Le Fardeau du Noyau Monolithique et de la Mémoire Virtuelle**

Les systèmes d'exploitation généralistes comme Linux reposent sur une gestion de la mémoire virtuelle conçue pour isoler les processus les uns des autres. Chaque processus dispose de son propre espace d'adressage virtuel, et le noyau utilise une unité de gestion de mémoire (MMU) pour traduire ces adresses en adresses physiques via des tables de pages.

Dans le contexte du Deep Learning, où les modèles et les jeux de données atteignent plusieurs centaines de gigaoctets, voire des téraoctets, cette gestion devient un obstacle majeur. Les accès mémoire aléatoires dans de vastes tableaux de tenseurs peuvent provoquer des défauts de cache TLB (Translation Lookaside Buffer) fréquents, ralentissant considérablement l'exécution.1 De plus, le mécanisme d'interruption du noyau Linux, essentiel pour gérer les périphériques dans un environnement multitâche, devient une source de perturbation. Lors de l'entraînement d'un réseau de neurones, le flux de données vers le GPU doit être continu. Or, le noyau interrompt régulièrement ce flux pour traiter des tâches d'arrière-plan (démons réseau, journalisation, gestionnaire de fenêtres), introduisant une latence stochastique imprévisible.3

Le tableau ci-dessous illustre les inefficacités inhérentes à la gestion des entrées/sorties (E/S) dans un OS traditionnel pour des charges de travail d'IA :

| Composant | Comportement OS Traditionnel (Linux) | Impact sur l'IA |
| :---- | :---- | :---- |
| **Ordonnanceur CPU** | Préemption temporelle (Time-slicing) pour l'équité | Interruptions de l'alimentation du GPU, famine des cœurs tenseurs |
| **Gestionnaire d'E/S** | Tampons multiples (Kernel space \-\> User space) | Latence de copie mémoire, saturation de la bande passante CPU 3 |
| **Système de Fichiers** | Hiérarchique, basé sur des blocs génériques (4KB) | Fragmentation des tenseurs géants, overhead des métadonnées POSIX |
| **Pilotes GPU** | Boîtes noires en espace noyau (Kernel Mode) | Surcoût des appels système (syscalls) pour lancer chaque noyau de calcul 5 |

### **2.2 La "Taxe des Deux Langages" et les Limites de Python**

L'écosystème actuel est dominé par Python en raison de sa facilité d'utilisation et de sa riche bibliothèque scientifique. Cependant, Python n'est pas adapté à la programmation système haute performance nécessaire pour piloter les accélérateurs modernes.6

1. **Le GIL (Global Interpreter Lock) :** Ce mécanisme empêche l'exécution simultanée de plusieurs threads Python, limitant la capacité du CPU à préparer les données et à lancer les noyaux GPU en parallèle, créant un goulot d'étranglement au niveau du CPU (CPU-bound) avant même que le GPU ne soit saturé.7  
2. **Typage Dynamique et Surcharge :** L'interpréteur Python doit vérifier les types à l'exécution, ce qui empêche de nombreuses optimisations de bas niveau concernant l'agencement mémoire des tenseurs.8  
3. **La Dichotomie Python/C++ :** Pour contourner la lenteur de Python, les parties critiques sont écrites en C++, CUDA ou Triton. Cela crée une fracture dans le développement : le chercheur qui écrit le modèle en Python ne peut pas facilement optimiser les opérations sous-jacentes sans changer de langage et de chaîne d'outils.9

Bien que des projets comme Mojo tentent de résoudre ce problème en "réparant" Python 12, et que Triton permette d'écrire des noyaux GPU en syntaxe Python 13, ces solutions restent assujetties aux limites du système d'exploitation sous-jacent.

## ---

**3\. Architecture de TensorOS : Le Concept de "DOS pour l'IA"**

**TensorOS** (TOS) est proposé comme la solution radicale à ces problèmes. Il s'agit d'un système d'exploitation **Exokernel** à espace d'adressage unique (SASOS \- Single Address Space Operating System), conçu pour exécuter une seule application à la fois : l'environnement d'exécution Neuro-Lang. L'analogie avec le DOS (Disk Operating System) est pertinente : c'est un système mono-utilisateur, mono-tâche (au sens applicatif), sans interface graphique, donnant un accès total et direct au matériel.14

### **3.1 Philosophie : L'Exokernel et le Bare-Metal**

Dans une architecture Exokernel, le rôle du noyau est réduit au strict minimum : multiplexer le matériel en toute sécurité, sans fournir d'abstractions de haut niveau. Au lieu de fournir un "système de fichiers", l'Exokernel fournit un accès sécurisé aux blocs du disque. C'est à la "LibOS" (ici, le runtime Neuro-Lang) de décider comment structurer ces données.16

Pour TensorOS, nous poussons ce concept vers l'unification totale. Puisqu'il n'y a qu'un seul utilisateur et une seule application active (l'entraînement ou l'inférence), la protection mémoire entre processus devient superflue.

* **Mode Ring 0 Unifié :** L'ensemble du code, du pilote GPU à la boucle d'entraînement du réseau de neurones, s'exécute en mode privilégié (Ring 0 sur x86). Cela supprime totalement le coût des appels système (syscalls) qui, dans Linux, nécessitent des changements de contexte coûteux pour passer du mode utilisateur au mode noyau.4  
* **Espace d'Adressage Unique (SAS) :** TensorOS mappe toute la mémoire disponible (RAM système, VRAM GPU, mémoire persistante NVMe via MMIO) dans un seul espace d'adressage virtuel 64 bits plat.15

### **3.2 Séquence de Démarrage et Initialisation**

Contrairement à un OS généraliste qui peut prendre plusieurs minutes à charger des services, TensorOS vise un temps de démarrage inférieur à 2 secondes, rappelant l'instantanéité des machines 8-bits ou des consoles de jeux anciennes générations.19

1. **Bootloader UEFI Personnalisé :** TensorOS ne s'appuie pas sur GRUB. Il utilise un chargeur EFI minimal (TOS.EFI). L'UEFI initialise le matériel de base, passe le processeur en mode 64 bits (Long Mode), et charge le binaire du noyau directement en mémoire.20  
2. **Initialisation Matérielle Minimaliste :** Le noyau scanne le bus PCIe pour identifier les accélérateurs (GPU). Au lieu de charger un pilote générique complexe, il initialise uniquement les registres de base (BARs \- Base Address Registers) nécessaires pour communiquer avec le GPU.5  
3. **Interface Console GOP :** Pour l'affichage, TensorOS utilise le protocole *Graphics Output Protocol* (GOP) de l'UEFI. Il n'y a pas de serveur d'affichage (X11/Wayland). Le texte est rendu directement dans le framebuffer linéaire fourni par le firmware, offrant une console haute résolution rapide et légère.23  
4. **Lancement du REPL :** Le système rend la main immédiatement à l'interpréteur de commandes Neuro-Lang (le REPL), prêt à recevoir des instructions.

### **3.3 Gestion de la Mémoire et "Zéro-Copie" Absolu**

L'innovation majeure de TensorOS réside dans sa gestion unifiée de la mémoire. Dans Linux, déplacer des données du disque vers le GPU implique souvent : Disque \-\> Cache Page (Noyau) \-\> Tampon Utilisateur \-\> Mémoire Pinned \-\> DMA \-\> GPU.

Dans TensorOS :

* **Pointeur Universel :** Un pointeur 64 bits peut désigner une adresse en RAM, en VRAM ou sur le SSD (via Memory Mapped I/O).  
* **Chargement par Mapping :** Charger un modèle de 100 Go ne provoque aucune lecture immédiate. L'OS mappe simplement les adresses physiques du NVMe dans l'espace virtuel.  
* **Direct Storage :** Lorsque le GPU a besoin des données, il utilise ses moteurs DMA pour lire directement les adresses physiques du NVMe (technologie similaire à GPUDirect Storage ou NVIDIA RTX IO), sans que les données ne transitent par les registres du CPU.26

### **3.4 Ordonnancement Coopératif Graph-Driven**

TensorOS abandonne l'ordonnancement préemptif (time-slicing). L'exécution est pilotée par le graphe de calcul (Computation Graph).

* **Approche Déterministe :** Puisque la structure du réseau de neurones est connue à l'avance (statique), le compilateur Neuro-Lang peut générer un plan d'exécution précis. L'ordonnanceur n'a pas à "deviner" quelle tâche prioriser ; il suit simplement le graphe de dépendances des tenseurs.1  
* **Monopole du Processeur :** Lorsqu'un noyau de calcul est lancé, il monopolise les ressources nécessaires jusqu'à sa complétion. Si une opération d'E/S est requise, le CPU attend activement (polling) ou bascule sur une autre branche du graphe, éliminant la gigue des interruptions.29

## ---

**4\. Neuro-Lang : Spécification du Langage**

**Neuro-Lang** est le langage natif de TensorOS. Il ne s'agit pas d'un langage de script, mais d'un langage système compilé, statiquement typé, conçu pour manipuler des tenseurs comme des types primitifs (au même titre que int ou float en C).

### **4.1 Syntaxe et Philosophie : "Tout est une Tuile"**

Inspiré par les travaux sur Triton 13 et les extensions MLIR 30, Neuro-Lang adopte une approche "Tile-Oriented". Les accélérateurs modernes ne traitent pas les scalaires efficacement ; ils traitent des blocs (tuiles) de données.

#### **4.1.1 Le Type Tile**

Le type fondamental est la tuile. Contrairement aux tableaux NumPy qui sont des vues sur la mémoire, une Tile en Neuro-Lang possède des sémantiques matérielles strictes (taille, layout, localisation).

Rust

// Exemple de syntaxe Neuro-Lang (Hypothétique)

// Définition d'une opération de noyau  
// @kernel indique que ce code est destiné à l'accélérateur (GPU/TPU)  
@kernel  
fn matmul\_tiled(  
    A: Tile\<128, 128, f16, Layout::RowMajor\>,   
    B: Tile\<128, 128, f16, Layout::ColMajor\>  
) \-\> Tile\<128, 128, f32\> {  
      
    // L'opération 'dot' est intrinsèque et mappée directement   
    // sur les Tensor Cores (ex: instruction HMMA sur NVIDIA)  
    return dot(A, B);  
}

// Code hôte (exécuté par le CPU de contrôle dans TensorOS)  
fn main() {  
    // Allocation directe en VRAM (Pointeur typé)  
    let gpu\_dev \= device::get(0);  
    var a \= Tensor::alloc(, f16, device=gpu\_dev);  
    var b \= Tensor::alloc(, f16, device=gpu\_dev);

    // Lancement du noyau : Le compilateur gère la grille  
    // Pas de syntaxe CUDA complexe \<\<\<grid, block\>\>\>  
    let result \= matmul\_tiled(a.view(), b.view());  
      
    console::print(result);  
}

Cette syntaxe force le développeur à penser en termes de hiérarchie mémoire (registres, mémoire partagée, VRAM) dès l'écriture du code, mais avec une abstraction plus propre que CUDA.13

### **4.2 Le Compilateur : Infrastructure MLIR**

Neuro-Lang n'est pas construit de zéro, mais repose sur **MLIR (Multi-Level Intermediate Representation)**, une technologie de compilateur modulaire issue de LLVM.30

1. **Frontend Neuro :** Le code source est parsé en un dialecte MLIR de haut niveau (neuro.ir). Ce dialecte préserve la sémantique des graphes de tenseurs.  
2. **Optimisation Algébrique :** À ce niveau, le compilateur effectue la fusion d'opérateurs (ex: combiner une convolution, un biais et une activation ReLU en un seul noyau).34  
3. **Différentiation Automatique (Autograd) :** Contrairement à PyTorch qui construit le graphe de gradient à l'exécution (dynamique), le compilateur Neuro-Lang génère le code de la passe arrière (backward pass) lors de la compilation, en utilisant des techniques de différentiation source-à-source (similaire à Enzyme ou JAX).35  
4. **Backend Bare-Metal :**  
   * Pour le CPU (contrôle), il génère du code machine x86-64 sans dépendance à la glibc.  
   * Pour le GPU, il génère directement de l'assembleur PTX ou SASS (NVIDIA) ou ISA GCN (AMD), sans passer par les bibliothèques d'exécution lourdes comme libcuda.so.37

### **4.3 Modèle de Mémoire : Propriété et Emprunt (Ownership & Borrowing)**

La gestion de la mémoire sur GPU est source fréquente de bugs (fuites, désallocations prématurées). Neuro-Lang adopte un modèle de propriété inspiré de Rust.39

* **Propriété Unique :** Un tenseur a un seul propriétaire. Lorsqu'il est passé à un noyau, la propriété est "empruntée" (borrowed) par le GPU.  
* **Sécurité à la Compilation :** Le compilateur vérifie qu'un tenseur n'est pas libéré par le CPU tant que le GPU a des commandes en attente qui l'utilisent. Cela élimine le besoin d'un ramasse-miettes (Garbage Collector) coûteux en temps réel.  
* **Allocateurs d'Arène :** Pour éviter la fragmentation de la mémoire GPU, Neuro-Lang favorise les allocateurs de type "Arena" ou "Stack". Toute la mémoire nécessaire pour une étape d'entraînement est allouée en bloc au début, et libérée en bloc à la fin.42

## ---

**5\. Spécifications Techniques Détaillées du Système**

### **5.1 Gestion des Pilotes GPU : L'Approche "Open-Hardware"**

Le principal défi de TensorOS est le support matériel, notamment pour les GPU NVIDIA qui nécessitent des firmwares signés et des séquences d'initialisation complexes.

**Stratégie d'Implémentation :**

1. **Modules Open Kernel :** NVIDIA a récemment publié ses modules noyau en open source sous licence GPL/MIT.44 TensorOS adapte ce code C en Rust/Neuro-Lang pour créer une séquence d'initialisation bare-metal.  
   * Chargement du firmware GSP (GPU System Processor).  
   * Initialisation des liens PCIe.  
   * Mapping des BARs (Base Address Registers).  
2. **Contrôle par l'Espace Utilisateur (Userspace Driver) :** Une fois le GPU initialisé, TensorOS mappe les registres de commande (Doorbell registers) directement dans l'espace d'adressage de l'application. Neuro-Lang écrit les commandes directement dans les files d'attente du GPU (Ring Buffers). C'est la méthode utilisée par les applications ultra-basse latence (HFT) pour contourner le noyau.5

### **5.2 Système de Fichiers : TensorFS**

Les systèmes de fichiers traditionnels (EXT4, NTFS) sont optimisés pour des millions de petits fichiers hiérarchisés. L'IA a besoin de stocker quelques milliers de fichiers gigantesques (checkpoints, datasets).

**TensorFS** est un système de stockage objet à plat :

* **Adressage par Hash :** Les données sont identifiées par le hash de leur contenu ou un identifiant unique (UUID), pas par un chemin /home/user/....47  
* **Alignement Physique :** Les tenseurs sont stockés sur le disque NVMe en blocs alignés sur la taille de page du GPU (ex: 64KB ou 2MB). Cela permet le transfert direct (Peer-to-Peer DMA) du SSD vers la VRAM sans réalignement ni copie intermédiaire par le CPU.27  
* **Journalisation Structurée (Log-Structured) :** Pour maximiser la durée de vie des SSD lors des écritures fréquentes de checkpoints, TensorFS écrit séquentiellement, transformant les écritures aléatoires en écritures séquentielles.

### **5.3 Réseau : RDMA comme Primitive de Base**

Pour l'entraînement distribué sur grappe (cluster), la pile TCP/IP traditionnelle est trop lente et consommatrice de CPU. TensorOS intègre une pile réseau minimaliste basée sur **RDMA over Converged Ethernet (RoCEv2)**.48

* **Bypass du Noyau :** La carte réseau (NIC) accède directement à la mémoire du GPU (GPUDirect RDMA) pour transférer les gradients entre les nœuds.50  
* **Primitives Collectives :** Les opérations comme AllReduce (synchronisation des modèles) ne sont pas gérées par le logiciel, mais déchargées sur le matériel réseau (In-Network Computing). Neuro-Lang expose une primitive sync() qui déclenche ces transferts matériels.

## ---

**6\. L'Expérience Utilisateur : Le "Shell" Neuro**

L'interface de TensorOS est austère, fonctionnelle et entièrement textuelle. C'est un retour aux sources pour une efficacité maximale.

### **6.1 Le Neuro-Shell**

Au démarrage, l'utilisateur fait face à une invite de commande. Ce n'est pas un shell Bash, mais une instance interactive (REPL) du compilateur Neuro-Lang.51

**Exemple de Session :**

Bash

TensorOS v1.0  
TOS\> import models.llama3  
TOS\> let model\_path \= "nvme://checkpoints/llama-70b-v2"  
TOS\> let model \= models.llama3.load(model\_path, device=Device.ALL)  
 Mapping 140GB to Unified Memory... Done (0.4s).  
 GSP Firmware Loaded on 8 Devices.

TOS\> let input \= "Décris l'architecture de TensorOS."  
TOS\> let output \= model.generate(input, max\_tokens=256)  
\[Output\] TensorOS est un système d'exploitation bare-metal...

### **6.2 Outils de Débogage Bas Niveau**

L'absence d'OS protecteur rend le débogage critique. TensorOS inclut un "Moniteur" matériel (similaire aux moniteurs ROM des années 80).

* En cas de crash (ex: NaN explosion ou faute de segmentation), le système fige l'état du GPU.  
* L'utilisateur peut inspecter le contenu brut de la VRAM, les registres des Streaming Multiprocessors (SM), et les files d'attente de commandes via la console, offrant une visibilité que les pilotes fermés sous Linux cachent souvent.53

## ---

**7\. Analyse Comparative et Performance Théorique**

L'adoption de TensorOS et Neuro-Lang promet des gains significatifs par rapport à la pile standard Linux/PyTorch.

| Métrique | Linux \+ PyTorch \+ CUDA | TensorOS \+ Neuro-Lang | Gain Estimé | Justification |
| :---- | :---- | :---- | :---- | :---- |
| **Latence de lancement (Kernel Launch)** | 5-10 µs | \< 1 µs | \~10x | Suppression des syscalls et écriture directe MMIO 5 |
| **Bande passante Mémoire (Hôte-Périphérique)** | 20-25 GB/s (Buffered) | \~60 GB/s (PCIe Limit) | \~2-3x | Zéro-copie réelle, pas de tampons noyau 26 |
| **Gigue (Jitter) lors de l'entraînement** | Élevée (Interruptions OS) | Nulle (Déterministe) | N/A | Exécution exclusive en Ring 0, pas de préemption 1 |
| **Temps de démarrage (Boot-to-Inference)** | 30s \- 2min | \< 2s | 30x | Pas d'initialisation de services inutiles (systemd, réseau, gui) |
| **Empreinte Mémoire Système** | 2-4 GB (Noyau \+ Shell) | \< 100 MB | 20x | Pas de démons d'arrière-plan |

## ---

**8\. Feuille de Route d'Implémentation et Défis**

La réalisation de ce système, bien que théoriquement supérieure, fait face à des obstacles pratiques majeurs.

### **8.1 Défis Matériels**

Le principal obstacle est l'hétérogénéité du matériel. Linux supporte des millions de périphériques. TensorOS, pour rester léger, doit être sélectif. Il est conçu pour fonctionner sur des "Appliances IA" standardisées (ex: architecture de référence x86 \+ NVIDIA Ampere/Hopper).  
L'absence de documentation publique complète pour certains aspects des GPU (comme les registres de performance ou les détails fins du SASS) nécessitera un effort continu de rétro-ingénierie, aidé par les communautés open-source comme Nouveau et le projet TinyGrad.28

### **8.2 Adoption et Écosystème**

Le passage de Python à Neuro-Lang représente un coût cognitif. Pour faciliter l'adoption, Neuro-Lang devra proposer des outils de transpilation capables de convertir des modèles PyTorch (via torch.export ou ONNX) en graphes Neuro-Lang intermédiaires, permettant aux utilisateurs de bénéficier de la performance de TensorOS sans réécrire immédiatement tout leur code.12

## **9\. Conclusion**

La proposition de **TensorOS** et **Neuro-Lang** n'est pas un simple exercice académique, mais une réponse nécessaire à l'évolution des besoins computationnels de l'IA. En revenant aux principes fondamentaux de l'informatique – accès direct, simplicité, déterminisme – et en les appliquant aux architectures massivement parallèles modernes, nous pouvons briser les plafonds de verre imposés par des décennies d'abstraction logicielle.

Ce "DOS pour l'IA" représente l'avenir des infrastructures d'entraînement dédiées : des machines où le logiciel s'efface pour laisser le matériel exprimer son plein potentiel. C'est la fusion ultime entre le code et le silicium, un environnement où chaque cycle d'horloge et chaque octet de mémoire sont dévoués à l'intelligence.

---

**Note sur les Sources :** Les références entre crochets \`\` renvoient aux extraits de recherche analysés pour la construction de ce rapport, couvrant les goulots d'étranglement OS, les architectures GPU, les langages émergents et les techniques de programmation système bas niveau.

#### **Sources des citations**

1. On the Information Bottleneck Theory of Deep Learning \- OpenReview, consulté le décembre 30, 2025, [https://openreview.net/forum?id=ry\_WPG-A-](https://openreview.net/forum?id=ry_WPG-A-)  
2. The New Bottlenecks of ML Training: A Storage Perspective \- SIGARCH, consulté le décembre 30, 2025, [https://www.sigarch.org/the-new-bottlenecks-of-ml-training-a-storage-perspective/](https://www.sigarch.org/the-new-bottlenecks-of-ml-training-a-storage-perspective/)  
3. I/O Bottleneck Investigation in Deep Learning Systems, consulté le décembre 30, 2025, [https://oaciss.uoregon.edu/icpp18/publications/pos137s2-file1.pdf](https://oaciss.uoregon.edu/icpp18/publications/pos137s2-file1.pdf)  
4. Challenges and Opportunities for Unikernels in Machine Learning Inference \- IEEE Xplore, consulté le décembre 30, 2025, [https://ieeexplore.ieee.org/document/9596080/"\>](https://ieeexplore.ieee.org/document/9596080/"\>)  
5. 1\. Overview — GPUDirect RDMA 13.1 documentation, consulté le décembre 30, 2025, [https://docs.nvidia.com/cuda/gpudirect-rdma/](https://docs.nvidia.com/cuda/gpudirect-rdma/)  
6. Rust vs. Python: Finding the right balance between speed and simplicity, consulté le décembre 30, 2025, [https://blog.jetbrains.com/rust/2025/11/10/rust-vs-python-finding-the-right-balance-between-speed-and-simplicity/](https://blog.jetbrains.com/rust/2025/11/10/rust-vs-python-finding-the-right-balance-between-speed-and-simplicity/)  
7. Rust vs Go vs Python: Which language is the best strategic move | Xenoss Blog, consulté le décembre 30, 2025, [https://xenoss.io/blog/rust-vs-go-vs-python-comparison](https://xenoss.io/blog/rust-vs-go-vs-python-comparison)  
8. Rust vs Python \- Which language will win in AI race, consulté le décembre 30, 2025, [https://users.rust-lang.org/t/rust-vs-python-which-language-will-win-in-ai-race/124696](https://users.rust-lang.org/t/rust-vs-python-which-language-will-win-in-ai-race/124696)  
9. Building a Hybrid Python \- Mojo ML Pipeline: Can Mojo Replace Custom CUDA Kernels?, consulté le décembre 30, 2025, [https://hexshift.medium.com/building-a-hybrid-python-mojo-ml-pipeline-can-mojo-replace-custom-cuda-kernels-a5695fa88c73](https://hexshift.medium.com/building-a-hybrid-python-mojo-ml-pipeline-can-mojo-replace-custom-cuda-kernels-a5695fa88c73)  
10. Understanding the Triton Tutorials Part 1 | by Isamu Isozaki \- Medium, consulté le décembre 30, 2025, [https://isamu-website.medium.com/understanding-the-triton-tutorials-part-1-6191b59ba4c](https://isamu-website.medium.com/understanding-the-triton-tutorials-part-1-6191b59ba4c)  
11. Mojo : Powerful CPU+GPU Programming \- Modular, consulté le décembre 30, 2025, [https://www.modular.com/mojo](https://www.modular.com/mojo)  
12. An easy introduction to Mojo for Python programmers \- Modular, consulté le décembre 30, 2025, [https://www.modular.com/blog/an-easy-introduction-to-mojo-for-python-programmers](https://www.modular.com/blog/an-easy-introduction-to-mojo-for-python-programmers)  
13. Welcome to Triton's documentation\! — Triton documentation, consulté le décembre 30, 2025, [https://triton-lang.org/](https://triton-lang.org/)  
14. AI Operating Systems Explained: Types, Examples, and Use Cases, consulté le décembre 30, 2025, [https://picovoice.ai/blog/ai-operating-system/](https://picovoice.ai/blog/ai-operating-system/)  
15. Single Address Space Operating System \- C2 Wiki, consulté le décembre 30, 2025, [https://wiki.c2.com/?SingleAddressSpaceOperatingSystem](https://wiki.c2.com/?SingleAddressSpaceOperatingSystem)  
16. The exokernel operating system architecture \- DSpace@MIT, consulté le décembre 30, 2025, [https://dspace.mit.edu/handle/1721.1/16713](https://dspace.mit.edu/handle/1721.1/16713)  
17. Exokernel: An Operating System Architecture for Application-Level Resource Management \- Stanford University, consulté le décembre 30, 2025, [https://web.stanford.edu/class/archive/cs/cs240/cs240.1236/old/sp2014/readings/engler\_exo.pdf](https://web.stanford.edu/class/archive/cs/cs240/cs240.1236/old/sp2014/readings/engler_exo.pdf)  
18. Single address space operating system \- Wikipedia, consulté le décembre 30, 2025, [https://en.wikipedia.org/wiki/Single\_address\_space\_operating\_system](https://en.wikipedia.org/wiki/Single_address_space_operating_system)  
19. I put alot of time and effort into unikernels and the technology is very appeali... | Hacker News, consulté le décembre 30, 2025, [https://news.ycombinator.com/item?id=17260564](https://news.ycombinator.com/item?id=17260564)  
20. Building a 64 BIT UEFI Bootloader with EDK that runs on real hardware \- YouTube, consulté le décembre 30, 2025, [https://m.youtube.com/watch?v=q2IvhV3rDEE](https://m.youtube.com/watch?v=q2IvhV3rDEE)  
21. "Building an UEFI x64 kernel from scratch: A long trip to userspace" \- The Weekend Writeup, consulté le décembre 30, 2025, [https://blog.llandsmeer.com/tech/2019/07/21/uefi-x64-userland.html](https://blog.llandsmeer.com/tech/2019/07/21/uefi-x64-userland.html)  
22. PCI BARs and other means of accessing the GPU \- envytools git documentation, consulté le décembre 30, 2025, [https://envytools.readthedocs.io/en/latest/hw/bus/bars.html](https://envytools.readthedocs.io/en/latest/hw/bus/bars.html)  
23. 12\. Protocols — Console Support — UEFI Specification 2.9A documentation, consulté le décembre 30, 2025, [https://uefi.org/specs/UEFI/2.9\_A/12\_Protocols\_Console\_Support.html](https://uefi.org/specs/UEFI/2.9_A/12_Protocols_Console_Support.html)  
24. UEFI: SIMPLE\_TEXT\_OUTPUT vs GRAPHICS\_OUTPUT : r/osdev \- Reddit, consulté le décembre 30, 2025, [https://www.reddit.com/r/osdev/comments/1n505in/uefi\_simple\_text\_output\_vs\_graphics\_output/](https://www.reddit.com/r/osdev/comments/1n505in/uefi_simple_text_output_vs_graphics_output/)  
25. OS Experiment in Rust (part 3): Graphics and the Framebuffer | malware.re blog, consulté le décembre 30, 2025, [https://blog.malware.re/2023/11/12/rust-os-part3/index.html](https://blog.malware.re/2023/11/12/rust-os-part3/index.html)  
26. Introducing Low-Level GPU Virtual Memory Management | NVIDIA Technical Blog, consulté le décembre 30, 2025, [https://developer.nvidia.com/blog/introducing-low-level-gpu-virtual-memory-management/](https://developer.nvidia.com/blog/introducing-low-level-gpu-virtual-memory-management/)  
27. GPUDirect Storage Installation and Troubleshooting Guide \- NVIDIA Documentation, consulté le décembre 30, 2025, [https://docs.nvidia.com/gpudirect-storage/troubleshooting-guide/index.html](https://docs.nvidia.com/gpudirect-storage/troubleshooting-guide/index.html)  
28. Speed \- tinygrad docs, consulté le décembre 30, 2025, [https://docs.tinygrad.org/developer/speed/](https://docs.tinygrad.org/developer/speed/)  
29. Intro \- tinygrad docs, consulté le décembre 30, 2025, [https://docs.tinygrad.org/developer/developer/](https://docs.tinygrad.org/developer/developer/)  
30. 'linalg' Dialect \- MLIR \- LLVM, consulté le décembre 30, 2025, [https://mlir.llvm.org/docs/Dialects/Linalg/](https://mlir.llvm.org/docs/Dialects/Linalg/)  
31. Simplifying GPU Programming With Parametric Tile-Level Tensors in Mojo \- LLVM, consulté le décembre 30, 2025, [https://llvm.org/devmtg/2024-10/slides/techtalk/Taei-Simplifying-GPU-Programming-with-Parametric-Tile-Level-Tensors-In-Mojo.pdf](https://llvm.org/devmtg/2024-10/slides/techtalk/Taei-Simplifying-GPU-Programming-with-Parametric-Tile-Level-Tensors-In-Mojo.pdf)  
32. The MLIR Transform Dialect: Your Compiler Is More Powerful Than You Think \- Michel Steuwer, consulté le décembre 30, 2025, [https://www.steuwer.info/files/publications/2025/CGO-The-MLIR-Transform-Dialect.pdf](https://www.steuwer.info/files/publications/2025/CGO-The-MLIR-Transform-Dialect.pdf)  
33. My First Language Frontend with LLVM Tutorial, consulté le décembre 30, 2025, [https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html](https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html)  
34. Triton Kernel Compilation Stages \- PyTorch, consulté le décembre 30, 2025, [https://pytorch.org/blog/triton-kernel-compilation-stages/](https://pytorch.org/blog/triton-kernel-compilation-stages/)  
35. Enzyme-MLIR: Early Experiments on multi-level automatic differentiation, consulté le décembre 30, 2025, [https://c.wsmoses.com/presentations/enzyme-mlir.pdf](https://c.wsmoses.com/presentations/enzyme-mlir.pdf)  
36. Starting my small machine-learning framework with MLIR linalg, Enzyme, etc \- Beginners, consulté le décembre 30, 2025, [https://discourse.llvm.org/t/starting-my-small-machine-learning-framework-with-mlir-linalg-enzyme-etc/84241](https://discourse.llvm.org/t/starting-my-small-machine-learning-framework-with-mlir-linalg-enzyme-etc/84241)  
37. Introducing Triton: Open-source GPU programming for neural networks \- OpenAI, consulté le décembre 30, 2025, [https://openai.com/index/triton/](https://openai.com/index/triton/)  
38. Reversing Nvidia GPU's SASS code \- Medium, consulté le décembre 30, 2025, [https://medium.com/@pnfsoftware/reversing-nvidia-gpus-sass-code-d4001265c296](https://medium.com/@pnfsoftware/reversing-nvidia-gpus-sass-code-d4001265c296)  
39. Mastering Mojo Ownership and Borrowing for Python Developers | by Hex Shift | Nov, 2025, consulté le décembre 30, 2025, [https://hexshift.medium.com/mastering-mojo-ownership-and-borrowing-for-python-developers-65cd13f6d129](https://hexshift.medium.com/mastering-mojo-ownership-and-borrowing-for-python-developers-65cd13f6d129)  
40. Ownership \- Mojo \- Modular Docs, consulté le décembre 30, 2025, [https://docs.modular.com/mojo/manual/values/ownership/](https://docs.modular.com/mojo/manual/values/ownership/)  
41. Mojo : a deep dive on ownership with Chris Lattner \- YouTube, consulté le décembre 30, 2025, [https://www.youtube.com/watch?v=9ag0fPMmYPQ](https://www.youtube.com/watch?v=9ag0fPMmYPQ)  
42. A Deep Dive into Building a Memory Allocator | by Sriman | Oct, 2025 \- Medium, consulté le décembre 30, 2025, [https://medium.com/@kondam.reddy/a-deep-dive-into-building-a-memory-allocator-dd5333a98195](https://medium.com/@kondam.reddy/a-deep-dive-into-building-a-memory-allocator-dd5333a98195)  
43. A Simple Device Memory Allocator For Vulkan \- Kyle Halladay, consulté le décembre 30, 2025, [https://kylehalladay.com/blog/tutorial/2017/12/13/Custom-Allocators-Vulkan.html](https://kylehalladay.com/blog/tutorial/2017/12/13/Custom-Allocators-Vulkan.html)  
44. NVIDIA Linux open GPU kernel module source \- GitHub, consulté le décembre 30, 2025, [https://github.com/NVIDIA/open-gpu-kernel-modules](https://github.com/NVIDIA/open-gpu-kernel-modules)  
45. NVIDIA Releases Open-Source GPU Kernel Modules | NVIDIA Technical Blog : r/linux, consulté le décembre 30, 2025, [https://www.reddit.com/r/linux/comments/unik4t/nvidia\_releases\_opensource\_gpu\_kernel\_modules/](https://www.reddit.com/r/linux/comments/unik4t/nvidia_releases_opensource_gpu_kernel_modules/)  
46. Writing a Rust GPU kernel driver: a brief introduction on how GPU drivers work \- Collabora, consulté le décembre 30, 2025, [https://www.collabora.com/news-and-blog/blog/2025/08/06/writing-a-rust-gpu-kernel-driver-a-brief-introduction-on-how-gpu-drivers-work/](https://www.collabora.com/news-and-blog/blog/2025/08/06/writing-a-rust-gpu-kernel-driver-a-brief-introduction-on-how-gpu-drivers-work/)  
47. The AI-Native OS: Rethinking the Operating System from First Principles | by Yashash Gc, consulté le décembre 30, 2025, [https://medium.com/@yashash.gc/the-ai-native-os-rethinking-the-operating-system-from-first-principles-a2b5c02332a6](https://medium.com/@yashash.gc/the-ai-native-os-rethinking-the-operating-system-from-first-principles-a2b5c02332a6)  
48. RDMA Explained: The Backbone of High-Performance Computing | DigitalOcean, consulté le décembre 30, 2025, [https://www.digitalocean.com/community/conceptual-articles/rdma-high-performance-networking](https://www.digitalocean.com/community/conceptual-articles/rdma-high-performance-networking)  
49. Deploy a Bare Metal GPU Cluster for AI Workloads in a Dedicated Cloud, consulté le décembre 30, 2025, [https://docs.oracle.com/en/solutions/deploy-bare-metal-gpu-cluster-for-ai/index.html](https://docs.oracle.com/en/solutions/deploy-bare-metal-gpu-cluster-for-ai/index.html)  
50. Streamlining Kubernetes Networking in Scale-out GPU Clusters with the new NVIDIA Network Operator 1.0 | NVIDIA Technical Blog, consulté le décembre 30, 2025, [https://developer.nvidia.com/blog/streamlining-kubernetes-networking-in-scale-out-gpu-clusters-with-the-new-nvidia-network-operator-1-0/](https://developer.nvidia.com/blog/streamlining-kubernetes-networking-in-scale-out-gpu-clusters-with-the-new-nvidia-network-operator-1-0/)  
51. Tutorial \- Write a Shell in C \- Stephen Brennan, consulté le décembre 30, 2025, [https://brennan.io/2015/01/16/write-a-shell-in-c/](https://brennan.io/2015/01/16/write-a-shell-in-c/)  
52. Let's Build a (Mini)Shell in Rust \- Micah Kepe, consulté le décembre 30, 2025, [https://micahkepe.com/blog/minishell/](https://micahkepe.com/blog/minishell/)  
53. Karol Herbst: Nouveau \- reverse engineering Nvidia GPUs \- YouTube, consulté le décembre 30, 2025, [https://www.youtube.com/watch?v=-7SdKBUrKJ0](https://www.youtube.com/watch?v=-7SdKBUrKJ0)  
54. NVIDIA Nsight Systems, consulté le décembre 30, 2025, [https://developer.nvidia.com/nsight-systems](https://developer.nvidia.com/nsight-systems)  
55. Runtime \- tinygrad docs, consulté le décembre 30, 2025, [https://docs.tinygrad.org/runtime/](https://docs.tinygrad.org/runtime/)