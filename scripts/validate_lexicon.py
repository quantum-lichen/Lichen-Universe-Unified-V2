import os
import re

# 🛑 LES MOTS INTERDITS (L'ANCIEN MONDE)
# Format: "Terme interdit": "Correction suggérée"
FORBIDDEN_TERMS = {
    r'\bMicrokernel\b': "Lichen μ-Kernel",
    r'\bFC496\b': "FC-496",
    r'\bCell-496\b': "FC-496",
    r'\bPhi-Compiler\b': "φ-Compiler",
    r'\bH\(s\)': "S(s) (pour Entropie)",
    r'\bH_score\b': "ℋ (pour Harmonie)",
    r'\bGenesis QC\b': "GENESIS QC (Majuscules)",
    r'H =': "Attention: Vérifier si c'est S, ℋ ou Û"
}

def scan_file(filepath):
    """Scanne un fichier pour trouver des hérésies lexicale."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.readlines()

    errors_found = False
    for line_num, line in enumerate(content):
        for pattern, suggestion in FORBIDDEN_TERMS.items():
            if re.search(pattern, line):
                # Ignore le fichier LEXIQUE lui-même ou le script
                if "LEXIQUE.md" in filepath or "validate_lexicon.py" in filepath:
                    continue
                    
                print(f"❌ [Ligne {line_num+1}] dans {filepath}")
                print(f"   Trouvé: '{pattern.replace(r'\\b', '')}'")
                print(f"   👉 Utiliser: {suggestion}\n")
                errors_found = True
    return errors_found

def main():
    print("🛡️  LICHEN LEXICON VALIDATOR - STARTING SCAN...\n")
    root_dir = "."  # Racine du repo
    
    violation_count = 0
    
    for dirpath, _, filenames in os.walk(root_dir):
        # On ignore le dossier .git
        if ".git" in dirpath:
            continue
            
        for filename in filenames:
            if filename.endswith(".md"):
                full_path = os.path.join(dirpath, filename)
                if scan_file(full_path):
                    violation_count += 1

    if violation_count == 0:
        print("✅ SUCCÈS : Aucun terme interdit trouvé. Le Lexique est respecté.")
    else:
        print(f"⚠️  ATTENTION : {violation_count} fichiers contiennent des termes obsolètes.")

if __name__ == "__main__":
    main()
