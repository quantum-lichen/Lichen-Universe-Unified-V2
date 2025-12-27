import mmap
import struct
import os
import time
from abc import ABC, abstractmethod

# ==============================================================================
# CONFIGURATION ET FORMATS
# ==============================================================================
# Définition de notre structure binaire "Transaction" pour l'Isomorphisme.
# Format:[Montant: 8 bytes]
# 'Q' = unsigned long long (8 bytes), 'd' = double (8 bytes)
STRUCT_FMT = "QdQ" 
STRUCT_SIZE = struct.calcsize(STRUCT_FMT)
DB_FILENAME = "zeroparse_storage.db"

# ==============================================================================
# COMPILER / ENCODER (Le Créateur)
# ==============================================================================
class ZeroParseCompiler:
    """
    Simule la phase d'édition/création. 
    Transforme des données 'humaines' en un blob binaire isomorphe à la RAM.
    Dans une vraie ZPA, ceci serait fait par un éditeur projectionnel.
    """
    @staticmethod
    def compile(data_list, output_file):
        print(f"\n[Compiler] 🔨 Compilation de {len(data_list)} enregistrements vers '{output_file}'...")
        start_time = time.time()
        
        with open(output_file, "wb") as f:
            # HEADER: Nombre d'éléments (8 bytes)
            f.write(struct.pack("Q", len(data_list)))
            
            # BODY: Données contiguës (Array-of-Structs)
            for item in data_list:
                # Sérialisation native. Aucune métadonnée JSON, aucun séparateur.
                # C'est une copie exacte de ce à quoi la struct ressemblerait en C/C++.
                packed_data = struct.pack(STRUCT_FMT, item['id'], item['amount'], item['timestamp'])
                f.write(packed_data)
                
        end_time = time.time()
        print(f"[Compiler] ✅ Terminé en {(end_time - start_time)*1000:.4f}ms.")
        print(f"[Compiler] Taille du fichier généré : {os.path.getsize(output_file)} bytes.")

# ==============================================================================
# DECODER / RUNTIME (L'Utilisateur Zero-Copy)
# ==============================================================================
class ZeroParseRuntime:
    """
    Le Runtime qui n'effectue AUCUN parsing.
    Il utilise MMAP pour accéder au disque comme si c'était de la RAM.
    """
    def __init__(self, db_file):
        if not os.path.exists(db_file):
            raise FileNotFoundError(f"Base de données '{db_file}' introuvable.")
            
        self.f = open(db_file, "r+b")
        # MMAP: Projection du fichier en mémoire. 
        # C'est l'équivalent de charger tout le fichier sans le lire physiquement.
        self.mm = mmap.mmap(self.f.fileno(), 0)
        self.base_addr = id(self.mm)
        print(f"\n 🚀 Base de données mappée. Adresse Virtuelle: {hex(self.base_addr)}")
        
    def get_total_count(self):
        # Lecture directe des 8 premiers octets (Header)
        # O(1) - Pas de scan
        return struct.unpack_from("Q", self.mm, 0)
        
    def get_record(self, index):
        """
        ACCÈS O(1) - FORMULE MATHÉMATIQUE
        Pas de boucle 'for', pas de 'split', pas de 'json.loads'.
        Juste des mathématiques de pointeurs.
        """
        count = self.get_total_count()
        if index >= count or index < 0:
            raise IndexError("Index hors limites")
            
        # Formule de l'offset (voir formulas.md)
        # Offset = Taille_Header + (Index * Taille_Struct)
        offset = 8 + (index * STRUCT_SIZE)
        
        # Simulation de l'accès pointeur (Casting)
        # En C/Rust, ce serait: Transaction* t = (Transaction*)(base_ptr + offset);
        # Ici en Python, on lit directement la plage mémoire.
        record_bytes = self.mm
        unpacked = struct.unpack(STRUCT_FMT, record_bytes)
        
        return {
            "id": unpacked,
            "amount": unpacked[2],
            "timestamp": unpacked[3]
        }
        
    def close(self):
        self.mm.close()
        self.f.close()
        print(" Fermeture du mapping.")

# ==============================================================================
# DÉMONSTRATION
# ==============================================================================
if __name__ == "__main__":
    # 1. Données brutes (Source)
    raw_data = [
        {"id": 101, "amount": 250.50, "timestamp": 1678880000},
        {"id": 102, "amount": 99.99, "timestamp": 1678880005},
        {"id": 103, "amount": 1200.00, "timestamp": 1678880010},
        {"id": 104, "amount": 5.75, "timestamp": 1678880015},
    ]
    
    # 2. Compilation (Écriture Isomorphe)
    compiler = ZeroParseCompiler()
    compiler.compile(raw_data, DB_FILENAME)
    
    # 3. Runtime (Lecture Zero-Parse)
    runtime = ZeroParseRuntime(DB_FILENAME)
    
    try:
        total = runtime.get_total_count()
        print(f"[App] Le Runtime voit {total} enregistrements.")
        
        # Accès aléatoire au dernier élément (instantané)
        idx_to_fetch = 3
        print(f"[App] Accès direct à l'index {idx_to_fetch}...")
        
        start_read = time.perf_counter()
        record = runtime.get_record(idx_to_fetch)
        end_read = time.perf_counter()
        
        print(f"[App] Résultat: ID={record['id']}, Amount={record['amount']}")
        print(f"[App] Temps d'accès (latence): {(end_read - start_read)*1_000_000:.2f} microsecondes")
        
        print("\n[App] Conclusion: Le 'parser' n'a jamais été appelé lors de la lecture.")
        
    finally:
        runtime.close()
        # Nettoyage
        if os.path.exists(DB_FILENAME):
            os.remove(DB_FILENAME)
