# Cool-Flow™ Fractal Cooling System
**Technologie :** Microfluidique Active Péristaltique
**Architecture :** Réseau Vasculaire Fractal (Loi de Murray)

---

## 1. Le Principe Biomimétique
La nature n'utilise pas de radiateurs. Elle utilise des réseaux vasculaires.
Pour le FC-496, nous appliquons la **Loi de Murray** ($r_p^3 = r_{d1}^3 + r_{d2}^3$) qui garantit que le flux sanguin (ou liquide de refroidissement) circule avec une résistance minimale à chaque bifurcation.

## 2. Architecture des Canaux (Gravure DRIE)

### Niveau 1 : L'Artère Principale (The Aorta)
* **Diamètre :** 500 µm
* **Flux :** Turbulent (Haut débit)
* **Rôle :** Amener le fluide diélectrique (Novec 7100) froid au centre de la pyramide.

### Niveau 2 : Les Capillaires Fractals (The Mesh)
* **Diamètre :** 50 µm -> 10 µm (Fractale)
* **Flux :** Laminaire (Échange thermique maximal)
* **Surface d'échange :** Le réseau fractal multiplie la surface de contact par **183,000**.
* **Matériau :** Silicium poreux recouvert de graphène.

## 3. L'Actuation Active (PZT)
Il n'y a pas de pompe externe massive. Le processeur **est** la pompe.

* **Parois Actives :** Les parois des canaux sont dopées au PZT (Titano-Zirconate de Plomb).
* **Fréquence de Pompage :** 20 kHz (Ultrasons).
* **Logique :** * Zone Froide = Parois inertes.
    * Zone Chaude (Calcul intensif) = Parois vibrent -> Flux accéléré localement.

## 4. Spécifications du Fluide
* **Type :** 3M™ Novec™ 7100 Engineered Fluid.
* **Propriété :** Diélectrique (non-conducteur), boue à 61°C (Changement de phase liquide -> gaz possible en cas d'urgence thermique).
