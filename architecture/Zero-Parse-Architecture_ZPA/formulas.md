1. Complexité Temporelle du Parsing Traditionnel
Dans une architecture classique (JSON/XML), pour accéder à un élément $e$ situé à la position $i$ dans un flux de données, le processeur doit lire et analyser tous les éléments précédents.

$$T_{access}(i) = \sum_{k=0}^{i} (T_{read}(b_k) + T_{lex}(b_k) + T_{parse}(b_k))$$
Où :
$T_{read}$ est le temps de lecture de l'octet.
$T_{lex}$ est le temps d'analyse lexicale (tokenization).
$T_{parse}$ est le temps de construction de l'AST.
La complexité est donc linéaire :


$$T_{total} = O(n)$$
2. Complexité Temporelle de l'Architecture Zéro-Parse
Dans l'architecture ZPA, l'accès à un élément est calculé par arithmétique de pointeur. La position mémoire $P_{i}$ de l'élément $i$ est donnée par :

$$P_{i} = P_{base} + (i \times S_{struct})$$
Où :
$P_{base}$ est l'adresse mémoire virtuelle du début du fichier mappé (via mmap).
$S_{struct}$ est la taille fixe de la structure en octets (padding inclus pour l'alignement).
Le temps d'accès est constant, quel que soit la taille du fichier :


$$T_{total} = O(1)$$
3. Efficacité Énergétique (Loi de Zeller-Palkar)
Si $E_{cpu}$ est l'énergie consommée par cycle CPU, l'économie d'énergie $\Delta E$ réalisée par ZPA est définie par l'élimination des cycles de transformation ($\eta_{trans}$) :

$$\Delta E = E_{total} - E_{utile} = \int_{t=0}^{T} \eta_{trans}(t) \,dt$$
Les recherches montrent que $\eta_{trans}$ représente jusqu'à 80-90% de la consommation CPU dans les systèmes Big Data.1 L'approche ZPA vise :

$$\lim_{ZPA \to \infty} \eta_{trans} = 0$$
