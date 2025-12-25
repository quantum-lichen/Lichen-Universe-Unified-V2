import streamlit as st
import sys
import time
import os

# ==========================================
# CONFIGURATION DU CHEMIN (PATH)
# ==========================================
# On s'assure que Python trouve tes modules HNP dans le dossier '../src' ou 'src'
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, '../src') # Ajuste si nécessaire
sys.path.insert(0, src_path)

# ==========================================
# IMPORTATION DES MODULES HNP
# ==========================================
try:
    from hnp_packet import HNPPacket
    from hnp_flow import HNPFlowControl
    from hnp_router import HNPRouter
except ImportError:
    st.error("⚠️ ERREUR CRITIQUE : Impossible d'importer les modules HNP.")
    st.info(f"Le système cherche dans : {src_path}")
    st.warning("Assurez-vous que le dossier 'src' contenant hnp_packet.py, etc. est bien accessible.")
    st.stop()

# ==========================================
# CONFIGURATION DE L'INTERFACE
# ==========================================
st.set_page_config(
    page_title="HNP Visualizer",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌌 HARMONIC NETWORK PROTOCOL")
st.markdown("**Visualisation Temps Réel du Protocole Philonomique**")

# Barre latérale pour le style
with st.sidebar:
    st.header("État du Système")
    st.success("✅ HNP KERNEL: ACTIF")
    st.info(f"🐍 Python Runtime: {sys.version.split()[0]}")
    st.metric("Constante φ", "1.618033")
    st.metric("Constante π", "3.141592")

# Création des onglets pour les démos
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
            # Création du paquet
            try:
                packet = HNPPacket()
                packet.src_addr = int(src_input, 16)
                packet.dst_addr = int(dst_input, 16)
                packet.sequence = int(seq_input)
                packet.set_data(msg_input.encode()) # Encodage auto en bytes
                packet.encode()

                # Affichage des métriques
                c1, c2, c3 = st.columns(3)
                c1.metric("Source", f"0x{packet.src_addr:08X}")
                c2.metric("Destination", f"0x{packet.dst_addr:08X}")
                c3.metric("Sequence", packet.sequence)

                st.markdown("---")
                
                # Tzolk'in
                cycle, day, trecena, veintena = packet.get_tzolkin_position()
                st.subheader("🌀 Tzolk'in Timestamp")
                tc1, tc2, tc3, tc4 = st.columns(4)
                tc1.metric("Cycle", cycle)
                tc2.metric("Day", f"{day}/260")
                tc3.metric("Trecena", f"{trecena}/13")
                tc4.metric("Veintena", f"{veintena}/20")

                # Validation
                is_valid = packet.verify_perfect()
                if is_valid:
                    st.success("✓ VALIDATION PARFAITE (Géométrie Intacte)")
                else:
                    st.error("⚠ ERREUR DE VALIDATION")

                # Hex Dump
                packet_bytes = packet.to_bytes()
                st.subheader(f"💾 Raw Data ({len(packet_bytes)} bytes / 496 bits)")
                st.code(packet_bytes.hex(), language="text")
                
            except Exception as e:
                st.error(f"Erreur lors de la création du paquet: {e}")

# ==========================================
# DEMO 2: FLOW CONTROL
# ==========================================
with tab2:
    st.header("Simulation du Contrôle de Flux (φ-Based)")
    
    if st.button("🌊 Lancer la Simulation de Flux"):
        flow = HNPFlowControl(initial_rate=1.0)
        
        # Containers pour affichage dynamique
        chart_placeholder = st.empty()
        metrics_placeholder = st.empty()
        log_placeholder = st.empty()
        
        rate_history = []
        events = ['success'] * 5 + ['congestion'] * 2 + ['success'] * 3 + ['congestion']
        
        for i, event in enumerate(events):
            time.sleep(0.5) # Petit délai pour l'animation
            
            if event == 'success':
                flow.on_success()
                log_text = f"Step {i+1}: ✅ Success"
            else:
                flow.on_congestion()
                log_text = f"Step {i+1}: ⚠ Congestion détectée"
                
            current_rate = flow.get_rate()
            rate_history.append(current_rate)
            
            # Mise à jour graphique
            chart_placeholder.line_chart(rate_history, height=300)
            
            # Mise à jour métriques
            with metrics_placeholder.container():
                mc1, mc2, mc3 = st.columns(3)
                mc1.metric("Taux (Packets/s)", f"{current_rate:.3f}")
                mc2.metric("État", "Converging..." if not flow.has_converged() else "Stable")
                mc3.markdown(f"**Event:** {log_text}")

        # Résultats finaux
        st.success("Simulation Terminée")
        stats = flow.get_statistics()
        
        st.subheader("📊 Statistiques Finales")
        sc1, sc2, sc3 = st.columns(3)
        sc1.metric("Taux Final", f"{stats.get('mean_rate', 0):.3f}")
        sc2.metric("Qualité Convergence", f"{flow.get_convergence_quality():.2f}")
        sc3.metric("Ratio Succès", f"{stats.get('success_ratio', 0):.1%}")

# ==========================================
# DEMO 3: FRACTAL ROUTER
# ==========================================
with tab3:
    st.header("Routeur Fractal & Adressage")
    
    router = HNPRouter()
    
    # Setup initial
    addresses = [0x00000001, 0x00000002, 0x00000005, 0x00000010, 0x7FFFFFFF]
    for addr in addresses:
        router.register_node(addr)
        
    st.info(f"Noeuds enregistrés dans l'espace topologique : {len(addresses)}")
    
    c1, c2 = st.columns(2)
    with c1:
        start_node = st.selectbox("Noeud de Départ", [f"0x{a:08X}" for a in addresses], index=0)
    with c2:
        end_node = st.selectbox("Noeud d'Arrivée", [f"0x{a:08X}" for a in addresses], index=4)
        
    if st.button("🗺️ Calculer la Route"):
        src = int(start_node, 16)
        dst = int(end_node, 16)
        
        path = router.route(src, dst)
        dist = router.distance(src, dst)
        
        st.subheader("Résultat du Routage")
        
        # Affichage visuel du chemin
        path_str = " ➔ ".join([f"**0x{addr:08X}**" for addr in path])
        st.markdown(f"### {path_str}")
        
        rc1, rc2 = st.columns(2)
        rc1.metric("Sauts (Hops)", len(path) - 1)
        rc2.metric("Distance Métrique", dist)
        
        # Stats Router
        stats = router.get_statistics()
        with st.expander("Voir les stats du routeur"):
            st.json(stats)

# ==========================================
# DEMO 4: END-TO-END
# ==========================================
with tab4:
    st.header("Transmission Complète (End-to-End)")
    st.markdown("Simulation d'une transmission complète avec délais réseau et corrections.")
    
    msg_to_send = st.text_input("Message à envoyer", "Harmonic transmission test - φ = 1.618...")
    
    if st.button("🚀 Lancer la Transmission"):
        # Init components
        packet = HNPPacket()
        flow = HNPFlowControl()
        router = HNPRouter()
        
        src_addr = 0x00000001
        dst_addr = 0x7FFFFFFF
        router.register_node(src_addr)
        router.register_node(dst_addr)
        
        # Prepare packet
        packet.src_addr = src_addr
        packet.dst_addr = dst_addr
        packet.set_data(msg_to_send) # correction ici: pas besoin d'encoder si set_data le gère, sinon .encode()
        packet.encode()
        
        # Route
        path = router.route(src_addr, dst_addr)
        
        # Display progress
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        st.write("📡 **Journal de transmission:**")
        log_container = st.container()
        
        total_hops = len(path) - 1
        
        for i, hop in enumerate(path[:-1]):
            next_hop = path[i+1]
            
            # Simulation délai
            time.sleep(0.3)
            
            # Flow logic
            if i % 3 == 0:
                flow.on_success()
                icon = "✅"
            else:
                flow.on_congestion()
                icon = "⚠"
            
            # Log
            with log_container:
                st.markdown(f"`{icon} Hop {i+1}: 0x{hop:08X} → 0x{next_hop:08X}` (Rate: {flow.get_rate():.2f} pkt/s)")
            
            # Update progress
            progress = (i + 1) / total_hops
            progress_bar.progress(progress)
            status_text.text(f"Transmission en cours... Hop {i+1}/{total_hops}")

        progress_bar.progress(1.0)
        status_text.text("Transmission terminée !")
        
        st.success("📥 PAQUET REÇU")
        st.code(packet.get_data().decode(), language="text")
        
        if packet.verify_perfect():
            st.balloons()
            st.success("Intégrité des données : 100% (Validé par 496/E8)")
        else:
            st.error("Données corrompues")

# Pied de page
st.markdown("---")
st.markdown("🌌 **LICHEN COLLECTIVE** - *Architecture Philonomique v2.0*")
