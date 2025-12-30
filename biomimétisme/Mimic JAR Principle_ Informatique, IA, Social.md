# **Le Protocole Eigenmannia : Architectures Bio-Inspirées de la Réponse d'Évitement de Brouillage (JAR) pour les Systèmes Informatiques et la Dynamique Sociale**

## **1\. Introduction et Cadre Théorique : De la Neuroéthologie à l'Algorithmique Sociale**

L'intersection de la neuroéthologie computationnelle et de la théorie des systèmes complexes offre aujourd'hui des perspectives inédites pour résoudre des défaillances systémiques modernes, allant de la saturation du spectre électromagnétique à la polarisation politique extrême. Ce rapport de recherche exhaustif se consacre à l'analyse approfondie de la **Réponse d'Évitement de Brouillage** (Jamming Avoidance Response \- JAR), un algorithme neuro-comportemental évolué observé chez les poissons électriques faiblement déchargeants, spécifiquement l'espèce *Eigenmannia virescens*. Notre objectif est de déconstruire ce mécanisme biologique pour en extraire une architecture computationnelle applicable à l'informatique distribuée, à la cybersécurité et, de manière cruciale, à la régulation des chambres d'écho dans les réseaux sociaux.

La prémisse centrale de cette étude postule que les algorithmes neuronaux, affinés par des millions d'années d'évolution pour maintenir une acuité sensorielle dans des environnements aquatiques électriquement bruyants, fournissent un modèle mathématique robuste pour la gestion des interférences. Ce modèle, basé sur le calcul différentiel phase-amplitude au sein du *torus semicircularis* du poisson, peut être mimé pour atténuer le "tassement spectral" dans les réseaux sans fil, prévenir l'"effondrement de mode" dans l'intelligence artificielle générative, et dissiper la "résonance" destructrice de la polarisation politique.1

Nous soutenons que la polarisation politique est fonctionnellement isomorphe au "brouillage" dans les réseaux électrosensoriels : une perte de capacité d'information due à l'interférence constructive de signaux homogènes. En implémentant un "JAR Social", la gouvernance algorithmique peut déplacer la "fréquence" du discours pour préserver l'"électrolocalisation" cognitive de la citoyenneté, permettant ainsi la réémergence de la nuance et du consensus.3

### **1.1 La Crise de l'Interférence : Une Pathologie Universelle**

Dans tout système de communication, qu'il soit biologique, électronique ou social, la capacité à distinguer le signal du bruit est fondamentale. Cependant, lorsque plusieurs émetteurs occupent la même bande passante, le phénomène de brouillage survient.

* **Dans le domaine spectral (RF) :** La prolifération des appareils IoT et la densité des réseaux 5G créent un environnement où les collisions de paquets et les interférences co-canal dégradent la qualité de service (QoS).5  
* **Dans le domaine cybernétique :** Les attaques par déni de service (DDoS) ou la reconnaissance de réseau par balayage d'IP exploitent la staticité des cibles pour saturer ou localiser une victime, un processus analogue au brouillage intentionnel d'un prédateur.7  
* **Dans le domaine social :** Les algorithmes de recommandation actuels, optimisés pour l'engagement, tendent à regrouper les utilisateurs ayant des opinions similaires. Cela crée des "bulles de filtres" où la diversité sémantique s'effondre. L'utilisateur, bombardé de signaux identiques au sien (homophilie), perd sa capacité à percevoir la réalité complexe, tout comme un poisson électrique brouillé devient aveugle aux obstacles physiques.9

L'universalité de ce problème suggère qu'une solution universelle pourrait exister. La nature, confrontée à ce défi chez les Gymnotiformes sud-américains, a développé non pas un blindage passif, mais une réponse dynamique active : le JAR.

### **1.2 L'Approche Bio-Mimétique**

Le biomimétisme en informatique ne se limite pas à copier la forme, mais à abstraire la logique computationnelle. *Eigenmannia virescens* est un modèle idéal car son circuit neuronal est l'un des mieux cartographiés de la neurobiologie.1 Contrairement aux réseaux de neurones profonds (Deep Learning) qui sont souvent des "boîtes noires", le circuit du JAR est une "démocratie neuronale" explicite, réalisant des opérations mathématiques précises (transformées de Hilbert, comparaisons de phase, intégrations vectorielles) que nous pouvons transcrire en code informatique.11

Ce rapport structurera cette transcription en trois phases : l'analyse du matériel biologique (le "hardware" du poisson), la transposition aux systèmes techniques (Radio Cognitive et Cybersécurité), et enfin, l'application théorique aux dynamiques d'opinion (le "Software" social).

## ---

**2\. Neuroéthologie Computationnelle de *Eigenmannia virescens***

Pour mimer le JAR avec succès, il est impératif de comprendre la physique et le traitement du signal qui sous-tendent ce réflexe. Ce n'est pas une simple fuite, mais un calcul vectoriel complexe réalisé en temps réel.

### **2.1 Physique de l'Électrolocalisation et du Brouillage**

*Eigenmannia virescens* (le poisson-couteau de verre) génère un champ électrique continu quasi-sinusoïdal, appelé Décharge de l'Organe Électrique (EOD), utilisé pour explorer son environnement. La fréquence fondamentale ($F\_1$) est très stable pour un individu donné, variant généralement entre 300 et 500 Hz selon le sexe et la maturité.1 Le poisson détecte les distorsions de ce champ causées par des objets conducteurs ou résistifs via des électrorécepteurs cutanés.

#### **Le Problème du Battement (The Beat Phenomenon)**

Lorsque deux poissons, Poisson A ($F\_A$) et Poisson B ($F\_B$), se trouvent à proximité, leurs champs électriques se mélangent vectoriellement. Si leurs fréquences sont proches (par exemple, $|F\_A \- F\_B| \< 20$ Hz), les signaux interfèrent pour créer un motif de battement.  
Ce signal mixte $S(t)$ perçu par le poisson A peut être modélisé comme :

$$S(t) \= A\_{soi} \\cos(2\\pi F\_A t) \+ A\_{voisin} \\cos(2\\pi F\_B t)$$

L'interférence résulte en une modulation d'amplitude (AM) et une modulation de phase (PM) du signal porteur du poisson A à la fréquence de différence $dF \= F\_B \- F\_A$.  
Ce battement est délétère car il masque les modulations plus subtiles causées par des objets passifs (proies, obstacles), rendant le poisson "aveugle". C'est le phénomène de brouillage électrosensoriel.14

#### **La Réponse Comportementale**

Le JAR est un réflexe par lequel le poisson décale sa fréquence EOD pour augmenter la différence ($dF$) avec le brouilleur :

* Si $F\_{voisin} \< F\_{soi}$ ($dF$ négatif), le poisson **augmente** sa fréquence ($F\_{soi} \\uparrow$).  
* Si $F\_{voisin} \> F\_{soi}$ ($dF$ positif), le poisson diminue sa fréquence ($F\_{soi} \\downarrow$).  
  Ce comportement maximise $|dF|$, repoussant la fréquence de battement hors de la bande passante sensible de l'électrolocalisation, restaurant ainsi l'acuité sensorielle.1

### **2.2 L'Algorithme Computationnel : Le Plan d'État (State Plane)**

Le défi majeur pour le système nerveux du poisson est de déterminer le signe de $dF$. Le poisson n'a pas accès à une horloge de référence interne absolue ni à la fréquence "pure" du voisin ; il ne perçoit que le signal mélangé sur sa peau. Comment savoir s'il faut monter ou descendre en fréquence?  
La solution évolutive est une analyse conjointe spatio-temporelle, visualisable géométriquement dans un Plan d'État.17  
L'algorithme nécessite de comparer le signal en deux points distincts du corps :

1. **Point A (Référence interne virtuelle) :** Une région où la géométrie du champ électrique rend le signal du brouilleur faible par rapport à l'EOD du poisson (généralement la tête ou le tronc).  
2. **Point B (Contaminé) :** Une région où le signal du brouilleur est fort.

Le mélange des deux signaux crée une modulation de l'Amplitude instantanée ($|S|$) et de la Phase différentielle ($H$). En traçant l'amplitude instantanée contre la phase différentielle (Phase au point A \- Phase au point B), le système nerveux construit une figure de Lissajous.19

* **Rotation Horaire du vecteur dans le plan d'état :** Indique que le voisin a une fréquence inférieure ($dF \< 0$).  
  * *Commande motrice :* Augmenter la fréquence du Pacemaker.  
* **Rotation Anti-Horaire :** Indique que le voisin a une fréquence supérieure ($dF \> 0$).  
  * *Commande motrice :* Diminuer la fréquence du Pacemaker.

Cette computation géométrique permet de résoudre le problème du signe de $\\Delta F$ sans référence temporelle absolue, uniquement par comparaison spatiale différentielle.11 C'est une forme primitive mais robuste de calcul vectoriel distribué.

### **2.3 Architecture du Circuit Neuronal**

Pour reproduire ce système en informatique, nous devons modéliser l'architecture de traitement parallèle du cerveau d'*Eigenmannia*. Le traitement se fait en plusieurs couches successives, passant de la sensation brute à l'abstraction géométrique, puis à la commande motrice.1

#### **Tableau 1 : Correspondance Fonctionnelle Bio-Informatique**

| Composant Biologique | Fonction Neurophysiologique | Équivalent Informatique / Algorithmique |
| :---- | :---- | :---- |
| **Récepteurs P (P-units)** | Codent l'Amplitude instantanée ($ | S |
| **Récepteurs T (T-units)** | Codent la Phase instantanée ($H$). Déclenchent un potentiel d'action à chaque passage par zéro du signal. | Boucles à Verrouillage de Phase (PLL), Détecteurs de Zéro-Crossing, Analyseurs Sémantiques Vectoriels (Orientation). |
| **Lobe de la Ligne Latérale Électrosensorielle (ELL)** | Premier relais. Ségrégation des voies de phase et d'amplitude. Cellules sphériques (T) et pyramidales (P). | Couche de Prétraitement, Normalisation des Données, Extraction de Caractéristiques (Feature Extraction). |
| **Torus Semicircularis (TS) \- Lamina 6** | Le cœur du calcul. Les neurones "Petites Cellules" comparent les temps d'arrivée (phase) entre différentes parties du corps. | Amplificateurs Différentiels, Portes XOR, Corrélateurs de Phase, Calcul de la Similarité Cosinus. |
| **Neurones Sélectifs de Signe (Sign-Selective Cells)** | Intègrent Amplitude et Phase différentielle. S'activent uniquement pour une rotation spécifique (horaire ou anti-horaire) dans le plan d'état. | Classifieurs Logiques, Arbres de Décision, Perceptrons Multicouches (MLP). |
| **Noyau Pré-pacemaker (PPn)** | Intègre les votes des cellules sélectives de signe et module le noyau pacemaker via des synapses GABAergiques (ralentissement) ou glutamatergiques (accélération). | Contrôleur Logique, Algorithme de Gouvernance, SDN Controller (Software Defined Network). |
| **Noyau Pacemaker** | Oscillateur central qui détermine la fréquence de l'EOD. | Oscillateur Contrôlé en Tension (VCO), Horloge Système, Générateur de Contenu. |

#### **Convergence Évolutive et Robustesse**

Il est fascinant de noter que l'espèce africaine *Gymnarchus niloticus* a évolué un JAR et un algorithme computationnel identiques de manière totalement indépendante (convergence évolutive), bien que l'implémentation neuronale diffère légèrement.1 Cela suggère que l'algorithme du plan d'état (State Plane Analysis) est une solution optimale fondamentale, voire une "vérité mathématique" biologique pour le problème de l'interférence ondulatoire.

Cette robustesse justifie notre démarche : si deux lignées évolutives distinctes ont convergé vers cet algorithme pour résoudre le brouillage, il est fort probable qu'il soit également optimal pour nos systèmes artificiels.

## ---

**3\. Application I : Réseaux Sans Fil et Radio Cognitive**

L'application la plus directe et la plus techniquement fidèle du principe JAR réside dans la gestion du spectre électromagnétique. Face à la "crise du spectre" (Spectrum Crunch), les appareils modernes se comportent comme des poissons aveuglés dans un aquarium surpeuplé.

### **3.1 Architectures Photoniques de JAR**

Des recherches pionnières menées à l'Université de Géorgie ont réussi à modéliser le circuit JAR en utilisant la photonique pour gérer les interférences dans les réseaux sans fil à large bande.2

Dans ce système biomimétique :

1. **Détection (Sensing) :** Le système utilise des composants photoniques équivalents aux unités P et T pour détecter le "battement" entre la fréquence porteuse de l'appareil et celle d'un interférent. La lumière est utilisée pour traiter les signaux RF en raison de sa vitesse et de sa large bande passante.  
2. **Traitement (Processing) :** Un réseau neuronal photonique artificiel calcule la rotation dans le plan d'état (espace phase-amplitude). Il ne nécessite pas de démodulation complète du signal adverse (ce qui serait coûteux en calcul), mais analyse simplement l'enveloppe et la phase relative.  
3. **Actuation (Actuation) :** Le système décale automatiquement la fréquence de transmission de l'émetteur pour s'éloigner de l'interférence.

**Avantage Critique :** Contrairement aux protocoles traditionnels de type "Listen-Before-Talk" (LBT), comme le CSMA/CA du Wi-Fi, qui cessent de transmettre lorsqu'une interférence est détectée (entraînant une latence), une radio basée sur le JAR maintient un débit continu en glissant sa fréquence en temps réel de manière fluide ("Soft Handover spectral").22

### **3.2 Apprentissage par Renforcement (RL) pour l'Anti-Brouillage**

Au-delà de l'implémentation photonique "câblée", les radios cognitives avancées (Cognitive Radio \- CR) utilisent l'**Apprentissage par Renforcement (Reinforcement Learning \- RL)** pour redécouvrir et optimiser la politique du JAR.5

Dans ce contexte, la radio agit comme un agent autonome :

* **État ($S$) :** L'occupation spectrale actuelle, le niveau de bruit et la présence de motifs d'interférence (analogue au motif de battement).  
* **Action ($A$) :** Changer de canal, ajuster la puissance de transmission, ou sauter en fréquence (analogue au décalage de l'EOD).  
* **Récompense ($R$) :** Maximisation du rapport Signal-sur-Interférence-plus-Bruit (SINR) et du débit de données.24

Les réseaux Q profonds (Deep Q-Networks \- DQN) ont été déployés avec succès pour contrer des "brouilleurs intelligents" (Smart Jammers). Là où un brouilleur classique émet du bruit blanc, un brouilleur intelligent tente de prédire la fréquence de la victime. L'agent RL apprend alors, par essais et erreurs, une stratégie dynamique de JAR qui est mathématiquement similaire à celle du poisson : détecter les précurseurs subtils d'un brouillage imminent (le "battement" avant la saturation) et exécuter une manœuvre d'évasion spectrale.26

#### **Tableau 2 : Analyse Comparative des Stratégies Anti-Brouillage**

| Caractéristique | Saut de Fréquence Traditionnel (FHSS) | JAR Bio-Inspiré (Eigenmannia) | Radio Cognitive basée sur RL |
| :---- | :---- | :---- | :---- |
| **Déclencheur** | Séquence pré-programmée (aveugle) | Détection de battement en temps réel (réactif) | Maximisation de la récompense apprise (proactif/adaptatif) |
| **Réponse** | Saut aléatoire ou pseudo-aléatoire | Décalage directionnel (s'éloigner du brouilleur) | Sélection de la politique optimale (peut inclure le silence ou le leurre) |
| **Efficacité Spectrale** | Faible (risque de sauter sur une autre interférence) | Haute (maximise toujours $dF$) | Très Haute (s'adapte à la stratégie du brouilleur) |
| **Coordination** | Requiert des clés synchronisées (vulnérable) | Décentralisée / Autonome | Décentralisée |

### **3.3 Accès Dynamique au Spectre (DSA) sans Coordination**

Une application majeure réside dans l'Accès Dynamique au Spectre (DSA).6 Dans un réseau décentralisé d'objets connectés (IoT), la coordination centrale est coûteuse. En dotant chaque nœud IoT d'un algorithme JAR local, le réseau s'auto-organise. Si deux nœuds choisissent le même canal, le mécanisme de répulsion spectrale (inspiré du JAR) les force à se séparer naturellement sur le spectre, optimisant l'utilisation de la bande passante globale sans surcharge de signalisation (overhead).29

## ---

**4\. Application II : Cybersécurité et Défense de Cible Mouvante (MTD)**

Dans le cyberespace, le concept de "brouillage" peut être étendu à toute action hostile visant à localiser ou saturer une ressource. L'attaque par Déni de Service (DoS) ou la phase de reconnaissance (scanning) où un attaquant "verrouille" une adresse IP statique sont fonctionnellement analogues au brouillage électrosensoriel. Le principe JAR est ici le précurseur biologique de la **Défense de Cible Mouvante (Moving Target Defense \- MTD)**.7

### **4.1 Le "Shuffling" d'IP comme Décalage de Fréquence**

Les configurations réseau statiques sont vulnérables car elles offrent aux attaquants un temps infini pour "électrolocaliser" la cible (scanner les vulnérabilités, mapper la topologie). Les stratégies MTD visent à randomiser les paramètres du système (adresses IP, numéros de port, disposition de la mémoire) pour augmenter l'incertitude et le coût pour l'attaquant.32

L'Algorithme Bio-Mimétique (Network Address Shuffling \- NASR) :  
Le principe JAR implique que le "décalage" ne doit pas être uniquement aléatoire, mais sensible et réactif. Une défense purement aléatoire est comme un poisson qui change de fréquence sans raison : coûteux en énergie. Le JAR est déclenché par la détection d'une menace.

1. **Détection (L'unité P) :** Les Systèmes de Détection d'Intrusion (IDS) surveillent le trafic. Un "ping" ICMP ou un balayage de port (SYN Scan) est perçu comme le "battement" d'un prédateur en approche.  
2. **Traitement (Le TS) :** Le Contrôleur SDN (Software Defined Network) analyse la persistance et la direction du scan. Il détermine la trajectoire de l'attaque.  
3. **Réponse (Le Pacemaker) :** Le contrôleur déclenche une mutation proactive de l'adresse IP virtuelle de l'hôte victime. C'est l'équivalent cybernétique du changement de fréquence EOD. L'attaquant, qui visait l'IP $X$, frappe dans le vide, car la cible est maintenant à l'IP $Y$.34

**Pseudo-Code pour une Mutation d'IP basée sur le JAR :**

Python

\# Implémentation conceptuelle d'une MTD inspirée du JAR  
class SDN\_Controller\_JAR:  
    def \_\_init\_\_(self, pool\_ip):  
        self.mapping\_reel\_virtuel \= {} \# Carte IP Réelle \-\> IP Virtuelle  
        self.taux\_mutation\_base \= 10 \# Fréquence de base (secondes)  
        self.seuil\_sensibilite \= 5 \# Seuil de détection de scan

    def detecter\_battement\_scan(self, flux\_trafic):  
        \# Mimétisme des unités P/T : Analyse de la rythmicité des paquets  
        \# Un scan séquentiel crée un "motif" temporel distinct  
        nombre\_syn \= self.analyser\_flags(flux\_trafic, 'SYN')  
        if nombre\_syn \> self.seuil\_sensibilite:  
            return True, "Scan\_Haute\_Frequence"  
        return False, None

    def reponse\_jar\_evitement(self, id\_hote, type\_menace):  
        \# Le Réflexe JAR : Décaler la "fréquence" (IP) loin de l'attaquant  
        ip\_virtuelle\_actuelle \= self.mapping\_reel\_virtuel\[id\_hote\]  
          
        \# Générer une IP orthogonale (dans un sous-réseau différent si possible)  
        nouvelle\_ip\_virtuelle \= self.generer\_ip\_orthogonale(ip\_virtuelle\_actuelle)  
          
        \# Mise à jour des tables de flux (Action du Pacemaker)  
        self.update\_flow\_table\_switch(id\_hote, nouvelle\_ip\_virtuelle)  
          
        \# Augmentation de l'état d'alerte (Taux de mutation accéléré)  
        self.taux\_mutation\_base /= 2   
        print(f" Hôte {id\_hote} décalé vers {nouvelle\_ip\_virtuelle}. Menace esquivée.")

Les résultats empiriques montrent que de telles stratégies, lorsqu'elles sont bien implémentées, peuvent réduire la connaissance de l'adversaire sur le réseau de près de 97%, rendant les attaques ciblées quasi impossibles.36

### **4.2 Les GANs et l'Effondrement de Mode (Digital Jamming)**

Une application sophistiquée et purement algorithmique du JAR concerne les **Réseaux Antagonistes Génératifs (GANs)**. Un problème majeur des GANs est l'**Effondrement de Mode (Mode Collapse)** : le Générateur, trouvant une image qui trompe le Discriminateur, se met à produire uniquement cette image (ou de très légères variantes). Il se "bloque" sur une fréquence unique. C'est un cas d'auto-brouillage où la diversité du système tombe à zéro.37

La Solution JAR : La Répulsion.  
Pour contrer cela, les chercheurs introduisent une "Force de Répulsion" entre les échantillons générés, analogue au JAR.  
L'utilisation de Processus Ponctuels Déterminantaux (Determinantal Point Processes \- DPP) permet de modéliser mathématiquement cette répulsion. Un noyau DPP définit une distribution de probabilité où l'inclusion d'un élément réduit la probabilité d'inclure des éléments similaires.39

* **Bio-Analogie :** Si l'échantillon A généré est à la fréquence $X$, l'échantillon B *doit* se décaler vers la fréquence $Y$. S'ils sont trop proches, l'"énergie" du système augmente (comme l'amplitude du battement chez le poisson), forçant le modèle à diverger lors de la descente de gradient.  
* **Implémentation :** Ajout d'une "Pénalité de Diversité" à la fonction de perte (Loss Function) du GAN, qui mime explicitement l'évitement des faibles $dF$ du JAR.41

## ---

**5\. Application III : Dynamique Sociale et Polarisation (Le "Social JAR")**

Cette section constitue le cœur de notre proposition innovante : l'application de l'algorithme JAR d'*Eigenmannia* au domaine de la dynamique de l'information pour contrer les chambres d'écho et la polarisation politique. Ici, nous répondons spécifiquement à la demande de "mimer le principe" pour apaiser les tensions sociales.

### **5.1 L'Isomorphisme du Brouillage et de la Polarisation**

Pour appliquer le JAR à la société, nous devons établir une correspondance rigoureuse entre les variables physiques et sociales.  
Chez le poisson électrique, la survie dépend de la Sensibilité de Phase (la capacité à distinguer des différences temporelles infimes). Dans les systèmes sociaux, la "santé" démocratique dépend de la Sensibilité à la Nuance.

* **Brouillage (Biologie) :** Deux signaux sont si proches ($dF \\approx 0$) qu'ils créent un battement basse fréquence, masquant la réalité physique.  
* **Chambre d'Écho (Sociologie) :** Les utilisateurs sont exposés à des signaux si identiques à leurs propres a priori (Homophilie) que les "battements informationnels" (le désaccord, la nouveauté, la surprise) sont éliminés. L'utilisateur devient "aveugle" à l'environnement social global.3

**Le Paradoxe de la Polarisation :** La polarisation est souvent perçue comme deux groupes étant "trop éloignés". Cependant, du point de vue de la théorie du signal, c'est le résultat d'une **Hyper-Synchronisation** interne. Le Groupe A est "brouillé" sur la Fréquence Haute ; le Groupe B est "brouillé" sur la Fréquence Basse. Il n'y a pas de mélange, pas de "battements", et donc aucune capacité d'échange d'information ou d'évolution d'opinion.4

### **5.2 L'Algorithme "Social JAR"**

Pour mimer *Eigenmannia*, un Système de Recommandation (Recommender System \- RS) doit cesser de maximiser l'"engagement" (qui mène souvent à l'homophilie et donc au brouillage) et commencer à maximiser la **"Distinctivité du Signal"** via un mécanisme JAR.

#### **5.2.1 Définition du Plan d'État Social (Social State Plane)**

Nous devons construire un Plan d'État computationnel pour le contenu social afin de permettre à l'algorithme de détecter le "Brouillage" (Chambres d'Écho).

* **Amplitude ($A$) :** L'intensité émotionnelle ou la "viralité" d'un post (Nombre de Likes, Partages, Magnitude du Sentiment, présence de majuscules/points d'exclamation). Une amplitude trop élevée sature le récepteur (l'utilisateur).19  
* **Phase ($\\Phi$) :** Le positionnement temporel ou sémantique du contenu par rapport à l'état de croyance actuel de l'utilisateur.  
  * *En Phase ($\\Phi \\approx 0$) :* Contenu qui s'aligne parfaitement avec le narratif de l'utilisateur (Biais de confirmation). C'est le signal de brouillage par excellence.  
  * *Anti-Phase ($\\Phi \\approx \\pi$) :* Contenu diamétralement opposé (Hostilité hors-groupe).  
  * *Phase Orthogonale ($\\Phi \\approx \\pi/2$) :* Contenu pertinent mais qui cadre le problème sous un angle différent, non hostile (Le "Pont" ou "Bridge").

Objectif de l'Algorithme :  
Les algorithmes actuels (Youtube, Facebook) tendent à minimiser $dF$ (donner à l'utilisateur ce qu'il aime). Cela conduit au brouillage.  
L'algorithme Social JAR détecte lorsque le flux de l'utilisateur a une variance sémantique trop faible (Brouillage). Il injecte alors délibérément du contenu qui induit un Décalage de Phase.

#### **5.2.2 Modèle Mathématique : Dynamique de Kuramoto Répulsive**

Nous modélisons les opinions des utilisateurs comme des oscillateurs dans un modèle de Kuramoto. Les modèles sociaux standards supposent un couplage *attractif* (les utilisateurs deviennent plus semblables à leurs voisins).45 Un modèle basé sur le JAR introduit un **Couplage Répulsif** pour prévenir l'effondrement (synchronisation totale).47

L'équation gouvernant l'opinion $\\theta\_i$ de l'utilisateur $i$ devient :

$$\\frac{d\\theta\_i}{dt} \= \\omega\_i \+ \\frac{K\_{attract}}{N} \\sum\_{j \\in Voisinage} \\sin(\\theta\_j \- \\theta\_i) \+ \\underbrace{R\_{JAR}(\\theta\_i, \\theta\_{cluster})}\_{\\text{Terme d'Évitement de Brouillage}}$$  
Où $R\_{JAR}$ est la fonction d'évitement dérivée d'Eigenmannia :

$$R\_{JAR} \= \\begin{cases} \\alpha \\cdot \\text{sgn}(\\Delta \\Phi\_{sociale}) & \\text{si } |\\theta\_{cluster} \- \\theta\_i| \< \\epsilon \\text{ (Trop proche/Chambre d'Écho)} \\\\ 0 & \\text{sinon} \\end{cases}$$  
Si la "distance sémantique" (différence d'opinion) descend sous un seuil $\\epsilon$, l'algorithme exerce une force $\\alpha$ pour pousser l'utilisateur *hors* du cluster, non pas pour le polariser vers l'extrême inverse, mais pour le déplacer vers une position orthogonale (nuancée).

### **5.3 Implémentation : L'Injection d'Information Orthogonale et "Bridging"**

Comment le système "pousse-t-il" un utilisateur hors d'une chambre d'écho sans provoquer de "Réactance Psychologique" (le rejet violent d'une opinion adverse) ou un désengagement?.49

* **Insight Biologique :** *Eigenmannia* ne s'éteint pas ; il décale sa fréquence légèrement.  
* **Implémentation Sociale :** Le système de recommandation injecte du **Contenu Orthogonal**.50

Si un utilisateur est enfermé dans une chambre d'écho "Anti-Immigration" (Fréquence A), lui montrer du contenu "Pro-Immigration" (Fréquence B) provoque un "battement" violent (dissonance cognitive/colère) — c'est le rejet de l'Anti-Phase.  
Au lieu de cela, le Social JAR injecte du contenu orthogonal :

* *Exemple :* À un utilisateur obsédé par l'aspect culturel de l'immigration, on propose un contenu sur les "Impacts économiques des pénuries de main-d'œuvre" (Sujet $A'$). C'est sémantiquement lié, mais cela "décale la phase" du discours du purement identitaire vers l'économique, forçant l'utilisateur à traiter de nouvelles dimensions sans déclencher ses défenses identitaires.

#### **Études de Cas : *vTaiwan* et *Pol.is***

La plateforme Pol.is, utilisée dans l'expérience démocratique vTaiwan, implémente efficacement un "Social JAR" primitif. Elle visualise le "Plan d'État" des opinions. Au lieu de trier les commentaires par "les plus likés" (dominance d'Amplitude, favorisant la polarisation), elle identifie les "clusters de consensus" et met en avant les opinions minoritaires qui ont un attrait transversal (Phase bridging).52  
Cela empêche le "brouillage" de la majorité d'étouffer la minorité, préservant le signal de la population entière. L'algorithme de Pol.is favorise mathématiquement les commentaires qui obtiennent des votes positifs de la part de groupes opposés (Groupe A et Groupe B), agissant comme des "Sign-Selective Cells" sociales qui détectent la cohérence inter-groupe.

#### **Contre-Récits vs Narratifs Alternatifs**

La recherche montre que les "Contre-Récits" (Counter-Narratives) frontaux sont souvent inefficaces voire contre-productifs (effet boomerang) car ils attaquent directement l'identité de la cible (Brouillage direct). Le JAR suggère l'utilisation de **Narratifs Alternatifs** : proposer une histoire différente, sur une fréquence adjacente, qui satisfait le besoin de fermeture cognitive (Need for Closure) sans confronter directement le dogme établi, permettant un glissement progressif de la fréquence d'opinion.49

### **5.4 Mesure du Succès : La Métrique de Variance Sémantique**

Pour valider le Social JAR, nous devons suivre la **Variance Sémantique** (ou Entropie Sémantique).55

* **Variance Basse :** Chambre d'Écho (Brouillage). L'utilisateur est aveugle à la réalité.  
* **Variance Haute :** Chaos/Bruit. L'utilisateur ne peut former une vision cohérente.  
* **Variance Optimale (Cible du JAR) :** La zone "Goldilocks" où $dF$ est assez grand pour percevoir des objets distincts (points de vue différents) mais assez stable pour maintenir une identité.

## ---

**6\. Architecture Technique Proposée : Le Moteur de Recommandation Dépolarisant**

Basé sur la synthèse du mécanisme biologique et des dynamiques sociales, nous proposons l'architecture technique suivante pour un "Moteur de Recommandation Dépolarisant". Ce système s'intégrerait comme un module de "Re-ranking" (reclassement) par-dessus les algorithmes existants.

### **6.1 La Couche Capteur (Les P-units et T-units Numériques)**

C'est l'interface d'ingestion des données. Elle doit traduire le langage naturel en signaux physiques traitables.

* **Encodeur Sémantique (L'unité T \- Phase) :** Utilise des modèles de langage (LLMs) type BERT ou RoBERTa pour générer des embeddings vectoriels des posts de l'utilisateur. Il calcule la "Phase" (l'angle dans l'espace vectoriel hypersphérique) de la session actuelle de l'utilisateur.44  
* **Détecteur de Sentiment/Viralité (L'unité P \- Amplitude) :** Mesure l'arousal (excitation) et l'amplitude émotionnelle du contenu. Une amplitude élevée combinée à une diversité sémantique faible est l'alerte signature du **Brouillage**.

### **6.2 La Couche de Traitement (Le Torus Semicircularis Numérique)**

C'est le cœur algorithmique qui détecte les chambres d'écho.

* **Cartographe du Plan d'État (State Plane Mapper) :** Le système trace la consommation récente de l'utilisateur dans un espace vectoriel dynamique.  
* **Détection d'Interférence (Calcul du Battement) :**  
  * *Condition :* Si le Vecteur Utilisateur $\\vec{U}$ et le Vecteur Contenu Moyen $\\vec{C}$ ont une Similarité Cosinus $\> 0.95$ sur une fenêtre temporelle $t \> 30$ minutes.  
  * *Diagnostic :* **Brouillage Détecté (Boucle de Chambre d'Écho).** L'utilisateur ne reçoit plus d'information nouvelle, juste de la résonance.  
* **Logique de Sélection de Signe :** Détermine la direction du décalage. L'utilisateur doit-il être poussé vers une nuance "Économique" ou "Éthique"? Ceci est déterminé par l'analyse des "Ponts" (Bridges) disponibles dans le graphe social global.56

### **6.3 La Couche d'Actuation (Le Pacemaker Algorithmique)**

C'est le module qui modifie le flux (Feed) de l'utilisateur.

* **Déplaceur de Fréquence (Frequency Shifter) :** Le moteur de recommandation effectue un re-ranking de la file d'attente.  
  * *Action 1 (Inhibition) :* Dé-prioriser (Down-rank) le contenu "En Phase" (confirmation pure).  
  * *Action 2 (Excitation) :* Sur-prioriser (Up-rank) le contenu "Orthogonal" (Sérendipité/Pont).  
  * *Action 3 (Diversité DPP) :* Appliquer un noyau de processus ponctuel déterminantal pour garantir que les 10 prochains posts ne sont pas colinéaires.39  
* **Boucle de Rétroaction :** Si l'utilisateur interagit avec le contenu orthogonal (Like, Clic, Temps de lecture), l'alarme "Brouillage" est désactivée. S'il le rejette (Scroll rapide), le système tente un décalage de fréquence plus faible (nuance plus subtile), mimant l'ajustement fin du poisson.

#### **Tableau 3 : Matrice de Traduction du "Social JAR"**

| Caractéristique Biologique | Équivalent Social/Informationnel | Objectif du Mimétisme |
| :---- | :---- | :---- |
| **Fréquence EOD** | Position Idéologique / Cadre Narratif de l'Utilisateur | Détecter le positionnement relatif |
| **Brouillage ($dF \\approx 0$)** | Chambre d'Écho / Bulle de Filtre (Vues Identiques) | Identifier la perte de signal/nuance |
| **Battement (AM)** | Boucles de contenu répétitives à forte excitation | Détecter la synchronisation pathologique |
| **Décalage de Fréquence (JAR)** | Injection Algorithmique de Contenu Divers/Orthogonal | Restaurer la capacité d'information |
| **T-unit (Phase)** | Angle d'Embedding Sémantique (Espace Vectoriel) | Mesurer l'orientation narrative |
| **P-unit (Amplitude)** | Métriques d'Engagement (Likes/Partages/Rage) | Mesurer l'intensité du signal |

## ---

**7\. Conclusion et Perspectives**

La Réponse d'Évitement de Brouillage d'*Eigenmannia virescens* n'est pas une simple curiosité biologique ; c'est un algorithme hautement optimisé pour la **préservation du signal dans des environnements compétitifs et bruyants**. En décodant la circuiterie neuronale qui calcule les différentiels phase-amplitude dans le *torus semicircularis*, nous débloquons un modèle puissant pour l'ingénierie de la résilience.

Ce rapport a démontré que ce principe est transposable à trois domaines critiques :

1. Dans les **Réseaux Sans Fil**, il permet une gestion autonome du spectre qui survit là où les protocoles rigides échouent.  
2. En **Cybersécurité**, il fournit le plan pour des Défenses de Cible Mouvante qui "esquivent" les attaquants avant qu'ils ne puissent verrouiller leur cible.  
3. Dans les **Systèmes Sociaux**, il offre l'antidote le plus prometteur à la polarisation : un mécanisme pour détecter le "tassement spectral" des chambres d'écho et induire algorithmiquement les "décalages de fréquence" nécessaires pour restaurer la diversité cognitive de la sphère publique numérique.

Le "Social JAR" ne censure pas ; il assure simplement que la distance entre les signaux ($dF$) reste suffisamment grande pour que l'esprit humain puisse effectuer sa propre "électrolocalisation" — la capacité de percevoir la forme de la réalité sociale au milieu du bruit. En remplaçant l'optimisation de l'engagement par l'optimisation de la distinction spectrale, nous pouvons espérer assainir nos écosystèmes numériques.

#### **Sources des citations**

1. Jamming avoidance response \- Wikipedia, consulté le décembre 30, 2025, [https://en.wikipedia.org/wiki/Jamming\_avoidance\_response](https://en.wikipedia.org/wiki/Jamming_avoidance_response)  
2. A fish may hold the key to more efficient wireless networks \- UGA Today, consulté le décembre 30, 2025, [https://news.uga.edu/fish-more-efficient-wireless-networks-1215/](https://news.uga.edu/fish-more-efficient-wireless-networks-1215/)  
3. Understanding Echo Chambers in Recommender Systems: A Systematic Review \- The Science and Information (SAI) Organization, consulté le décembre 30, 2025, [https://thesai.org/Downloads/Volume16No10/Paper\_71-Understanding\_Echo\_Chambers\_in\_Recommender\_Systems.pdf](https://thesai.org/Downloads/Volume16No10/Paper_71-Understanding_Echo_Chambers_in_Recommender_Systems.pdf)  
4. The Effect of People Recommenders on Echo Chambers and Polarization \- ResearchGate, consulté le décembre 30, 2025, [https://www.researchgate.net/publication/365031329\_The\_Effect\_of\_People\_Recommenders\_on\_Echo\_Chambers\_and\_Polarization](https://www.researchgate.net/publication/365031329_The_Effect_of_People_Recommenders_on_Echo_Chambers_and_Polarization)  
5. Spectrum and Power Efficient Anti-jamming Approach for Cognitive Radio Networks Based on Reinforcement Learning \- Eco-Vector Journals Portal, consulté le décembre 30, 2025, [https://journals.eco-vector.com/2210-3279/article/view/645564](https://journals.eco-vector.com/2210-3279/article/view/645564)  
6. On Random Dynamic Spectrum Access for Cognitive Radio Networks \- ResearchGate, consulté le décembre 30, 2025, [https://www.researchgate.net/publication/221284506\_On\_Random\_Dynamic\_Spectrum\_Access\_for\_Cognitive\_Radio\_Networks](https://www.researchgate.net/publication/221284506_On_Random_Dynamic_Spectrum_Access_for_Cognitive_Radio_Networks)  
7. A Survey on Moving Target Defense for Networks: A Practical View \- MDPI, consulté le décembre 30, 2025, [https://www.mdpi.com/2079-9292/11/18/2886](https://www.mdpi.com/2079-9292/11/18/2886)  
8. IP ADDRESS SHUFFLING USING MOVING TARGET DEFENSE (MTD) \- IJRET, consulté le décembre 30, 2025, [https://ijret.org/volumes/2016v05/i11/IJRET20160511004.pdf](https://ijret.org/volumes/2016v05/i11/IJRET20160511004.pdf)  
9. How Can Recommender Systems Contribute to Mitigate Echo Chambers and Filter Bubbles? | Takuya Kitazawa, consulté le décembre 30, 2025, [https://takuti.me/note/recsys-2021-echo-chambers-and-filter-bubbles/](https://takuti.me/note/recsys-2021-echo-chambers-and-filter-bubbles/)  
10. The Effect of People Recommenders on Echo Chambers and Polarization | Proceedings of the International AAAI Conference on Web and Social Media, consulté le décembre 30, 2025, [https://ojs.aaai.org/index.php/ICWSM/article/view/19275](https://ojs.aaai.org/index.php/ICWSM/article/view/19275)  
11. The jamming avoidance response in the weakly electric fish Eigenmannia. A behavior controlled by distributed evaluation of electroreceptive afferences \- PubMed, consulté le décembre 30, 2025, [https://pubmed.ncbi.nlm.nih.gov/7432544/](https://pubmed.ncbi.nlm.nih.gov/7432544/)  
12. The Jamming Avoidance Response (JAR) of the Electric Fish, Eigenmannia: The Processing of Sensory Information and Motor Control \- ResearchGate, consulté le décembre 30, 2025, [https://www.researchgate.net/publication/299688050\_The\_Jamming\_Avoidance\_Response\_JAR\_of\_the\_Electric\_Fish\_Eigenmannia\_The\_Processing\_of\_Sensory\_Information\_and\_Motor\_Control](https://www.researchgate.net/publication/299688050_The_Jamming_Avoidance_Response_JAR_of_the_Electric_Fish_Eigenmannia_The_Processing_of_Sensory_Information_and_Motor_Control)  
13. Sensory hyperacuity in the jamming avoidance response of weakly electric fish \- University of Toronto Scarborough, consulté le décembre 30, 2025, [https://www.utsc.utoronto.ca/\~amason/courses/coursepage/presentations/files/Sensory%20hyperacuity%20in%20the%20jamming%20avoidance%20response%20of%20weakly%20electric%20fish%20-%20review%20paper.pdf](https://www.utsc.utoronto.ca/~amason/courses/coursepage/presentations/files/Sensory%20hyperacuity%20in%20the%20jamming%20avoidance%20response%20of%20weakly%20electric%20fish%20-%20review%20paper.pdf)  
14. The complexity of high-frequency electric fields degrades electrosensory inputs: implications for the jamming avoidance response in weakly electric fish \- Journals, consulté le décembre 30, 2025, [https://royalsocietypublishing.org/rsif/article/15/138/20170633/64907/The-complexity-of-high-frequency-electric-fields](https://royalsocietypublishing.org/rsif/article/15/138/20170633/64907/The-complexity-of-high-frequency-electric-fields)  
15. RESEARCH ARTICLE Closed-loop stabilization of the Jamming Avoidance Response reveals its locally unstable and globally nonlinear, consulté le décembre 30, 2025, [https://limbs.lcsr.jhu.edu/wp-content/uploads/2013/11/madhavclosed-loop2013.pdf](https://limbs.lcsr.jhu.edu/wp-content/uploads/2013/11/madhavclosed-loop2013.pdf)  
16. The development of the Jamming Avoidance Response (JAR) in Eigenmannia: an innate behavior indeed \- PubMed, consulté le décembre 30, 2025, [https://pubmed.ncbi.nlm.nih.gov/1941715/](https://pubmed.ncbi.nlm.nih.gov/1941715/)  
17. Phase and amplitude computations in the midbrain of an electric fish: intracellular studies of neurons participating in the jamming avoidance response of Eigenmannia \- PMC \- NIH, consulté le décembre 30, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6565201/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6565201/)  
18. Gating of sensory information: joint computations of phase and amplitude data in the midbrain of the electric fish, Eigenmannia \- PubMed, consulté le décembre 30, 2025, [https://pubmed.ncbi.nlm.nih.gov/3772827/](https://pubmed.ncbi.nlm.nih.gov/3772827/)  
19. Beyond the Jamming Avoidance Response: Weakly electric fish respond to the envelope of social electrosensory signals \- ResearchGate, consulté le décembre 30, 2025, [https://www.researchgate.net/publication/233334750\_Beyond\_the\_Jamming\_Avoidance\_Response\_Weakly\_electric\_fish\_respond\_to\_the\_envelope\_of\_social\_electrosensory\_signals](https://www.researchgate.net/publication/233334750_Beyond_the_Jamming_Avoidance_Response_Weakly_electric_fish_respond_to_the_envelope_of_social_electrosensory_signals)  
20. Encoding of social signals in all three electrosensory pathways of Eigenmannia virescens, consulté le décembre 30, 2025, [https://journals.physiology.org/doi/full/10.1152/jn.00116.2014](https://journals.physiology.org/doi/full/10.1152/jn.00116.2014)  
21. Comparative analysis of the jamming avoidance response in African and South American wave-type electric fishes \- PubMed, consulté le décembre 30, 2025, [https://pubmed.ncbi.nlm.nih.gov/8776846/](https://pubmed.ncbi.nlm.nih.gov/8776846/)  
22. Bio-inspired Jamming Avoidance Response \- UGA Photonics and Soft Robotics Lab, consulté le décembre 30, 2025, [https://wave.engr.uga.edu/portfolio/bio-inspired-jamming-avoidance-response/](https://wave.engr.uga.edu/portfolio/bio-inspired-jamming-avoidance-response/)  
23. Dynamic Spectrum Sharing Based on Deep Reinforcement Learning in Mobile Communication Systems \- PMC \- PubMed Central, consulté le décembre 30, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10006914/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10006914/)  
24. Multi-User Opportunistic Spectrum Access for Cognitive Radio Networks Based on Multi-Head Self-Attention and Multi-Agent Deep Reinforcement Learning \- MDPI, consulté le décembre 30, 2025, [https://www.mdpi.com/1424-8220/25/7/2025](https://www.mdpi.com/1424-8220/25/7/2025)  
25. A Novel Dynamic Spectrum Access Framework Based on Reinforcement Learning for Cognitive Radio Sensor Networks \- MDPI, consulté le décembre 30, 2025, [https://www.mdpi.com/1424-8220/16/10/1675](https://www.mdpi.com/1424-8220/16/10/1675)  
26. (PDF) Learning Dynamic Jamming Models in Cognitive Radios \- ResearchGate, consulté le décembre 30, 2025, [https://www.researchgate.net/publication/330713950\_Learning\_Dynamic\_Jamming\_Models\_in\_Cognitive\_Radios](https://www.researchgate.net/publication/330713950_Learning_Dynamic_Jamming_Models_in_Cognitive_Radios)  
27. Improving reinforcement learning algorithms for dynamic spectrum allocation in cognitive sensor networks \- IEEE Xplore, consulté le décembre 30, 2025, [http://ieeexplore.ieee.org/document/6554535/](http://ieeexplore.ieee.org/document/6554535/)  
28. Reinforcement-Learning-Based Dynamic Spectrum Access for Software-Defined Cognitive Industrial Internet of Things \- ResearchGate, consulté le décembre 30, 2025, [https://www.researchgate.net/publication/354740667\_Reinforcement-Learning-Based\_Dynamic\_Spectrum\_Access\_for\_Software-Defined\_Cognitive\_Industrial\_Internet\_of\_Things](https://www.researchgate.net/publication/354740667_Reinforcement-Learning-Based_Dynamic_Spectrum_Access_for_Software-Defined_Cognitive_Industrial_Internet_of_Things)  
29. Dynamic Spectrum Access | Wireless & Mobile Networking (WiMNet) Lab, consulté le décembre 30, 2025, [https://wimnet.ee.columbia.edu/portfolio/dynamic-spectrum-access/](https://wimnet.ee.columbia.edu/portfolio/dynamic-spectrum-access/)  
30. Deep Reinforcement Learning-Based Dynamic Spectrum Access for D2D Communication Underlay Cellular Networks, consulté le décembre 30, 2025, [https://app.cafeprozhe.com/storage/files/project/hatyu9MD5UBG5dhmPWJEyZ9fBAXHhMHKtX4qh2gY.pdf](https://app.cafeprozhe.com/storage/files/project/hatyu9MD5UBG5dhmPWJEyZ9fBAXHhMHKtX4qh2gY.pdf)  
31. Toward Proactive, Adaptive Defense: A Survey on Moving Target Defense \- arXiv, consulté le décembre 30, 2025, [https://arxiv.org/pdf/1909.08092](https://arxiv.org/pdf/1909.08092)  
32. Automated Moving Target Defense \- cybersecurity \- Reddit, consulté le décembre 30, 2025, [https://www.reddit.com/r/cybersecurity/comments/1gmu6nz/automated\_moving\_target\_defense/](https://www.reddit.com/r/cybersecurity/comments/1gmu6nz/automated_moving_target_defense/)  
33. Towards Enhancing the Endpoint Security using Moving Target Defense (Shuffle-based Approach) in Software Defined Networking, consulté le décembre 30, 2025, [https://pdfs.semanticscholar.org/c0dd/d0791e0cf797f824ab29faf3cf4d92d780c2.pdf](https://pdfs.semanticscholar.org/c0dd/d0791e0cf797f824ab29faf3cf4d92d780c2.pdf)  
34. Implementation of a Lossless Moving Target Defense Mechanism \- MDPI, consulté le décembre 30, 2025, [https://www.mdpi.com/2079-9292/13/5/918](https://www.mdpi.com/2079-9292/13/5/918)  
35. girishsg24/Moving-Target-Defense-RHM-using-SDN ... \- GitHub, consulté le décembre 30, 2025, [https://github.com/girishsg24/Moving-Target-Defense-RHM-using-SDN](https://github.com/girishsg24/Moving-Target-Defense-RHM-using-SDN)  
36. Moving Target Defense for Space Systems \- OSTI, consulté le décembre 30, 2025, [https://www.osti.gov/servlets/purl/1848040](https://www.osti.gov/servlets/purl/1848040)  
37. GANs Failure Modes: How to Identify and Monitor Them, consulté le décembre 30, 2025, [https://neptune.ai/blog/gan-failure-modes](https://neptune.ai/blog/gan-failure-modes)  
38. GAN — Why it is so hard to train Generative Adversarial Networks\! \- Jonathan Hui \- Medium, consulté le décembre 30, 2025, [https://jonathan-hui.medium.com/gan-why-it-is-so-hard-to-train-generative-advisory-networks-819a86b3750b](https://jonathan-hui.medium.com/gan-why-it-is-so-hard-to-train-generative-advisory-networks-819a86b3750b)  
39. Diversity in Recommendations — Determinantal Point Processes (DPP) | by Aayush Agrawal | Dec, 2025 | Medium, consulté le décembre 30, 2025, [https://medium.com/@aayushmnit/diversity-in-recommendations-determinantal-point-processes-dpp-2427bf1b6324](https://medium.com/@aayushmnit/diversity-in-recommendations-determinantal-point-processes-dpp-2427bf1b6324)  
40. Fast Greedy MAP Inference for Determinantal Point Process to Improve Recommendation Diversity \- NIPS papers, consulté le décembre 30, 2025, [http://papers.neurips.cc/paper/7805-fast-greedy-map-inference-for-determinantal-point-process-to-improve-recommendation-diversity.pdf](http://papers.neurips.cc/paper/7805-fast-greedy-map-inference-for-determinantal-point-process-to-improve-recommendation-diversity.pdf)  
41. On the Performance of Generative Adversarial Network by Limiting Mode Collapse for Malware Detection Systems \- PMC \- NIH, consulté le décembre 30, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8749644/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8749644/)  
42. Soft Generative Adversarial Network: Combating Mode Collapse in Generative Adversarial Network Training via Dynamic Borderline Softening Mechanism \- MDPI, consulté le décembre 30, 2025, [https://www.mdpi.com/2076-3417/14/2/579](https://www.mdpi.com/2076-3417/14/2/579)  
43. \[2110.11981\] How to Quantify Polarization in Models of Opinion Dynamics \- arXiv, consulté le décembre 30, 2025, [https://arxiv.org/abs/2110.11981](https://arxiv.org/abs/2110.11981)  
44. \[2510.19656\] Sentiment Analysis of Social Media Data for Predicting Consumer Behavior Trends Using Machine Learning \- arXiv, consulté le décembre 30, 2025, [https://arxiv.org/abs/2510.19656](https://arxiv.org/abs/2510.19656)  
45. Modeling of the Public Opinion Polarization Process with the Considerations of Individual Heterogeneity and Dynamic Conformity \- MDPI, consulté le décembre 30, 2025, [https://www.mdpi.com/2227-7390/7/10/917](https://www.mdpi.com/2227-7390/7/10/917)  
46. Opinion dynamics: Statistical physics and beyond \- arXiv, consulté le décembre 30, 2025, [https://arxiv.org/html/2507.11521v1](https://arxiv.org/html/2507.11521v1)  
47. (PDF) Partial synchronization in the Kuramoto model with attractive and repulsive interactions via the Bellerophon state \- ResearchGate, consulté le décembre 30, 2025, [https://www.researchgate.net/publication/351840601\_Partial\_synchronization\_in\_the\_Kuramoto\_model\_with\_attractive\_and\_repulsive\_interactions\_via\_the\_Bellerophon\_state](https://www.researchgate.net/publication/351840601_Partial_synchronization_in_the_Kuramoto_model_with_attractive_and_repulsive_interactions_via_the_Bellerophon_state)  
48. Cyclops states in repulsive Kuramoto networks: the role of higher-order coupling \- Mathematics and Statistics, consulté le décembre 30, 2025, [https://math.gsu.edu/ibelykh/prl\_cyclope\_states\_submitted.pdf](https://math.gsu.edu/ibelykh/prl_cyclope_states_submitted.pdf)  
49. Do Counter-Narratives Reduce Support for ISIS? Yes, but Not for Their Target Audience, consulté le décembre 30, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7325943/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7325943/)  
50. How does serendipity affect diversity in recommender systems? A serendipity-oriented greedy algorithm \- JYX: JYU, consulté le décembre 30, 2025, [https://jyx.jyu.fi/jyx/Record/jyx\_123456789\_67800](https://jyx.jyu.fi/jyx/Record/jyx_123456789_67800)  
51. Serendipity in Recommender Systems \- Semantic Scholar, consulté le décembre 30, 2025, [https://pdfs.semanticscholar.org/fc47/50727d505f6ca3109ee60f254c8e2c38f6cd.pdf](https://pdfs.semanticscholar.org/fc47/50727d505f6ca3109ee60f254c8e2c38f6cd.pdf)  
52. vTaiwan \- Participedia, consulté le décembre 30, 2025, [https://participedia.net/method/vtaiwan](https://participedia.net/method/vtaiwan)  
53. Bridging Systems: Open problems for countering destructive divisiveness across ranking, recommenders, and governance | Knight First Amendment Institute, consulté le décembre 30, 2025, [https://knightcolumbia.org/content/bridging-systems](https://knightcolumbia.org/content/bridging-systems)  
54. Do counter-narratives actually reduce violent extremism? \- Brookings Institution, consulté le décembre 30, 2025, [https://www.brookings.edu/articles/do-counter-narratives-actually-reduce-violent-extremism/](https://www.brookings.edu/articles/do-counter-narratives-actually-reduce-violent-extremism/)  
55. Achieving Semantic Consistency: Contextualized Word Representations for Political Text Analysis \- arXiv, consulté le décembre 30, 2025, [https://arxiv.org/html/2412.04505v2](https://arxiv.org/html/2412.04505v2)  
56. Bridge-building instead of polarization \- Bertelsmann Stiftung, consulté le décembre 30, 2025, [https://bridging.reframetech.de/en](https://bridging.reframetech.de/en)  
57. mayankmanj/k-DPP-reco-engine: Determinantal point processes for basket recommendations \- GitHub, consulté le décembre 30, 2025, [https://github.com/mayankmanj/k-DPP-reco-engine](https://github.com/mayankmanj/k-DPP-reco-engine)