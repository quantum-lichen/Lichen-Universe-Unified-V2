#!/usr/bin/env python3
"""
Basic HNP Demo
Demonstrates core functionality of Harmonic Network Protocol
"""

import sys
sys.path.insert(0, '../src')

from hnp_packet import HNPPacket
from hnp_flow import HNPFlowControl
from hnp_router import HNPRouter
import time


def demo_packet():
    """Demo 1: Basic packet creation and validation"""
    print("=" * 60)
    print("DEMO 1: HNP PACKET")
    print("=" * 60)
    print()
    
    # Create packet
    packet = HNPPacket()
    packet.src_addr = 0x12345678
    packet.dst_addr = 0x7FFFFFFF  # Mersenne prime
    packet.sequence = 42
    packet.set_data(b"Hello, Harmonic Universe!")
    
    # Encode
    packet.encode()
    
    print(f"📦 Packet created:")
    print(f"   Source: 0x{packet.src_addr:08X}")
    print(f"   Destination: 0x{packet.dst_addr:08X}")
    print(f"   Sequence: {packet.sequence}")
    print(f"   Data: {packet.get_data().decode()}")
    print()
    
    # Tzolk'in position
    cycle, day, trecena, veintena = packet.get_tzolkin_position()
    print(f"🌀 Tzolk'in Timestamp:")
    print(f"   Cycle: {cycle}")
    print(f"   Day: {day}/260")
    print(f"   Trecena: {trecena}/13")
    print(f"   Veintena: {veintena}/20")
    print()
    
    # Validate
    is_valid = packet.verify_perfect()
    print(f"✓ Perfect validation: {is_valid}")
    print()
    
    # Serialize/Deserialize
    packet_bytes = packet.to_bytes()
    print(f"💾 Serialized: {len(packet_bytes)} bytes (496 bits)")
    print(f"   Hex: {packet_bytes[:16].hex()}...")
    print()
    
    # Deserialize
    packet2 = HNPPacket.from_bytes(packet_bytes)
    print(f"📬 Deserialized: {packet2.get_data().decode()}")
    print(f"   Still valid: {packet2.verify_perfect()}")
    print()


def demo_flow_control():
    """Demo 2: φ-based flow control"""
    print("=" * 60)
    print("DEMO 2: φ-FLOW CONTROL")
    print("=" * 60)
    print()
    
    flow = HNPFlowControl(initial_rate=1.0)
    
    print(f"🌊 Initial rate: {flow.get_rate():.3f} packets/sec")
    print()
    
    print("📈 Simulating network conditions...")
    print()
    
    # Simulate success/congestion
    events = ['success'] * 5 + ['congestion'] * 2 + ['success'] * 3 + ['congestion']
    
    for i, event in enumerate(events):
        if event == 'success':
            flow.on_success()
            print(f"   {i+1}. ✓ Success → Rate: {flow.get_rate():.3f} pkt/s")
        else:
            flow.on_congestion()
            print(f"   {i+1}. ⚠ Congestion → Rate: {flow.get_rate():.3f} pkt/s")
    
    print()
    print(f"💎 Final rate: {flow.get_rate():.3f} packets/sec")
    print(f"🎯 Converged: {flow.has_converged()}")
    print(f"⭐ Quality: {flow.get_convergence_quality():.2f}")
    print()
    
    # Statistics
    stats = flow.get_statistics()
    print(f"📊 Statistics:")
    print(f"   Success ratio: {stats['success_ratio']:.1%}")
    print(f"   Mean rate: {stats['mean_rate']:.3f} pkt/s")
    print(f"   Min/Max: {stats['min_rate_seen']:.3f} / {stats['max_rate_seen']:.3f}")
    print()


def demo_router():
    """Demo 3: Fractal routing"""
    print("=" * 60)
    print("DEMO 3: FRACTAL ROUTER")
    print("=" * 60)
    print()
    
    router = HNPRouter()
    
    print(f"🌳 Router initialized")
    print()
    
    # Register some nodes
    addresses = [
        0x00000001,  # Node 1
        0x00000002,  # Node 2
        0x00000005,  # Node 3
        0x00000010,  # Node 4
        0x7FFFFFFF,  # Mersenne prime node
    ]
    
    print(f"📝 Registering {len(addresses)} nodes...")
    for addr in addresses:
        router.register_node(addr)
        print(f"   ✓ 0x{addr:08X}")
    print()
    
    # Route between nodes
    src = addresses[0]
    dst = addresses[-1]
    
    print(f"🗺️ Routing from 0x{src:08X} to 0x{dst:08X}...")
    path = router.route(src, dst)
    print(f"   Path: {' → '.join(f'0x{addr:08X}' for addr in path)}")
    print(f"   Hops: {len(path) - 1}")
    print(f"   Distance: {router.distance(src, dst)}")
    print()
    
    # Statistics
    stats = router.get_statistics()
    print(f"📊 Router Statistics:")
    print(f"   Total nodes: {stats['total_nodes']}")
    print(f"   Tree depth: {stats['max_depth']}")
    print(f"   Theoretical depth (log_φ n): {stats['theoretical_depth']}")
    print(f"   Efficiency: {stats['efficiency']:.2%}")
    print()


def demo_end_to_end():
    """Demo 4: End-to-end transmission"""
    print("=" * 60)
    print("DEMO 4: END-TO-END TRANSMISSION")
    print("=" * 60)
    print()
    
    print("🚀 Simulating network transmission...")
    print()
    
    # Create components
    packet = HNPPacket()
    flow = HNPFlowControl()
    router = HNPRouter()
    
    # Setup
    src_addr = 0x00000001
    dst_addr = 0x7FFFFFFF
    
    router.register_node(src_addr)
    router.register_node(dst_addr)
    
    # Create message
    message = "Harmonic transmission test - φ = 1.618..."
    packet.src_addr = src_addr
    packet.dst_addr = dst_addr
    packet.set_data(message)
    packet.encode()
    
    print(f"📤 Sending: {message.decode()}")
    print(f"   From: 0x{src_addr:08X}")
    print(f"   To: 0x{dst_addr:08X}")
    print()
    
    # Route
    path = router.route(src_addr, dst_addr)
    print(f"🗺️ Route: {' → '.join(f'0x{a:08X}' for a in path)}")
    print()
    
    # Simulate transmission
    print(f"📡 Transmitting...")
    for i, hop in enumerate(path[:-1]):
        next_hop = path[i+1]
        
        # Simulate delay
        time.sleep(0.1)
        
        # Update flow control
        if i % 3 == 0:
            flow.on_success()
            status = "✓"
        else:
            flow.on_congestion()
            status = "⚠"
        
        print(f"   {status} Hop {i+1}: 0x{hop:08X} → 0x{next_hop:08X} (rate: {flow.get_rate():.2f} pkt/s)")
    
    print()
    print(f"📥 Received: {packet.get_data().decode()}")
    print(f"   Valid: {packet.verify_perfect()}")
    print()
    
    print(f"✨ Transmission complete!")
    print(f"   Final rate: {flow.get_rate():.3f} pkt/s")
    print(f"   Total hops: {len(path) - 1}")
    print()


def main():
    """Run all demos"""
    print()
    print("🌊" * 30)
    print("  HARMONIC NETWORK PROTOCOL - DEMO")
    print("🌊" * 30)
    print()
    
    try:
        demo_packet()
        input("Press Enter to continue...")
        print()
        
        demo_flow_control()
        input("Press Enter to continue...")
        print()
        
        demo_router()
        input("Press Enter to continue...")
        print()
        
        demo_end_to_end()
        
        print()
        print("=" * 60)
        print("✨ ALL DEMOS COMPLETE!")
        print("=" * 60)
        print()
        print("Next steps:")
        print("  • Run benchmarks: python benchmark.py")
        print("  • Run tests: pytest ../tests/")
        print("  • See docs: ../docs/API.md")
        print()
        
    except KeyboardInterrupt:
        print("\n\n⚠ Demo interrupted.")
        sys.exit(0)


if __name__ == "__main__":
    main()
---
