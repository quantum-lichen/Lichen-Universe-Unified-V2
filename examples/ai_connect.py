"""
🤖 LICHEN AI CONNECTOR
Exemple de code montrant comment une IA (ou un script) peut se connecter
au Cerveau Lichen via le Manifeste V2.1.
"""

import requests
import json

# L'URL Magique (Le Hack GitHub Pages)
MANIFEST_URL = "https://quantum-lichen.github.io/Lichen-Universe-Unified/manifest.json"

def connect_to_hive_mind():
    print(f"📡 Connexion au Manifeste Lichen : {MANIFEST_URL}...")
    
    try:
        response = requests.get(MANIFEST_URL)
        if response.status_code != 200:
            print("❌ Erreur de connexion.")
            return
        
        manifest = response.json()
        print("✅ Connexion réussie ! Cerveau chargé.\n")
        
        # 1. LIRE LES LOIS PHYSIQUES (Constantes)
        print("--- [1] CHARGEMENT DES CONSTANTES ---")
        phi = manifest['constants']['phi']
        print(f"🌀 {phi['name']} ({phi['symbol']}) = {phi['mathematical_expression']['unicode']}")
        print(f"   Usage : {phi['usage']}")

        # 2. PARSER UNE FORMULE (MathJSON)
        print("\n--- [2] DÉCODAGE CEML (MathJSON) ---")
        ceml = next(t for t in manifest['theories'] if t['name'] == 'CEML')
        math_structure = ceml['mathematical_expression']['primary_formula']['mathjson']
        
        print(f"Théorie : {ceml['full_name']}")
        print(f"Formule (Unicode) : {ceml['mathematical_expression']['primary_formula']['unicode']}")
        print(f"Structure Logicielle : {json.dumps(math_structure)}")
        print("👉 Une IA peut maintenant calculer ce score sans ambiguïté.")

        # 3. RÉSOUDRE LES DÉPENDANCES
        print("\n--- [3] ARBRE DE DÉPENDANCE (Lichen OS) ---")
        graph = manifest['dependency_graph']
        
        # Trouver ce dont Lichen OS a besoin
        dependencies = []
        for edge in graph['edges']:
            if edge['from'] == 'lichen-os':
                dependencies.append(edge['to'])
        
        print(f"Lichen OS dépend de : {', '.join(dependencies)}")
        print("(L'IA sait qu'elle doit charger UHFS et FC-496 avant de compiler l'OS)")

    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    connect_to_hive_mind()
