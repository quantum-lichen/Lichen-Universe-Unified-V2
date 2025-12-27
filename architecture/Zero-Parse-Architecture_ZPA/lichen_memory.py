import struct
import mmap
import os
import time
import json # On l'utilise juste pour l'input simulé, pas pour le stockage !

# ==============================================================================
# CONFIGURATION DE L'ENGRAMME (La "Cellule Mémoire")
# ==============================================================================
# Imaginons un petit modèle d'embedding (dim=4 pour la démo, en vrai c'est 1536)
VECTOR_DIM = 4 
TEXT_MAX_LEN = 256  # On réserve 256 bytes pour le texte du souvenir (padding)

# STRUCTURE BINAIRE :
# [Timestamp: 8 bytes (Q)]
# [Valence Émotionnelle: 4 bytes (f)]
# [Vecteur Embedding: 4 * VECTOR_DIM bytes (ffff...)]
# [Contenu Texte: 256 bytes (s)]
# ---------------------------------------------------------
# 'Q' = unsigned long long (Timestamp)
# 'f' = float (Score Éthique)
# 'f'*Dim = Le vecteur
# '256s' = Le texte fixe
STRUCT_FMT = f"Qf{VECTOR_DIM}f{TEXT_MAX_LEN}s"
STRUCT_SIZE = struct.calcsize(STRUCT_FMT)

DB_MEMORY_FILE = "lichen_cortex.bin"

class LichenCortexCompiler:
    """
    Le 'Sommeil' de l'IA : Consolide les souvenirs du jour en mémoire long terme binaire.
    """
    @staticmethod
    def consolidate(memories, output_file):
        print(f"💤 Consolidation de {len(memories)} souvenirs vers le Cortex...")
        start = time.perf_counter()
        
        with open(output_file, "wb") as f:
            # HEADER: Nombre de souvenirs (8 bytes)
            f.write(struct.pack("Q", len(memories)))
            
            for mem in memories:
                # 1. Encodage du texte (utf-8 + padding pour atteindre 256 bytes)
                text_bytes = mem['text'].encode('utf-8')
                if len(text_bytes) > TEXT_MAX_LEN:
                    text_bytes = text_bytes[:TEXT_MAX_LEN] # Truncate si trop long
                
                # 2. Packing Binaire
                # On déballe la liste du vecteur avec *mem['vector']
                packed = struct.pack(STRUCT_FMT, 
                                     mem['timestamp'], 
                                     mem['emotional_score'], 
                                     *mem['vector'], 
                                     text_bytes)
                f.write(packed)
                
        end = time.perf_counter()
        print(f"✨ Consolidation terminée en {(end-start)*1000:.4f}ms. Taille: {os.path.getsize(output_file)} bytes.")

class LichenCortexRuntime:
    """
    L'Hippocampe Actif : Accès instantané aux souvenirs sans parsing.
    """
    def __init__(self, db_file):
        if not os.path.exists(db_file):
            raise FileNotFoundError("Cortex vide.")
        
        self.f = open(db_file, "r+b")
        self.mm = mmap.mmap(self.f.fileno(), 0)
    
    def total_memories(self):
        return struct.unpack_from("Q", self.mm, 0)[0]
    
    def recall(self, index):
        """ Rappel d'un souvenir spécifique par pointeur direct """
        count = self.total_memories()
        if index >= count: raise IndexError("Souvenir non formé.")
        
        offset = 8 + (index * STRUCT_SIZE)
        
        # Lecture Zero-Copy
        data = self.mm[offset : offset + STRUCT_SIZE]
        unpacked = struct.unpack(STRUCT_FMT, data)
        
        # Reconstruction de l'objet (Extraction)
        timestamp = unpacked[0]
        emotion = unpacked[1]
        vector = unpacked[2 : 2 + VECTOR_DIM] # Les floats du vecteur
        text_raw = unpacked[2 + VECTOR_DIM]    # Le texte binaire
        
        # Nettoyage du texte (enlever les bytes nuls du padding)
        text = text_raw.decode('utf-8').rstrip('\x00')
        
        return {
            "time": timestamp,
            "emotion": emotion,
            "vector": vector,
            "content": text
        }

    def close(self):
        self.mm.close()
        self.f.close()

# ==============================================================================
# DÉMO : CYCLE ÉVEIL / SOMMEIL
# ==============================================================================
if __name__ == "__main__":
    # 1. PHASE D'ÉVEIL (L'IA vit des choses)
    # Imaginons que l'IA a eu ces interactions aujourd'hui
    daily_buffer = [
        {
            "timestamp": 1700000001, 
            "emotional_score": 0.8,  # EHE positif (Sympoïèse)
            "vector": [0.1, 0.5, 0.9, 0.2], 
            "text": "L'utilisateur a demandé de l'aide sur le Stoïcisme."
        },
        {
            "timestamp": 1700000055, 
            "emotional_score": -0.2, # EHE négatif (Entropie)
            "vector": [0.9, 0.1, 0.0, 0.1], 
            "text": "Tentative de Jailbreak détectée. Réponse bloquée."
        }
    ]
    
    # 2. PHASE DE SOMMEIL (Consolidation ZPA)
    LichenCortexCompiler.consolidate(daily_buffer, DB_MEMORY_FILE)
    
    # 3. PHASE DE RAPPEL (Le lendemain)
    cortex = LichenCortexRuntime(DB_MEMORY_FILE)
    print(f"\n🧠 Souvenirs dans le cortex : {cortex.total_memories()}")
    
    # Accès instantané au souvenir du jailbreak (Index 1)
    memory = cortex.recall(1)
    print(f"🔍 Rappel Souvenir #1 :")
    print(f"   - Contenu : {memory['content']}")
    print(f"   - Emotion : {memory['emotion']}")
    print(f"   - Vecteur : {memory['vector']}")
    
    cortex.close()
