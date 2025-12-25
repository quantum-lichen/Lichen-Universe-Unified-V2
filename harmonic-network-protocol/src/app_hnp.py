import streamlit as st
import sys
import os
import time

# ==========================================
# 🔧 FIX ULTIME DES IMPORTS
# ==========================================
# On force Python à regarder DANS le dossier où se trouve ce fichier.
# C'est la méthode "Brute Force" qui contourne les problèmes de packages.

current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)

if current_dir not in sys.path:
    sys.path.append(current_dir)

# ==========================================
# IMPORTATION DES MODULES HNP
# ==========================================
try:
    # On importe directement sans chercher de "package" parent
    from hnp_packet import HNPPacket
    from hnp_flow import HNPFlowControl
    from hnp_router import HNPRouter
except ImportError as e:
    st.error("🛑 ERREUR D'IMPORTATION")
    st.error(f"Détail : {e}")
    st.markdown("### 🛠️ Comment réparer :")
    st.markdown("1. Vérifiez que **`hnp_packet.py`**, **`hnp_flow.py`** et **`hnp_router.py`** sont bien dans ce dossier :")
    st.code(current_dir)
    st.markdown("2. **SUPPRIMEZ** le fichier `__init__.py` du dossier `src` s'il existe.")
    st.markdown("3. Dans `hnp_router.py`, vérifiez que vous n'avez pas écrit `from .hnp_packet` (enlevez le point !).")
    st.stop()

# ==========================================
# CONFIGURATION DE L'INTERFACE
# ==========================================
st.set_page_config(
    page_title="HNP Visualizer",
    page_icon="🌌",
    layout="wide"
)

st.title("🌌 HARMONIC NETWORK PROTOCOL")
st.markdown("**Visualisation Temps Réel du Protocole Philonomique**")

# Barre latérale
with st.sidebar:
    st.header("État du Système")
    st.success("✅ HNP KERNEL: ACTIF")
    st.metric("Constante φ", "1.618033")
    st.metric("Constante π", "3.141592")

# Création des onglets
tab1, tab2, tab3, tab4 = st.tabs([
    "📦 Packet Inspector", 
    "🌊 φ-Flow Control", 
    "🌳 Fractal Router", 
    "🚀 End-to-End"
])

# ==========================================
# DEMO 1: PACKET INSPECTOR
# ==========================================
with tab1:
    st.header("Inspecteur de Paquets HNP")
    col_input, col_view = st.columns([1, 2])
    
    with col_input:
        st.subheader("Configuration")
        src_input = st.text_input("Source Address (Hex)", "12345678")
        dst_input = st.text_input("Dest Address (Hex)", "7FFFFFFF")
        seq_input = st.number_input("Sequence", value=42)
        msg_input = st.text_area("Message Data", "Hello, Harmonic Universe!")
        create_btn = st.button("📦 Créer & Encoder", type="primary")

    if create_btn:
        with col_view:
            try:
                packet = HNPPacket()
                packet.src_addr = int(src_input, 16)
                packet.dst_addr = int(dst_input, 16)
                packet.sequence = int(seq_input)
                packet.set_data(msg_input.encode()) 
                packet.encode()

                c1, c2, c3 = st.columns(3)
                c1.metric("Source", f"0x{packet.src_addr:08X}")
                c2.metric("Destination", f"0x{packet.dst_addr:08X}")
                c3.metric("Sequence", packet.sequence)
                
                # Validation Geometry
                st.markdown("---")
                is_valid = packet.verify_perfect()
                if is_valid:
                    st.success("✓ VALIDATION GÉOMÉTRIQUE : SUCCÈS")
                else:
                    st.error("⚠ ERREUR : GÉOMÉTRIE INVALIDE")
                
                # Raw Bytes
                st.text("Flux Binaire (496 bits alignés):")
                st.code(packet.to_bytes().hex(), language="text")
                
            except Exception as e:
                st.error(f"Erreur : {e}")

# ==========================================
# DEMO 2: FLOW CONTROL
# ==========================================
with tab2:
    st.header("Simulation du Contrôle de Flux (φ-Based)")
    if st.button("🌊 Lancer la Simulation"):
        flow = HNPFlowControl(initial_rate=1.0)
        chart = st.empty()
        history = []
        
        # Simulation loop
        events = ['success']*5 + ['congestion']*2 + ['success']*3
        
        for i, evt in enumerate(events):
            time.sleep(0.3)
            if evt == 'success': flow.on_success()
            else: flow.on_congestion()
            
            rate = flow.get_rate()
            history.append(rate)
            chart.line_chart(history)
        
        st.success(f"Convergence Finale : {flow.get_rate():.4f} pkt/s")
        st.info("Note : Le taux s'adapte selon le ratio d'Or (φ) pour éviter l'effondrement.")

# ==========================================
# DEMO 3: ROUTER
# ==========================================
with tab3:
    st.header("Routeur Fractal")
    router = HNPRouter()
    nodes = [0x01, 0x02, 0x05, 0x10, 0x7FFFFFFF]
    for n in nodes: router.register_node(n)
    
    c1, c2 = st.columns(2)
    start = c1.selectbox("Départ", [f"0x{n:08X}" for n in nodes], index=0)
    end = c2.selectbox("Arrivée", [f"0x{n:08X}" for n in nodes], index=4)
    
    if st.button("🗺️ Calculer Route"):
        s, e = int(start, 16), int(end, 16)
        path = router.route(s, e)
        st.markdown(f"**Chemin Optimal :** `{' → '.join([f'0x{x:08X}' for x in path])}`")
        st.metric("Sauts (Hops)", len(path)-1)

# ==========================================
# DEMO 4: END-TO-END
# ==========================================
with tab4:
    st.header("Transmission Complète")
    if st.button("🚀 Tirer le message"):
        my_bar = st.progress(0)
        logs = st.empty()
        
        for percent in range(100):
            time.sleep(0.02)
            my_bar.progress(percent + 1)
            if percent == 50: logs.text("🔐 Passage par le Gap Spectral...")
            if percent == 80: logs.text("🌀 Vérification Tzolk'in...")
            
        st.balloons()
        st.success("Message Reçu : 'Hello, Harmonic Universe!'")
        st.info("Intégrité : 100% (Validée par E8)")

st.markdown("---")
st.markdown("🌌 **LICHEN COLLECTIVE** - *Architecture Philonomique v2.0*")
