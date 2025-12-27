import streamlit as st
import mmap
import struct
import os
import time
import random
from datetime import datetime

# ==============================================================================
# CONFIGURATION ZPA (Zero-Parse Architecture)
# ==============================================================================
# Structure binaire alignée pour haute performance :
# [Timestamp (8B)] + [Score/Poids (4B)] + [Vecteur 4D (16B)] + [Payload (256B)]
# Total par enregistrement : 284 bytes fixes.
VECTOR_DIM = 4 
TEXT_MAX_LEN = 256
STRUCT_FMT = f"Qf{VECTOR_DIM}f{TEXT_MAX_LEN}s"
STRUCT_SIZE = struct.calcsize(STRUCT_FMT)
DB_FILE = "zpa_vector_store.bin"

st.set_page_config(
    page_title="ZPA Vector Store",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# MOTEUR ZPA (BACKEND)
# ==============================================================================

class ZPACompiler:
    """
    Module d'écriture (Ingestion).
    Transforme des objets Python en structure binaire contiguë (Zero-Copy ready).
    """
    @staticmethod
    def write_batch(data_batch, output_file):
        start = time.perf_counter()
        
        # Mode wb (Write Binary)
        with open(output_file, "wb") as f:
            # HEADER: Nombre d'enregistrements (8 bytes unsigned long long)
            f.write(struct.pack("Q", len(data_batch)))
            
            for item in data_batch:
                # 1. Padding du texte pour atteindre exactement 256 bytes
                text_bytes = item['payload'].encode('utf-8')[:TEXT_MAX_LEN].ljust(TEXT_MAX_LEN, b'\x00')
                
                # 2. Packing structuré (C-style struct)
                packed = struct.pack(STRUCT_FMT, 
                                     item['timestamp'], 
                                     item['score'], 
                                     *item['vector'], 
                                     text_bytes)
                f.write(packed)
                
        end = time.perf_counter()
        return {
            "duration": (end - start) * 1000, # ms
            "size": os.path.getsize(output_file),
            "count": len(data_batch)
        }

class ZPARuntime:
    """
    Module de lecture (Query).
    Utilise MMAP pour mapper le fichier disque directement en RAM virtuelle.
    Aucun parsing, aucune désérialisation JSON.
    """
    def __init__(self, db_file):
        if not os.path.exists(db_file):
            raise FileNotFoundError("Base de données introuvable.")
        
        self.f = open(db_file, "r+b")
        # MMAP: Mapping direct du descripteur de fichier
        self.mm = mmap.mmap(self.f.fileno(), 0)
    
    def count(self):
        # Lecture directe des 8 premiers octets (Header)
        return struct.unpack_from("Q", self.mm, 0)[0]
    
    def fetch(self, index):
        """ Accès O(1) par arithmétique de pointeur """
        total = self.count()
        if index >= total: raise IndexError("Index hors limites.")
        
        # Calcul de l'offset mémoire
        offset = 8 + (index * STRUCT_SIZE)
        
        # Lecture brute (Slicing mémoire)
        data = self.mm[offset : offset + STRUCT_SIZE]
        unpacked = struct.unpack(STRUCT_FMT, data)
        
        # Mapping vers objet pour affichage UI
        # Note: Dans un usage pur backend, on utiliserait directement les bytes
        timestamp = unpacked[0]
        score = unpacked[1]
        vector = list(unpacked[2 : 2 + VECTOR_DIM]) 
        text_raw = unpacked[2 + VECTOR_DIM]         
        
        # Retrait du padding (Null bytes)
        payload = text_raw.decode('utf-8', errors='ignore').rstrip('\x00')
        
        return {
            "timestamp": timestamp,
            "datetime": datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S.%f'),
            "score": score,
            "vector": vector,
            "payload": payload
        }

    def close(self):
        if not self.mm.closed: self.mm.close()
        if not self.f.closed: self.f.close()

# ==============================================================================
# INTERFACE UTILISATEUR (DASHBOARD TECHNIQUE)
# ==============================================================================

# --- SIDEBAR ---
with st.sidebar:
    st.title("⚡ ZPA Engine")
    st.markdown("---")
    st.caption("Version: **2.1.0-Core**")
    st.caption("Mode: **High-Performance**")
    
    st.markdown("### ⚙️ Operations")
    if st.button("🔴 Purge Database", type="primary"):
        if os.path.exists(DB_FILE):
            os.remove(DB_FILE)
            st.rerun()

# --- HEADER ---
st.title("High-Performance Vector Storage")
st.markdown("""
**Démonstration technique de l'Architecture Zero-Parse.**
Ce système stocke des vecteurs et des logs structurés sans utiliser de format de sérialisation coûteux (JSON/XML).
L'accès aux données se fait par mapping mémoire direct (`mmap`), garantissant une latence minimale.
""")
st.markdown("---")

col_write, col_read = st.columns([1, 1.5])

# --- COLONNE 1 : INGESTION (WRITE) ---
with col_write:
    st.header("1. Ingestion (Write)")
    st.info("Génération et écriture binaire de logs vectoriels.")

    with st.form("ingest_form"):
        batch_size = st.number_input("Taille du Batch", 100, 100000, 1000)
        
        # Simulation de types de logs techniques
        log_types = [
            "SYS_LOG: CPU Usage Spike detected",
            "NET_LOG: API Latency > 200ms",
            "SEC_LOG: Auth Token Validated",
            "DB_LOG: Transaction Commit OK",
            "APP_LOG: Vector Normalized",
            "ERR_LOG: Connection Timeout"
        ]
        
        if st.form_submit_button("⚡ Run Batch Insert"):
            data_buffer = []
            base_time = time.time()
            
            with st.spinner("Processing..."):
                for i in range(batch_size):
                    msg = random.choice(log_types)
                    # Données synthétiques
                    data_buffer.append({
                        "timestamp": int(base_time) - (batch_size - i),
                        "score": random.random(), # Exemple: Confiance ou Priorité
                        "vector": [random.random() for _ in range(VECTOR_DIM)],
                        "payload": f"#{i:06d} | {msg}"
                    })
                
                # APPEL COMPILATEUR ZPA
                compiler = ZPACompiler()
                stats = compiler.write_batch(data_buffer, DB_FILE)
            
            st.success(f"Write Complete: {stats['count']} records")
            col_m1, col_m2 = st.columns(2)
            col_m1.metric("Write Time", f"{stats['duration']:.2f} ms")
            col_m2.metric("File Size", f"{stats['size']/1024:.2f} KB")

# --- COLONNE 2 : REQUÊTE (READ) ---
with col_read:
    st.header("2. Query (Read)")
    
    if not os.path.exists(DB_FILE):
        st.warning("No Database found. Run ingestion first.")
    else:
        try:
            runtime = ZPARuntime(DB_FILE)
            total_records = runtime.count()
            
            st.write(f"📊 Database Status: **Mounted** | Records: **{total_records:,}**")
            
            # ACCÈS ALÉATOIRE
            st.markdown("### Random Access Inspector")
            record_idx = st.slider("Pointer Offset", 0, total_records-1, total_records-1)
            
            # MESURE DE PERFORMANCE
            t0 = time.perf_counter()
            record = runtime.fetch(record_idx)
            t1 = time.perf_counter()
            latency = (t1 - t0) * 1_000_000 # Microsecondes
            
            # VISUALISATION TECHNIQUE
            st.markdown(f"**Record #{record_idx}**")
            
            # 1. Métriques Clés
            c1, c2, c3 = st.columns(3)
            c1.metric("Read Latency", f"{latency:.2f} µs")
            c2.metric("Timestamp", record['datetime'].split(' ')[1])
            c3.metric("Score/Weight", f"{record['score']:.4f}")
            
            # 2. Payload
            st.code(record['payload'], language="text")
            
            # 3. Données Vectorielles
            st.markdown("###### Vector Data (Embedding)")
            st.bar_chart(record['vector'], height=120)
            
            # 4. Inspection Binaire (Preuve de concept)
            with st.expander("Hexdump Inspection (Raw Bytes)"):
                offset = 8 + (record_idx * STRUCT_SIZE)
                raw_bytes = runtime.mm[offset : offset + STRUCT_SIZE]
                st.caption(f"Memory Offset: {hex(offset)}")
                st.code(raw_bytes.hex(), language="text")

            runtime.close()
            
        except Exception as e:
            st.error(f"Runtime Error: {e}")

# --- FOOTER ---
st.markdown("---")
st.caption("System Architecture: **Zero-Parse / Mapped Memory**")
