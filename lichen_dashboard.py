import streamlit as st
import requests

st.title("🕵️‍♂️ Détective de Connexion")

# L'URL exacte qu'on essaie de joindre
url = "https://raw.githubusercontent.com/quantum-lichen/Lichen-Universe-Unified-V2/main/manifest.json"

st.write(f"**Cible :** `{url}`")

try:
    # On essaie de lire le fichier brut
    response = requests.get(url)
    
    st.write(f"**Code Réponse :** `{response.status_code}`")
    
    if response.status_code == 200:
        st.success("✅ CONNEXION RÉUSSIE ! Le fichier est accessible.")
        st.text("Voici les 500 premiers caractères du fichier :")
        st.code(response.text[:500])
        
        # Test de lecture JSON
        try:
            data = response.json()
            st.success("✅ JSON VALIDE ! Structure comprise.")
            st.write(f"Projet détecté : **{data.get('project', {}).get('name', 'Inconnu')}**")
        except Exception as e:
            st.error(f"❌ Erreur de lecture JSON : {e}")
            st.warning("Le fichier existe mais contient peut-être une erreur de syntaxe.")
            
    elif response.status_code == 404:
        st.error("❌ ERREUR 404 : Fichier non trouvé.")
        st.write("Causes possibles :")
        st.write("1. Le fichier s'appelle 'Manifest.json' (Majuscule?) au lieu de 'manifest.json' ?")
        st.write("2. Le dépôt est-il 'Private' ? (Streamlit ne peut pas lire les repos privés sans token)")
        
    else:
        st.error(f"❌ Erreur bizarre : {response.status_code}")

except Exception as e:
    st.error(f"💥 Crash complet : {e}")
