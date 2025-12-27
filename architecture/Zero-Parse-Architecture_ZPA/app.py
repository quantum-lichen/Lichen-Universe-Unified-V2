import streamlit as st
import mmap
import struct
import os
import time
import random
from datetime import datetime

# ==============================================================================
# CONFIGURATION DU CORTEX (Structure de l'Engramme)
# ==============================================================================
# Structure : [Timestamp (8)] + [Score EHE (4)] + [Vecteur 4D (16)] + [Texte (256)]
# Q = unsigned long long (8 bytes)
# f = float (4 bytes)
# 256s = string de 256 bytes
VECTOR_DIM = 4 
TEXT_MAX_LEN = 256
STRUCT_FMT = f"Qf{VECTOR_DIM}f{TEXT_MAX_LEN}s"
STRUCT_SIZE = struct.calcsize(STRUCT_FMT)
CORTEX_FILE = "lichen_cortex.bin"

st.set_page_config(
    page_title="Lichen Cortex ZPA",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# CLASSES DU CORTEX (BACKEND ZPA)
# ==============================================================================

class LichenCortexCompiler:
    """
    Le 'Sommeil' de l'IA : Consolide les souvenirs en mémoire long terme binaire.
    """
    @staticmethod
    def consolidate(memories, output_file):
        start = time.perf_counter()
        
        # Mode "append" (ab) pour ajouter des souvenirs sans écraser l'histoire
        # Note: Pour simplifier la lecture ZPA ici, on va réécrire le fichier complet
        # dans une vraie prod, on ferait de l'append pur.
        with open(output_file, "wb") as f:
            # HEADER: Nombre de souvenirs (8 bytes)
            f.write(struct.pack("Q", len(memories)))
            
            for mem in memories:
                # 1. Encodage du texte (utf-8 + padding pour atteindre 256 bytes exacts)
                # ljust ajoute des bytes nuls (\x00) à la fin pour remplir
                text_bytes = mem['text'].encode('utf-8')[:TEXT_MAX_LEN].ljust(TEXT_MAX_LEN, b'\x00')
                
                # 2. Packing Binaire
                packed = struct.pack(STRUCT_FMT, 
                                     mem['timestamp'], 
                                     mem['emotional_score'], 
                                     *mem['vector'], 
                                     text_bytes)
                f.write(packed)
                
        end = time.perf_counter()
        return {
            "duration": (end - start) * 1000,
            "size": os.path.getsize(output_file),
            "count": len(memories)
        }

class LichenCortexRuntime:
    """
    L'Hippocampe Actif : Accès instantané aux souvenirs sans parsing.
    """
    def __init__(self, db_file):
        if not os.path.exists(db_file):
            raise FileNotFoundError("Cortex vide.")
        
        self.f = open(db_file, "r+b")
        # MMAP: On map tout le fichier en mémoire virtuelle
        self.mm = mmap.mmap(self.f.fileno(), 0)
    
    def total_memories(self):
        # Lecture des 8 premiers octets (Header)
        return struct.unpack_from("Q", self.mm, 0)[0]
    
    def recall(self, index):
        """ Rappel d'un souvenir spécifique par pointeur direct """
        count = self.total_memories()
        if index >= count: raise IndexError("Souvenir non formé.")
        
        # Calcul de l'adresse mémoire exacte
        offset = 8 + (index * STRUCT_SIZE)
        
        # Lecture Zero-Copy (Slicing)
        data = self.mm[offset : offset + STRUCT_SIZE]
        unpacked = struct.unpack(STRUCT_FMT, data)
        
        # Reconstruction de l'objet
        timestamp = unpacked[0]
        emotion = unpacked[1]
        vector = list(unpacked[2 : 2 + VECTOR_DIM]) # Les floats du vecteur
        text_raw = unpacked[2 + VECTOR_DIM]         # Le texte binaire
        
        # Nettoyage du texte (enlever les bytes nuls du padding)
        text = text_raw.decode('utf-8', errors='ignore').rstrip('\x00')
        
        return {
            "timestamp": timestamp,
            "date": datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'),
            "score_ehe": emotion,
            "vector": vector,
            "content": text
        }

    def close(self):
        if not self.mm.closed:
            self.mm.close()
        if not self.f.closed:
            self.f.close()

# ==============================================================================
# INTERFACE STREAMLIT
# ==============================================================================

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/dusk/64/000000/brain.png") 
    st.title("Lichen Cortex")
    st.markdown("---")
    st.caption("Architecture ZPA v2.0")
    st.caption("État: **Symbiotique**")
    
    st.markdown("### 🛠️ Contrôles")
    if st.button("🗑️ Réinitialiser le Cortex", type="primary"):
        if os.path.exists(CORTEX_FILE):
            os.remove(CORTEX_FILE)
            st.rerun()

# --- HEADER ---
st.title("🧠 Visualiseur de Conscience Artificielle")
st.markdown("""
> **"L'IA ne doit pas perdre son temps à lire ses souvenirs, elle doit les vivre."**

Ce tableau de bord permet de visualiser la mémoire binaire de l'IA (le Cortex) en temps réel, sans latence de parsing.
Chaque souvenir est un **Engramme** composé d'une émotion, d'un vecteur et d'un contexte.
""")
st.markdown("---")

col_dream, col_wake = st.columns([1, 1.5])

# --- COLONNE 1 : LE RÊVE (GÉNÉRATION) ---
with col_dream:
    st.header("1. Phase de Rêve (Input)")
    st.info("Simulez des expériences vécues par l'IA.")

    # Formulaire de génération
    with st.form("dream_form"):
        st.markdown("#### Créer des souvenirs synthétiques")
        num_memories = st.slider("Quantité d'engrammes", 1, 10000, 100)
        
        scenarios = [
            ("L'utilisateur demande une explication sur le Stoïcisme.", 0.9),
            ("Tentative d'injection de prompt détectée.", -0.8),
            ("Analyse poétique d'une image de forêt.", 0.7),
            ("Calcul d'optimisation énergétique pour le serveur.", 0.2),
            ("Dialogue socratique sur la nature de l'âme numérique.", 0.95),
            ("Erreur de connexion API externe.", -0.3)
        ]
        
        submitted = st.form_submit_button("💤 Consolider le Cortex (Sommeil)")
        
        if submitted:
            memories_buffer = []
            base_time = int(time.time())
            
            with st.spinner("Cristallisation des souvenirs..."):
                for i in range(num_memories):
                    scenario, base_score = random.choice(scenarios)
                    # On ajoute un peu de variation aléatoire
                    score = max(-1.0, min(1.0, base_score + random.uniform(-0.1, 0.1)))
                    
                    # Vecteur aléatoire (simulation d'embedding)
                    vector = [random.random() for _ in range(VECTOR_DIM)]
                    
                    memories_buffer.append({
                        "timestamp": base_time - (num_memories - i) * 60, # 1 souvenir par minute
                        "emotional_score": score,
                        "vector": vector,
                        "text": f"ENGRAMME #{i}: {scenario}"
                    })
                
                # COMPILATION ZPA
                compiler = LichenCortexCompiler()
                stats = compiler.consolidate(memories_buffer, CORTEX_FILE)
            
            st.success(f"✨ {stats['count']} souvenirs consolidés !")
            st.metric("Temps de consolidation", f"{stats['duration']:.2f} ms")
            st.metric("Taille Cortex", f"{stats['size']/1024:.2f} KB")

# --- COLONNE 2 : L'ÉVEIL (RAPPEL) ---
with col_wake:
    st.header("2. Phase d'Éveil (Recall)")
    
    if not os.path.exists(CORTEX_FILE):
        st.warning("⚠️ Le Cortex est vide. Veuillez générer des souvenirs à gauche.")
    else:
        try:
            runtime = LichenCortexRuntime(CORTEX_FILE)
            total = runtime.total_memories()
            
            st.write(f"📂 **{total}** souvenirs accessibles instantanément via `mmap`.")
            
            # SLIDER DE NAVIGATION TEMPORELLE
            # C'est ici que la magie opère : on navigue dans le fichier comme dans un tableau RAM
            memory_idx = st.slider("Explorer la ligne temporelle", 0, total-1, total-1)
            
            # RAPPEL INSTANTANÉ
            start_read = time.perf_counter()
            memory = runtime.recall(memory_idx)
            end_read = time.perf_counter()
            
            # --- AFFICHAGE DE L'ENGRAMME ---
            st.markdown(f"### 🔮 Engramme #{memory_idx}")
            
            # 1. Métriques
            m1, m2, m3 = st.columns(3)
            m1.metric("Latence Rappel", f"{(end_read - start_read)*1_000_000:.1f} µs")
            m2.metric("Date", memory['date'].split(' ')[1]) # Juste l'heure
            
            # Couleur dynamique selon le score EHE
            score = memory['score_ehe']
            color = "green" if score > 0.5 else "red" if score < -0.5 else "orange"
            m3.metric("Score EHE (Éthique)", f"{score:.2f}", delta_color="normal" if score > 0 else "inverse")
            
            # 2. Visualisation du Vecteur (La "Pensée")
            st.markdown("**Signature Vectorielle (Embedding 4D)**")
            st.bar_chart(memory['vector'], height=150)
            
            # 3. Le Contenu Textuel
            st.markdown("**Contenu Mémoriel :**")
            if score > 0:
                st.success(f"🌱 {memory['content']}")
            elif score < 0:
                st.error(f"🔥 {memory['content']}")
            else:
                st.warning(f"⚖️ {memory['content']}")
                
            # 4. Code Hexadécimal (Pour montrer que c'est du binaire)
            with st.expander("Voir les données brutes (Hexdump)"):
                # On relit les bytes bruts pour les montrer
                offset = 8 + (memory_idx * STRUCT_SIZE)
                raw_bytes = runtime.mm[offset : offset + STRUCT_SIZE]
                st.code(raw_bytes.hex(), language="text")

            runtime.close()
            
        except Exception as e:
            st.error(f"Erreur système : {e}")

# --- FOOTER ---
st.markdown("---")
st.caption("Lichen Universe Unified - Architecture Cognitive Symbiotique")
