L'Architecture Isomorphe : Une Stratégie pour l'Éradication Totale du Parsing

1. Introduction : La Crise Silencieuse de l'Interprétation

L'informatique moderne repose sur un paradoxe fondamental. D'un côté, nous disposons de processeurs capables d'exécuter des milliards d'opérations par seconde. De l'autre, la majorité de cette puissance est gaspillée pour traduire des données d'un format à un autre. Ce phénomène est le parsing.
Le parsing est le processus consistant à transformer une séquence linéaire de symboles en une structure de données hiérarchique. Cette transformation coûteuse se produit à chaque frontière du système. Les études montrent que les applications modernes peuvent passer entre 80 % et 90 % de leur temps CPU uniquement à parser des données. De plus, le parsing est le vecteur principal des vulnérabilités de sécurité (LangSec).
Ce document propose l'Architecture Isomorphe, qui aligne la représentation des données en mémoire, sur le disque et sur le réseau, rendant l'acte de parser obsolète.


2. Anatomie de la Pathologie du Parsing

2.1 L'Inadéquation d'Impédance

Il existe une divergence entre le stockage (séquentiel) et la mémoire (accès aléatoire). Pour combler ce fossé, nous utilisons la sérialisation, qui "aplatit" les objets.

Domaine
Nature de la Donnée
Mécanisme d'Accès
Mémoire (RAM)
Graphe structuré
Accès direct (O(1))
Disque
Séquence linéaire
Accès séquentiel (O(n))
ZPA
Isomorphe
Accès direct via mmap


2.2 La Menace Sécuritaire (LangSec)

La Sécurité Théorique des Langages postule qu'on ne peut pas sécuriser le parsing de langages complexes. Les "Weird Machines" exploitent les divergences d'interprétation des parseurs pour exécuter du code arbitraire. La seule solution est d'éliminer le besoin de vérifier la syntaxe complexe en utilisant des structures de données valides par construction.


3. Solution Technique : Le Stack "Zero-Parse"

3.1 Données : Sérialisation Zéro-Copie (Cap'n Proto)
Nous devons utiliser des formats où la représentation binaire est identique en mémoire et sur le disque, comme Cap'n Proto ou FlatBuffers. Ces formats utilisent des pointeurs relatifs et ne nécessitent aucun décodage.

3.2 Persistance : Mémoire Mappée (LMDB)
Au lieu de lire des fichiers, nous utilisons mmap pour projeter le disque dans l'espace d'adressage virtuel. LMDB permet de gérer des bases de données immenses comme de la RAM, avec un chargement paresseux géré par le matériel (MMU).

3.3 Code et Interface : Unison et Édition Projectionnelle
Pour le code, nous adoptons des langages adressés par le contenu comme Unison, où le code est stocké sous forme d'AST hashé dans une base de données, éliminant le parsing du code source. L'humain interagit via des éditeurs projectionnels (comme MPS) qui manipulent directement la structure, empêchant la création d'erreurs de syntaxe.


4. Conclusion
L'Architecture Isomorphe (ZPA) est réalisable aujourd'hui avec le matériel existant. Elle permet de passer d'un paradigme de "Lecture -> Traduction -> Traitement" à "Mappage -> Utilisation".
