# **PROJET DE NORME ISO 27050 (ISO-IVIM) : SYSTÈME DE MANAGEMENT DE LA VÉRACITÉ INFORMATIONNELLE ET DE L'INTÉGRITÉ MÉDIATIQUE**

## **1\. Introduction : L'Urgence d'une Architecture Normative pour la Sécurité Cognitive**

L'ère numérique a engendré un paradoxe déstabilisant : alors que l'accès à l'information est devenu universel, la certitude quant à la véracité de cette information s'est effondrée. La désinformation n'est plus un simple phénomène de nuisance publique ou de propagande politique traditionnelle ; elle est devenue une infrastructure systémique de radicalisation et de déstabilisation sociétale. Face à ce défi, les réponses législatives nationales ou les initiatives isolées de vérification des faits (*fact-checking*) se révèlent insuffisantes car fragmentées et souvent perçues comme partisanes.

Ce rapport de recherche propose l'élaboration de la première norme internationale sous l'égide de l'Organisation Internationale de Normalisation (ISO), provisoirement désignée **ISO-IVIM (Information Veracity and Integrity Management)** ou ISO 27050\. L'objectif n'est pas de créer un "ministère de la vérité" mondial, mais d'établir un référentiel technique, méthodologique et éthique auditable, permettant de certifier les processus de production et de diffusion de l'information. Cette norme est conçue pour s'interfacer directement avec les systèmes éducatifs mondiaux (via ISO 21001\) et servir de signal de confiance universel pour les algorithmes des plateformes numériques, créant ainsi une source de vérité globale et résiliente.

L'analyse qui suit dissèque les mécanismes psychosociaux de la radicalisation que la norme doit neutraliser, évalue les standards existants (ISO 8000, JTI, C2PA) pour en extraire les briques fondamentales, et détaille l'architecture de la future norme ISO-IVIM.

## ---

**2\. Analyse Phénoménologique : Désinformation, Radicalisation et Média**

Pour concevoir une norme efficace, il est impératif de comprendre la pathologie qu'elle vise à traiter. La désinformation ne fonctionne pas dans le vide ; elle exploite des vulnérabilités cognitives spécifiques et des structures algorithmiques pour induire des changements comportementaux, dont le plus extrême est la radicalisation.

### **2.1 La Mécanique de la Radicalisation : Vecteurs Descendants et Ascendants**

La littérature scientifique identifie deux dynamiques principales de radicalisation que la norme ISO-IVIM doit impérativement intercepter dans ses protocoles de risque.

L'approche traditionnelle, ou modèle "Top-Down" (descendant), théorisé par Hoffman (2006), décrit la radicalisation comme un processus orchestré par des organisations structurées. Dans ce schéma, des leaders charismatiques et des groupes organisés manipulent les individus via une propagande ciblée et un endoctrinement progressif.1 La désinformation y est utilisée comme une arme stratégique pour aligner la vision du monde de la recrue sur l'idéologie du groupe, souvent en exploitant des griefs politiques ou sociaux préexistants.

Cependant, l'architecture des médias sociaux a favorisé l'émergence d'un modèle "Bottom-Up" (ascendant), ou auto-radicalisation. Ce phénomène se produit lorsque des individus, souvent isolés, recherchent activement des contenus extrémistes sur des plateformes non régulées ou cryptées comme Telegram, 4chan, ou Reddit.1 Binder et Kenyon (2022) soulignent que ces individus gravitent vers des communautés qui valident leurs frustrations personnelles. Dans ce contexte, la désinformation n'est pas toujours imposée d'en haut ; elle est consommée volontairement pour satisfaire un besoin psychologique de cohérence ou d'appartenance.1

La norme ISO-IVIM doit donc agir sur deux fronts :

1. **Contre le modèle Top-Down :** En exigeant une transparence totale sur la propriété et le financement des médias (inspiré de la JTI) pour empêcher les acteurs malveillants d'opérer dans l'ombre.  
2. **Contre le modèle Bottom-Up :** En imposant des marqueurs de fiabilité visibles et intelligibles (provenance C2PA) qui pénètrent les bulles de filtre et offrent des alternatives cognitives aux narratifs complotistes.

### **2.2 La Boucle de Polarisation (The Polarization Loop)**

Le moteur central de la diffusion de la désinformation réside dans ce que les chercheurs appellent la "boucle de polarisation". Ce modèle causal explique la relation cyclique et auto-renforçante entre les messages extrêmes, l'engagement émotionnel et l'amplification médiatique.2

| Composante | Description du Mécanisme | Implication pour la Norme ISO-IVIM |
| :---- | :---- | :---- |
| **Message Extrême** | Contenu divisif défiant le consensus, souvent caractérisé par une rhétorique hostile et sans compromis.2 | La norme doit inclure des critères d'analyse sémantique (W3C Signals) pour détecter la toxicité et l'absence de nuance. |
| **Engagement Émotionnel** | La peur, la colère et l'outrage augmentent la viralité via la "contagion émotionnelle". C'est le mécanisme "Thinking Fast" de Kahneman qui est exploité.2 | Les indicateurs de performance (KPI) des médias certifiés ne doivent pas être basés uniquement sur l'engagement, mais sur la "valeur ajoutée" informationnelle.3 |
| **Amplification Médiatique** | Les algorithmes privilégient le contenu à fort engagement, propulsant les messages radicaux vers une audience large.2 | La norme doit exiger des plateformes une "Transparence Algorithmique" prouvant que les signaux de véracité (ISO-IVIM) pèsent plus lourd que les signaux d'engagement émotionnel. |

Cette boucle crée un environnement où la vérité factuelle, souvent complexe et moins émotionnellement stimulante, est désavantagée. La norme ISO-IVIM vise à inverser cette asymétrie en créant un "avantage algorithmique" pour le contenu certifié.

### **2.3 Biais Cognitifs et Persistance de l'Erreur**

L'analyse psychologique révèle que l'exposition répétée à des contenus extrémistes exploite l'**effet de vérité illusoire** (*illusory truth effect*), où une affirmation fausse finit par sembler vraie simplement parce qu'elle est familière.4 Les réseaux de bots et les fermes à clics exploitent industriellement ce biais cognitif. De plus, le **biais de confirmation** pousse les individus à rejeter les corrections qui contredisent leur identité politique ou sociale.

Plus inquiétant encore est l'**effet d'influence continue** (*continued influence effect*), observé par Johnson et Seifert (1994), où les individus continuent de s'appuyer sur une information erronée pour leur raisonnement même après qu'elle a été formellement démentie.4 Cela démontre l'insuffisance des méthodes actuelles de "Debunking". La norme ISO-IVIM devra donc standardiser non seulement la vérification, mais aussi la *pédagogie de la correction*, s'assurant que le rectificatif soit cognitivement aussi saillant que l'erreur initiale.

### **2.4 Typologie des Désordres Informationnels**

Pour être techniquement précise, la norme doit adopter la terminologie experte distinguant trois types de menaces 5 :

1. **Misinformation (Mésinformation) :** Information fausse diffusée sans intention de nuire (ex: erreur journalistique). La réponse normative est la correction (ISO 10002).  
2. **Disinformation (Désinformation) :** Information fausse créée et diffusée délibérément pour nuire (ex: propagande d'état, fabrication de preuves). La réponse normative est l'audit de sécurité et la provenance (C2PA).  
3. **Malinformation :** Information factuellement vraie mais utilisée hors contexte ou divulguée pour causer du tort (ex: revenge porn, doxxing). La réponse normative relève de l'éthique et de la protection de la vie privée (ISO 27701).

## ---

**3\. Audit des Standards Existants : Les Briques de la Future Norme**

Il n'est pas nécessaire de créer la norme ISO-IVIM *ex nihilo*. Plusieurs cadres normatifs et techniques existent déjà, couvrant des aspects fragmentés du problème. L'enjeu est de les intégrer dans un système de management cohérent.

### **3.1 ISO 8000 : La Qualité des Données comme Socle Insuffisant**

La norme **ISO 8000** traite de la qualité des données industrielles et administratives. Elle définit la qualité des données comme "le degré auquel un ensemble de caractéristiques inhérentes aux données satisfait aux exigences".6

* **Apports pertinents :**  
  * **Exactitude (Accuracy) :** La donnée représente correctement la réalité (ex: un capteur de température indique la bonne valeur).8  
  * **Provenance :** La capacité de tracer l'historique et l'origine de la donnée.  
  * **Complétude :** L'absence de lacunes qui pourraient fausser l'interprétation.7  
  * **Cohérence (Consistency) :** L'absence de contradictions au sein du jeu de données.9  
* **Limites critiques :** L'ISO 8000 est conçue pour des données structurées (chiffres, codes). Elle est inopérante pour analyser la *sémantique narrative* ou l'intentionnalité d'un article de presse. Elle peut certifier qu'une base de données de propagande est "techniquement parfaite" (pas de doublons, format correct), sans détecter sa fausseté morale ou factuelle. L'ISO-IVIM devra donc étendre les principes de l'ISO 8000 à la donnée non structurée et narrative.

### **3.2 Journalism Trust Initiative (JTI) \- CWA 17493**

Développée par le CEN (Comité Européen de Normalisation) et Reporters Sans Frontières, la **CWA 17493** est le précurseur le plus direct de notre projet.10 Elle se concentre sur l'identité et les processus des médias.

* **Apports pertinents :**  
  * **Transparence de la Propriété :** Exigence absolue de divulguer les bénéficiaires effectifs ultimes, empêchant les médias "coquilles vides".12  
  * **Transparence des Revenus :** Obligation de lister les sources de revenus (publicité, subventions, abonnements) pour identifier les conflits d'intérêts potentiels.10  
  * **Mission Éditoriale :** Définition claire de la ligne éditoriale et des mécanismes de responsabilité.13  
* **Limites critiques :** La JTI certifie le *contenant* (l'entreprise médiatique) mais pas le *contenu*. Un média certifié JTI pourrait théoriquement publier une erreur majeure si ses processus internes échouent ponctuellement. La JTI est une condition nécessaire mais non suffisante pour garantir la vérité informationnelle "atomique" (article par article).

### **3.3 IFCN Code of Principles : La Méthodologie du Fact-Checking**

L'International Fact-Checking Network (IFCN) a établi un code de principes qui régit la communauté des vérificateurs de faits.14

* **Apports pertinents :**  
  * **Reproductibilité (Transparency of Sources) :** C'est le principe scientifique clé. Le lecteur doit pouvoir suivre le cheminement logique et accéder aux sources primaires pour reproduire la conclusion du vérificateur.15  
  * **Non-partisanerie :** Application des mêmes standards de preuve à toutes les affirmations, quelle que soit leur origine politique.16

### **3.4 Standards Techniques : C2PA et W3C**

Pour passer d'une certification "déclarative" à une certification "technique", l'ISO-IVIM doit intégrer des protocoles informatiques.

* **C2PA (Coalition for Content Provenance and Authenticity) :** Ce standard permet de lier cryptographiquement la provenance à un fichier numérique (image, vidéo, audio).17 Il crée une chaîne de contrôle inviolable depuis la capture (appareil photo) jusqu'à la publication, en passant par l'édition (Photoshop). Il agit comme une "étiquette nutritionnelle" inviolable du contenu numérique.18  
* **W3C Credibility Signals :** Le groupe communautaire du W3C a identifié plus de 200 signaux techniques associés à la crédibilité (ex : citation d'experts, absence de titres clickbait, valence émotionnelle neutre).19 Ces signaux permettent une évaluation automatisée préliminaire.

## ---

**4\. Architecture de la Norme ISO-IVIM (Proposition Détaillée)**

Nous proposons ici la structure formelle de la norme **ISO-IVIM : Système de Management de la Véracité Informationnelle et de l'Intégrité Médiatique**. Elle suit la structure HLS (High Level Structure) commune à toutes les normes ISO modernes (comme ISO 9001 ou ISO 27001\) pour faciliter son adoption par les organisations déjà certifiées.

### **4.1 Domaine d'Application**

La norme s'applique à toute entité qui produit, édite, agrège ou enseigne de l'information publique. Cela inclut les entreprises de presse, les plateformes de réseaux sociaux, les ONG éducatives, les ministères de l'éducation et les instituts de fact-checking.

### **4.2 Clause 4 : Contexte de l'Organisation et Analyse de Risque**

L'organisation doit comprendre son écosystème informationnel et évaluer son exposition aux risques de désinformation.

* **4.1 Cartographie des Menaces :** L'organisation doit identifier les acteurs susceptibles de cibler ses contenus (états hostiles, groupes d'intérêts, trolls).  
* **4.2 Évaluation de la Vulnérabilité Cognitive :** Analyse de la susceptibilité de l'audience cible à la radicalisation (modèle bottom-up) et mise en place de garde-fous sémantiques.1

### **4.3 Clause 5 : Leadership et Transparence (Le Pilier "Identité")**

Cette clause intègre les exigences du CWA 17493 (JTI).

* **5.1 Propriété et Influence :** Publication obligatoire et mise à jour annuelle de l'organigramme complet des actionnaires directs et indirects (Beneficial Owners).12  
* **5.2 Indépendance Financière :** Les sources de financement dépassant un certain seuil (ex: 5% du budget) doivent être publiques. Une clause de "pare-feu" doit être prouvée entre les financeurs et la direction éditoriale.15

### **4.4 Clause 6 : Planification et Objectifs de Qualité**

L'organisation doit définir des objectifs mesurables (KPI) pour la qualité de l'information, et non seulement pour la performance économique.

* **Exemples de KPI ISO-IVIM :**  
  * Taux de rectification (vitesse moyenne de correction d'une erreur avérée).  
  * Indice de diversité des sources (pour éviter les chambres d'écho).  
  * Taux de conformité C2PA (pourcentage de contenus visuels disposant d'une provenance cryptographique).

### **4.5 Clause 7 : Support et Infrastructure Technique (Le Pilier "Provenance")**

C'est ici que la norme ISO-IVIM innove radicalement en rendant obligatoires des technologies de traçabilité.

* **7.1 Provenance Cryptographique (Standard C2PA) :** Tout contenu multimédia diffusé par l'entité certifiée doit inclure des métadonnées C2PA (Content Credentials). Ces métadonnées doivent attester de l'origine (humaine ou synthétique/IA) et de l'historique des modifications.21  
  * *Exigence spécifique :* Les images générées par IA doivent porter un marquage explicite et indélébile dans les métadonnées.  
* **7.2 Sécurité de l'Information (ISO 27001\) :** L'organisation doit sécuriser ses CMS (Content Management Systems) pour éviter le piratage et l'injection de fausses nouvelles, garantissant l'intégrité (le 'I' de la triade CIA).22  
* **7.3 Compétence des Vérificateurs :** Le personnel chargé de la vérification doit être formé aux techniques OSINT (Open Source Intelligence), à la détection des biais cognitifs et à l'analyse statistique.23

### **4.6 Clause 8 : Réalisation des Activités Opérationnelles (Le Pilier "Méthodologie")**

Cette clause définit le "protocole industriel" de la vérité.

#### **8.1 Protocole de Corroboration Croisée (Cross-Corroboration)**

Pour qu'une affirmation soit certifiée "conforme ISO-IVIM", elle doit subir un processus de vérification strict 23 :

* **Triangulation :** Chaque fait contesté doit être corroboré par au moins deux sources indépendantes l'une de l'autre (pour éviter la circularité des sources), ou par une source primaire directe (document officiel, donnée brute).  
* **Traçabilité des Sources :** Chaque affirmation doit être liée par hyperlien ou référence bibliographique à sa source. L'utilisation de sources anonymes est restreinte aux cas de force majeure (sécurité de la source) et doit être explicitement justifiée par la direction.16

#### **8.2 Analyse de la Valence Émotionnelle et Sémantique**

Pour contrer la radicalisation par l'émotion 2, le contenu doit être audité sur sa forme :

* **Neutralité du Titre :** Le titre doit refléter fidèlement le contenu de l'article sans exagération (lutte contre le clickbait).  
* **Signaux W3C :** Le contenu ne doit pas utiliser de techniques de manipulation émotionnelle (ex: usage excessif de majuscules, langage déshumanisant, appels à la violence).20

#### **8.3 Gestion des Corrections (Adaptation ISO 10002\)**

L'erreur est inévitable. Sa gestion définit la fiabilité. En adaptant l'ISO 10002 (Traitement des réclamations) 24 :

* **Accessibilité :** Un mécanisme clair et visible doit permettre au public de signaler une erreur factuelle.  
* **Proportionnalité de la Correction :** Si une erreur a été vue par 1 million de personnes, la correction doit être diffusée avec des moyens techniques visant à atteindre cette même audience (push notif, épinglage), contrant ainsi l'effet d'influence continue.4

### **4.7 Clause 9 : Évaluation de la Performance et Audit**

La certification ISO-IVIM ne peut être auto-déclarée.

* **Audit Tierce Partie :** Des organismes certificateurs accrédités (type Bureau Veritas, SGS, DNV) doivent auditer annuellement la conformité de l'organisation.26  
* **Audit Algorithmique :** Des tests automatisés vérifieront la présence des métadonnées C2PA et la validité des liens sources sur un échantillon aléatoire de contenus publiés.

## ---

**5\. Application 1 : Une Éducation Standard Mondiale Garantie**

L'un des objectifs majeurs de la requête est de garantir une éducation mondiale standard. L'ISO-IVIM fournit l'infrastructure de confiance nécessaire pour cela, en s'intégrant à la norme **ISO 21001** (Systèmes de management pour les organismes d'éducation).

### **5.1 Sécurisation de la Chaîne d'Approvisionnement Cognitive**

Actuellement, les manuels scolaires et ressources éducatives sont vulnérables au révisionnisme historique et aux biais idéologiques nationaux.

* **Certification des Ressources Pédagogiques :** L'ISO-IVIM permettrait de certifier les *intrants* éducatifs. Une école certifiée ISO 21001 pourrait exiger que ses manuels d'histoire ou de sciences soient produits par des éditeurs certifiés ISO-IVIM.  
* **Mécanisme :** Dans un manuel numérique certifié, chaque affirmation historique majeure (ex: causes d'une guerre) serait liée à des sources primaires vérifiées et porterait une signature de provenance. Cela crée un socle de "faits communs" universels, difficilement contestables par la propagande locale.

### **5.2 Intégration dans le Curriculum MIL (Media and Information Literacy)**

L'UNESCO promeut l'éducation aux médias et à l'information (MIL).27 L'ISO-IVIM fournit les outils pratiques pour ce curriculum.

* **Compétence de Vérification :** Les élèves apprendraient non seulement à "douter", mais à "auditer". Le programme inclurait l'apprentissage de la lecture des étiquettes de provenance C2PA ("Qui a pris cette photo?") et l'évaluation des signaux de crédibilité W3C.  
* **Résilience à la Radicalisation :** En comprenant les mécanismes de la "boucle de polarisation" et les biais cognitifs (enseignés dès le secondaire), les élèves développent une immunité cognitive contre les techniques de recrutement extrémistes.1

### **5.3 Respect des Savoirs Autochtones (IEEE P2890)**

Pour être véritablement mondiale, l'éducation ne doit pas être une imposition occidentale. L'ISO-IVIM intègre les principes du standard **IEEE P2890** sur la provenance des données autochtones.29

* **Souveraineté des Données :** La norme reconnaît que certaines connaissances appartiennent à des communautés spécifiques. Dans le contexte éducatif, cela signifie que les informations concernant les peuples autochtones doivent inclure une provenance attestant qu'elles ont été collectées avec leur consentement et selon leurs protocoles de savoir.

## ---

**6\. Application 2 : Source de Vérité et Fact-Checking Global**

L'ISO-IVIM permet la création d'une infrastructure technique pour un fact-checking mondial, fonctionnant comme une chambre de compensation (*clearinghouse*) de la vérité.

### **6.1 Interopérabilité Fédérée des Fact-Checkers**

Actuellement, les fact-checkers (comme ceux certifiés IFCN) travaillent souvent en silos nationaux. L'ISO-IVIM impose un format de données standardisé (basé sur Schema.org ClaimReview enrichi).

* **Le Réseau de Vérité :** Si un fact-checker au Brésil (ex: *Aos Fatos*) vérifie une rumeur virale sur un virus et publie le résultat au format ISO-IVIM, cette "unité de vérité" est immédiatement lisible et utilisable par un agrégateur en Inde ou en France.  
* **Économie d'Échelle :** On évite la duplication des efforts. Une fausse citation attribuée à une personnalité politique mondiale n'a besoin d'être démentie qu'une seule fois par une source certifiée pour que le démenti soit propagé globalement.

### **6.2 Le Concept de "Safe Harbor" Algorithmique**

Les grandes plateformes (Meta, Google, X, TikTok) sont sous pression pour modérer le contenu sans devenir des censeurs arbitraires. L'ISO-IVIM offre une solution neutre.

* **Priorisation, pas Censure :** Les algorithmes de recommandation pourraient être programmés pour donner un "boost" de visibilité aux contenus provenant de sources certifiées ISO-IVIM.  
* **Déclassement du Bruit :** À l'inverse, les contenus viraux dépourvus de provenance C2PA ou émanant de sources opaques (non conformes à la Clause 5\) verraient leur portée virale artificiellement freinée (friction algorithmique) pour empêcher la boucle de polarisation de s'emballer.2

### **6.3 Une Base de Données pour l'IA (Grounding for AI)**

Avec l'essor des IA génératives qui "hallucinent", l'ISO-IVIM offre une base de données d'entraînement propre.

* **Corpus de Haute Fidélité :** Les développeurs d'IA pourraient privilégier les corpus de textes issus de médias certifiés ISO-IVIM pour l'entraînement (Pre-training) ou l'ancrage (RAG \- Retrieval Augmented Generation) de leurs modèles, réduisant ainsi la génération de désinformation par les machines elles-mêmes.

## ---

**7\. Tableau de Synthèse : Comparaison ISO-IVIM vs Standards Actuels**

Le tableau ci-dessous résume comment l'ISO-IVIM comble les lacunes des normes actuelles pour fournir une solution intégrée.

| Domaine Fonctionnel | Standard Existant | Lacune Identifiée | Solution Intégrée ISO-IVIM |
| :---- | :---- | :---- | :---- |
| **Qualité Technique** | ISO 8000 | Focalisé sur la donnée structurée, ignore le narratif et l'intention.30 | Extension des critères de qualité (exactitude, cohérence) aux contenus narratifs et multimédias. |
| **Identité Média** | JTI (CWA 17493\) | Certifie l'entreprise, pas le contenu individuel.12 | Lie la certification de l'entité à la certification technique de chaque contenu (C2PA). |
| **Méthodologie** | IFCN Code | Principes éthiques auto-régulés, manque de contrainte technique.15 | Rend les principes (reproductibilité) auditables par des tiers accrédités ISO. |
| **Provenance** | C2PA / CAI | Standard technique optionnel, adoption lente par l'industrie.17 | Rend l'adoption du C2PA obligatoire pour obtenir la certification ISO-IVIM (Clause 7). |
| **Correction** | ISO 10002 | Conçu pour les réclamations commerciales, pas le débat public.24 | Adaptation pour garantir une "visibilité réparatrice" des rectificatifs médiatiques. |
| **Éducation** | ISO 21001 | Gère le management éducatif, pas la vérité des manuels.31 | Ajoute une exigence de conformité ISO-IVIM pour les ressources pédagogiques critiques. |

## ---

**8\. Conclusion**

La crise de la vérité informationnelle est un défi systémique qui menace les fondements mêmes de la démocratie et de la cohésion sociale mondiale. La désinformation, en exploitant nos biais cognitifs et les failles algorithmiques, alimente une radicalisation qui peut déstabiliser des nations entières.

La proposition de norme **ISO-IVIM** présentée dans ce rapport ne cherche pas à imposer une vérité unique, mais à établir un **protocole de confiance universel**. En fusionnant la rigueur de la gestion de la qualité industrielle (ISO), la transparence de la propriété médiatique (JTI), la traçabilité cryptographique (C2PA) et la méthodologie scientifique du fact-checking (IFCN), cette norme offre une architecture robuste.

Sa mise en œuvre permettrait de :

1. **Assainir l'espace numérique** en donnant un avantage concurrentiel à l'information vérifiée.  
2. **Protéger les systèmes éducatifs** contre la pollution cognitive et le révisionnisme.  
3. **Fournir aux citoyens et aux algorithmes** les outils nécessaires pour distinguer le signal du bruit dans le chaos informationnel du 21ème siècle.

L'ISO-IVIM transforme la "vérité" d'une notion philosophique abstraite en un bien public tangible, auditable et protégeable.

#### **Sources des citations**

1. How Misinformation and Disinformation Fuel Online Radicalization | Quinnipiac University, consulté le janvier 1, 2026, [https://iq.qu.edu/experiential-learning/course-projects-and-capstones/student-projects/political-extremism-and-online-radicalization/](https://iq.qu.edu/experiential-learning/course-projects-and-capstones/student-projects/political-extremism-and-online-radicalization/)  
2. The Polarization Loop: How Emotions Drive Propagation of Disinformation in Online Media—The Case of Conspiracy Theories and Extreme Right Movements in Southern Europe \- MDPI, consulté le janvier 1, 2026, [https://www.mdpi.com/2076-0760/13/11/603](https://www.mdpi.com/2076-0760/13/11/603)  
3. “Media time” is considered a valuable KPI, but quality of content also matters \- INMA, consulté le janvier 1, 2026, [https://www.inma.org/blogs/media-leaders/post.cfm/media-time-is-considered-a-valuable-kpi-but-quality-of-content-also-matters](https://www.inma.org/blogs/media-leaders/post.cfm/media-time-is-considered-a-valuable-kpi-but-quality-of-content-also-matters)  
4. Social media, AI, and the rise of extremism during intergroup conflict \- Frontiers, consulté le janvier 1, 2026, [https://www.frontiersin.org/journals/social-psychology/articles/10.3389/frsps.2025.1711791/full](https://www.frontiersin.org/journals/social-psychology/articles/10.3389/frsps.2025.1711791/full)  
5. The Link between Misinformation and Radicalisation: \- Perspectives on Terrorism, consulté le janvier 1, 2026, [https://pt.icct.nl/sites/default/files/2023-03/PT%20Vol%20XVII%2C%20I%20March%202023%20RN1%20ep\_0.pdf](https://pt.icct.nl/sites/default/files/2023-03/PT%20Vol%20XVII%2C%20I%20March%202023%20RN1%20ep_0.pdf)  
6. GUIDELINES ON DATA QUALITY ASSESSMENT \- Irclass.org, consulté le janvier 1, 2026, [https://www.irclass.org/media/8031/guidelines-on-data-quality-assessment\_sept-2025\_new.pdf](https://www.irclass.org/media/8031/guidelines-on-data-quality-assessment_sept-2025_new.pdf)  
7. The data quality management system (ISO8000) | RMG, consulté le janvier 1, 2026, [https://www.rmg-sa.com/en/the-data-quality-management-system-iso8000/](https://www.rmg-sa.com/en/the-data-quality-management-system-iso8000/)  
8. DAQUA-MASS: An ISO 8000-61 Based Data Quality Management Methodology for Sensor Data \- MDPI, consulté le janvier 1, 2026, [https://www.mdpi.com/1424-8220/18/9/3105](https://www.mdpi.com/1424-8220/18/9/3105)  
9. ISO 8000 and Data Extraction \- Building Reliable Automation With Data Quality Standards \- Parseur, consulté le janvier 1, 2026, [https://parseur.com/blog/iso-8000](https://parseur.com/blog/iso-8000)  
10. CEN WORKSHOP AGREEMENT CWA 17493 \- CEN-CENELEC, consulté le janvier 1, 2026, [https://www.cencenelec.eu/media/CEN-CENELEC/CWAs/ICT/cwa17493.pdf](https://www.cencenelec.eu/media/CEN-CENELEC/CWAs/ICT/cwa17493.pdf)  
11. About JTI \- Journalism Trust Initiative, consulté le janvier 1, 2026, [https://journalismtrustinitiative.org/about-jti/](https://journalismtrustinitiative.org/about-jti/)  
12. JTI CWA 17493 \- JTI App, consulté le janvier 1, 2026, [https://www.jti-app.com/footer/cwa](https://www.jti-app.com/footer/cwa)  
13. CWA No. 17493 The JTI Standard – Clauses \- Trebinje \- Direkt portal, consulté le janvier 1, 2026, [https://direkt-portal.com/wp-content/uploads/2025/08/Direkt-2.pdf](https://direkt-portal.com/wp-content/uploads/2025/08/Direkt-2.pdf)  
14. IFCN Fact-Checkers' Code of Principles Signatory \- Credly, consulté le janvier 1, 2026, [https://www.credly.com/org/ifcn/badge/ifcn-fact-checkers-code-of-principles-signatory](https://www.credly.com/org/ifcn/badge/ifcn-fact-checkers-code-of-principles-signatory)  
15. International Fact-Checking Network fact-checkers' code of principles, consulté le janvier 1, 2026, [https://accountablejournalism.org/ethics-codes/international-fact-checking-network-fact-checkers-code-of-principles](https://accountablejournalism.org/ethics-codes/international-fact-checking-network-fact-checkers-code-of-principles)  
16. Code of Principles \- FactCheckNI, consulté le janvier 1, 2026, [https://factcheckni.org/about-us/code-of-principles/](https://factcheckni.org/about-us/code-of-principles/)  
17. C2PA | Verifying Media Content Sources, consulté le janvier 1, 2026, [https://c2pa.org/](https://c2pa.org/)  
18. C2PA: Overview, consulté le janvier 1, 2026, [https://spec.c2pa.org/](https://spec.c2pa.org/)  
19. Evaluating Web Content Using the W3C Credibility Signals, consulté le janvier 1, 2026, [https://www.dfki.de/fileadmin/user\_upload/import/12708\_SSW-55-SSW220005.pdf](https://www.dfki.de/fileadmin/user_upload/import/12708_SSW-55-SSW220005.pdf)  
20. Credibility Signals, consulté le janvier 1, 2026, [https://credweb.org/signals-20191126](https://credweb.org/signals-20191126)  
21. Insights into Coalition for Content Provenance and Authenticity (C2PA) \- Infosys, consulté le janvier 1, 2026, [https://www.infosys.com/iki/techcompass/content-provenance-authenticity.html](https://www.infosys.com/iki/techcompass/content-provenance-authenticity.html)  
22. Integrity in the CIA triad: Truth Enforcer and the ISO 27001 standard \- Connecting Software, consulté le janvier 1, 2026, [https://www.connecting-software.com/blog/integrity-in-the-cia-triad-and-iso-27001-standard/](https://www.connecting-software.com/blog/integrity-in-the-cia-triad-and-iso-27001-standard/)  
23. Source Verification: Best Tools & Practices for Journalists \- Yellowbrick, consulté le janvier 1, 2026, [https://www.yellowbrick.co/blog/journalism/source-verification-best-tools-practices-for-journalists](https://www.yellowbrick.co/blog/journalism/source-verification-best-tools-practices-for-journalists)  
24. ISO 10002 (Guidelines for Complaints Handling in Organizations) \- Quality Austria, consulté le janvier 1, 2026, [https://www.qualityaustria.com/en/product-groups/quality/iso-10002-guidelines-for-complaints-handling-in-organizations/](https://www.qualityaustria.com/en/product-groups/quality/iso-10002-guidelines-for-complaints-handling-in-organizations/)  
25. ISO 10002 \- International Accreditation Council (IAC), consulté le janvier 1, 2026, [https://iacouncil.org/iso-10002/](https://iacouncil.org/iso-10002/)  
26. ISO Audit: what it is and why it's important \- DNV, consulté le janvier 1, 2026, [https://www.dnv.com/assurance/articles/what-is-an-iso-audit/](https://www.dnv.com/assurance/articles/what-is-an-iso-audit/)  
27. Welcome to the Media and Information Literacy e-Platform \- unesco, consulté le janvier 1, 2026, [https://www.unesco.org/mil4teachers/en](https://www.unesco.org/mil4teachers/en)  
28. UNESCO Media and Information Literacy Framework, consulté le janvier 1, 2026, [https://www.unesco.gov.ph/wp-content/uploads/2020/03/UNESCO-Media-and-Information-Literacy-Framework-and-Recent-Initiatives.pdf](https://www.unesco.gov.ph/wp-content/uploads/2020/03/UNESCO-Media-and-Information-Literacy-Framework-and-Recent-Initiatives.pdf)  
29. IEEE Provenance \- Global Indigenous Data Alliance, consulté le janvier 1, 2026, [https://www.gida-global.org/ieee-provenance](https://www.gida-global.org/ieee-provenance)  
30. ISO 8000-61 DATA QUALITY MANAGEMENT STANDARD, TDQM ..., consulté le janvier 1, 2026, [https://ualr.edu/informationquality/wp-content/uploads/sites/103/2023/02/P23-ICIQ2017-ISO8000-61-DQ-Standard.pdf](https://ualr.edu/informationquality/wp-content/uploads/sites/103/2023/02/P23-ICIQ2017-ISO8000-61-DQ-Standard.pdf)  
31. ISO 21001:2018 – Educational organizations – Management systems for educational organizations – Requirements with guidance for use \- PECB, consulté le janvier 1, 2026, [https://pecb.com/en/whitepaper/iso-210012018-educational-organizations-management-systems-for-educational-organizations-requirements-with-guidance-for-use](https://pecb.com/en/whitepaper/iso-210012018-educational-organizations-management-systems-for-educational-organizations-requirements-with-guidance-for-use)