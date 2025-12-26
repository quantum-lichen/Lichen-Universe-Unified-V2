import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuration de la page Streamlit
st.set_page_config(page_title="Mandala 496", layout="centered")

st.title("🌌 Mandala 496 (E8×E8)")
st.write("Visualisation basée sur les constantes φ et π.")

# Constantes mathématiques
phi = (1 + np.sqrt(5)) / 2  # Nombre d'or
pi = np.pi  # Pi

def generate_496_mandala():
    """
    Génère un mandala basé sur 496 points avec des proportions φ et des angles π.
    """
    # Configuration du mandala
    outer_radius = 306  # Rayon externe (payload)
    inner_radius = 190  # Rayon interne (header)
    ratio = outer_radius / inner_radius  # Ratio ≈ φ

    # Angles pour 496 points (E8×E8)
    angles = np.linspace(0, 2 * pi, 496, endpoint=False)

    # Initialisation de la figure
    # Note: On crée fig et ax explicitement pour Streamlit
    fig, ax = plt.subplots(figsize=(12, 12), facecolor='black')
    ax.set_facecolor('black')
    ax.set_aspect('equal')
    ax.axis('off')

    # Cercle externe (306 bits)
    outer_circle = plt.Circle((0, 0), outer_radius, color='gold', fill=False, linewidth=2, alpha=0.7)
    ax.add_artist(outer_circle)

    # Cercle interne (190 bits)
    inner_circle = plt.Circle((0, 0), inner_radius, color='silver', fill=False, linewidth=2, alpha=0.7)
    ax.add_artist(inner_circle)

    # Points du mandala (496 points)
    for i in range(496):
        angle = angles[i]
        radius = outer_radius if i % 2 == 0 else inner_radius
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)

        # Couleur des points (alternance doré et argenté)
        color = 'gold' if i % 2 == 0 else 'silver'
        ax.scatter(x, y, color=color, s=10, alpha=0.8)

    # Ajouter des motifs liés à φ et π
    for i in range(5):  # 5 motifs (liés au pentagone et φ)
        angle = 2 * pi * i / 5
        x = outer_radius * np.cos(angle)
        y = outer_radius * np.sin(angle)
        ax.scatter(x, y, color='red', s=50, alpha=0.9, marker='o')

    # Titre et légende (directement sur le plot)
    ax.set_title(f"Mandala 496 (E8×E8, φ, π)\nRatio: {ratio:.3f}", color='white', fontsize=14)
    plt.figtext(0.5, 0.1, f"φ ≈ {phi:.5f}, π ≈ {pi:.5f}", color='white', ha='center', fontsize=10)

    # AFFICHAGE STREAMLIT (Au lieu de plt.show)
    st.pyplot(fig)

# Générer le mandala
if st.button('Générer le Mandala'):
    generate_496_mandala()
else:
    generate_496_mandala() # Générer au chargement par défaut
