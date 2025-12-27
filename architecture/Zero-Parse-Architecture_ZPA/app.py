import streamlit as st
import mmap
import struct
import os
import time
import random

# ==============================================================================
# CONFIGURATION ET FORMATS
# ==============================================================================
# Format: [ID: 8 bytes (Q)], [Montant: 8 bytes (d)], [Timestamp: 8 bytes (Q)]
STRUCT_FMT = "QdQ" 
STRUCT_SIZE = struct.calcsize(STRUCT_FMT)
DB_FILENAME = "zeroparse_storage.db"

# Configuration de la page Streamlit
st.set_page_config(
    page_title="ZeroParse Demo",
    page_icon="🚀",
    layout="wide"
)

# ==============================================================================
# CLASSES BACKEND (Logique pure)
# ==============================================================================

class ZeroParseCompiler:
    """
    Transforme des données en un blob binaire isomorphe à la RAM.
    """
    @staticmethod
    def compile(data_list, output_file):
        start_time = time.time()
        
        with open(output_file, "wb") as f:
            # HEADER: Nombre d'éléments (8 bytes)
            f.write(struct.pack("Q", len(data_list)))
            
            # BODY: Données contiguës
            for item in data_list:
                packed_data = struct.pack(STRUCT_FMT, item['id'], item['amount'], item['timestamp'])
                f.write(packed_data)
                
        end_time = time.time()
        return {
            "duration": (end_time - start_time) * 1000, # ms
            "size": os.path.getsize(output_file),
            "count": len(data_list)
        }

class ZeroParseRuntime:
    """
    Runtime Zero-Copy via MMAP.
    """
    def __init__(self, db_file):
        if not os.path.exists(db_file):
            raise FileNotFoundError(f"Base de données '{db_file}' introuvable.")
            
        self.f = open(db_file, "r+b")
        self.mm = mmap.mmap(self.f.fileno(), 0)
        self.base_addr = id(self.mm)
        
    def get_total_count(self):
        # Lecture des 8 premiers octets
        # unpack_from retourne un tuple, on veut le premier élément
        return struct.unpack_from("Q", self.mm, 0)[0]
        
    def get_record(self, index):
        count = self.get_total_count()
        if index >= count or index < 0:
            raise IndexError(f"Index {index} hors limites (Max: {count-1})")
            
        # Offset = Header (8 bytes) + (Index * Taille Struct)
        offset = 8 + (index * STRUCT_SIZE)
        
        # Lecture ciblée via slicing du buffer mmap (Zero-Copy effectif en lecture)
        # Note: struct.unpack demande des bytes, slicing mmap donne des bytes.
        record_bytes = self.mm[offset : offset + STRUCT_SIZE]
        unpacked = struct.unpack(STRUCT_FMT, record_bytes)
        
        # CORRECTION ICI: Q, d, Q donne indices 0, 1, 2
        return {
            "id": unpacked[0],
            "amount": unpacked[1],
            "timestamp": unpacked[2]
        }
        
    def close(self):
        self.mm.close()
        self.f.close()

# ==============================================================================
# INTERFACE STREAMLIT
# ==============================================================================

st.title("🚀 Zero-Parse / Zero-Copy Architecture")
st.markdown("""
Cette application démontre la puissance de l'accès mémoire direct (**mmap**) par rapport au parsing classique.
Les données ne sont pas lues ligne par ligne, mais accédées via des pointeurs mathématiques.
""")

col1, col2 = st.columns(2)

# --- COLONNE 1 : LE CRÉATEUR (COMPILER) ---
with col1:
    st.header("1. Compiler (Écriture)")
    st.info("Simule la création d'une base de données binaire optimisée.")
    
    num_records = st.slider("Nombre d'enregistrements à générer", 10, 1_000_000, 10_000)
    
    if st.button("🔨 Compiler les données"):
        # Génération de fausses données
        with st.spinner("Génération des données en RAM..."):
            raw_data = []
            base_time = int(time.time())
            for i in range(num_records):
                raw_data.append({
                    "id": i,
                    "amount": round(random.uniform(1.0, 9999.99), 2),
                    "timestamp": base_time + i
                })
        
        # Compilation
        compiler = ZeroParseCompiler()
        stats = compiler.compile(raw_data, DB_FILENAME)
        
        st.success("Compilation terminée !")
        
        # Affichage des métriques
        m1, m2, m3 = st.columns(3)
        m1.metric("Enregistrements", f"{stats['count']:,}")
        m2.metric("Temps (ms)", f"{stats['duration']:.2f} ms")
        m3.metric("Taille Fichier", f"{stats['size']/1024/1024:.2f} MB")

# --- COLONNE 2 : L'UTILISATEUR (RUNTIME) ---
with col2:
    st.header("2. Runtime (Lecture)")
    st.info("Accès direct au disque sans parsing JSON/CSV.")
    
    if os.path.exists(DB_FILENAME):
        try:
            # Initialisation du runtime
            runtime = ZeroParseRuntime(DB_FILENAME)
            total_items = runtime.get_total_count()
            
            st.write(f"📂 Base de données chargée. **{total_items:,}** éléments disponibles.")
            st.caption(f"📍 Adresse mémoire virtuelle (MMAP): {hex(runtime.base_addr)}")
            
            # Contrôles de lecture
            search_index = st.number_input("Entrer un Index (ID) à chercher", 
                                         min_value=0, 
                                         max_value=total_items-1 if total_items > 0 else 0,
                                         value=0)
            
            if st.button("⚡ Fetch Record (Zero-Copy)"):
                try:
                    # Mesure précise
                    start_read = time.perf_counter()
                    record = runtime.get_record(int(search_index))
                    end_read = time.perf_counter()
                    
                    latency_us = (end_read - start_read) * 1_000_000
                    
                    # Affichage résultat
                    st.json(record)
                    
                    # Affichage performance
                    st.metric(
                        label="Temps d'accès (Latence)", 
                        value=f"{latency_us:.2f} µs",
                        delta="O(1) Constant Time"
                    )
                    
                    st.success("Le parser n'a jamais été appelé. Données lues directement depuis l'offset binaire.")
                    
                except Exception as e:
                    st.error(f"Erreur: {e}")
            
            # Nettoyage
            runtime.close()
            
        except Exception as e:
            st.error(f"Erreur d'ouverture de la DB: {e}")
            
        # Bouton de reset
        if st.button("🗑️ Supprimer la base de données"):
            if os.path.exists(DB_FILENAME):
                os.remove(DB_FILENAME)
                st.rerun()
    else:
        st.warning("⚠️ Aucune base de données trouvée. Veuillez compiler des données dans la colonne de gauche.")

# --- FOOTER ---
st.markdown("---")
st.markdown("*Architecture inspirée des moteurs de jeux et du trading haute fréquence.*")
