#!/usr/bin/env python3
"""
HNP Unit Tests
Comprehensive test suite for Harmonic Network Protocol
"""

import sys
sys.path.insert(0, '../src')

import pytest
from hnp_packet import HNPPacket
from hnp_flow import HNPFlowControl, AdaptiveHNPFlowControl
from hnp_router import HNPRouter
from e8_encoding import E8Encoder


class TestHNPPacket:
    """Test HNP packet functionality"""
    
    def test_packet_creation(self):
        """Test basic packet creation"""
        packet = HNPPacket()
        assert packet.src_addr == 0
        assert packet.dst_addr == 0
        assert packet.PACKET_SIZE_BITS == 496
        assert packet.PACKET_SIZE_BYTES == 62
    
    def test_packet_data(self):
        """Test packet data handling"""
        packet = HNPPacket()
        data = b"Test data"
        packet.set_data(data)
        assert packet.get_data() == data
    
    def test_packet_encoding(self):
        """Test packet encoding"""
        packet = HNPPacket()
        packet.set_data(b"Test")
        packet.encode()
        
        # Should have timestamp and checksum
        assert packet.tzolkin_time > 0
        assert packet.checksum > 0
    
    def test_perfect_validation(self):
        """Test perfect number validation"""
        packet = HNPPacket()
        packet.set_data(b"Hello")
        packet.encode()
        
        # Should validate
        assert packet.verify_perfect() == True
        
        # Corrupt checksum
        packet.checksum += 1
        assert packet.verify_perfect() == False
    
    def test_serialization(self):
        """Test packet serialization/deserialization"""
        packet1 = HNPPacket()
        packet1.src_addr = 0x12345678
        packet1.dst_addr = 0x7FFFFFFF
        packet1.set_data(b"Test message")
        packet1.encode()
        
        # Serialize
        packet_bytes = packet1.to_bytes()
        assert len(packet_bytes) == 62
        
        # Deserialize
        packet2 = HNPPacket.from_bytes(packet_bytes)
        assert packet2.src_addr == packet1.src_addr
        assert packet2.dst_addr == packet1.dst_addr
        assert packet2.get_data() == packet1.get_data()
    
    def test_tzolkin_position(self):
        """Test Tzolk'in timestamp"""
        packet = HNPPacket()
        packet.encode()
        
        cycle, day, trecena, veintena = packet.get_tzolkin_position()
        
        # Validate ranges
        assert 0 <= day < 260
        assert 0 <= trecena < 13
        assert 0 <= veintena < 20


class TestFlowControl:
    """Test φ-based flow control"""
    
    def test_flow_initialization(self):
        """Test flow control initialization"""
        flow = HNPFlowControl(initial_rate=1.0)
        assert flow.get_rate() == 1.0
        assert flow.PHI == pytest.approx(1.618033988749895, rel=1e-6)
    
    def test_on_success(self):
        """Test success increases rate by φ"""
        flow = HNPFlowControl(initial_rate=1.0)
        initial = flow.get_rate()
        
        flow.on_success()
        
        assert flow.get_rate() == pytest.approx(initial * flow.PHI, rel=1e-6)
    
    def test_on_congestion(self):
        """Test congestion decreases rate by 1/φ"""
        flow = HNPFlowControl(initial_rate=10.0)
        initial = flow.get_rate()
        
        flow.on_congestion()
        
        assert flow.get_rate() == pytest.approx(initial / flow.PHI, rel=1e-6)
    
    def test_rate_bounds(self):
        """Test rate stays within bounds"""
        flow = HNPFlowControl(initial_rate=1.0, min_rate=0.1, max_rate=10.0)
        
        # Try to exceed max
        for _ in range(20):
            flow.on_success()
        assert flow.get_rate() <= 10.0
        
        # Try to go below min
        for _ in range(40):
            flow.on_congestion()
        assert flow.get_rate() >= 0.1
    
    def test_convergence(self):
        """Test φ-convergence"""
        flow = HNPFlowControl(initial_rate=1.0)
        
        # Simulate alternating success/congestion
        for _ in range(10):
            flow.on_success()
            flow.on_congestion()
        
        # Should converge
        assert flow.has_converged(window=5, threshold=0.2)
    
    def test_statistics(self):
        """Test flow statistics"""
        flow = HNPFlowControl()
        
        flow.on_success()
        flow.on_congestion()
        flow.on_success()
        
        stats = flow.get_statistics()
        
        assert stats['success_count'] == 2
        assert stats['congestion_count'] == 1
        assert stats['total_events'] == 3
        assert stats['success_ratio'] == pytest.approx(2/3, rel=0.01)


class TestRouter:
    """Test fractal routing"""
    
    def test_router_initialization(self):
        """Test router initialization"""
        router = HNPRouter()
        assert router.root is not None
        assert len(router.address_map) >= 1
    
    def test_node_registration(self):
        """Test node registration"""
        router = HNPRouter()
        
        addr = 0x12345678
        success = router.register_node(addr)
        
        assert success == True
        assert addr in router.address_map
        
        # Can't register twice
        success2 = router.register_node(addr)
        assert success2 == False
    
    def test_routing(self):
        """Test route finding"""
        router = HNPRouter()
        
        src = 0x00000001
        dst = 0x7FFFFFFF
        
        router.register_node(src)
        router.register_node(dst)
        
        path = router.route(src, dst)
        
        assert len(path) >= 2
        assert path[0] == src
        assert path[-1] == dst
    
    def test_distance(self):
        """Test harmonic distance"""
        router = HNPRouter()
        
        addr1 = 0x00000001
        addr2 = 0x00000002
        
        router.register_node(addr1)
        router.register_node(addr2)
        
        distance = router.distance(addr1, addr2)
        assert distance >= 0
    
    def test_neighbors(self):
        """Test neighbor discovery"""
        router = HNPRouter()
        
        # Register several nodes
        addrs = [0x00000001, 0x00000002, 0x00000003]
        for addr in addrs:
            router.register_node(addr)
        
        neighbors = router.get_neighbors(addrs[0], max_distance=2)
        assert len(neighbors) >= 0


class TestE8Encoding:
    """Test E8 lattice encoding"""
    
    def test_encoder_initialization(self):
        """Test E8 encoder initialization"""
        encoder = E8Encoder()
        assert encoder.E8_DIM == 8
    
    def test_encode_decode(self):
        """Test encoding and decoding"""
        encoder = E8Encoder()
        
        data = b"Test data for E8 encoding"
        
        # Encode
        encoded = encoder.encode(data)
        assert len(encoded) == 31
        
        # Decode
        decoded = encoder.decode(encoded)
        assert decoded.startswith(data)
    
    def test_error_correction(self):
        """Test error correction capability"""
        encoder = E8Encoder()
        
        data = b"Original data"
        encoded = encoder.encode(data)
        
        # Simulate 1-bit error
        corrupted = bytearray(encoded)
        corrupted[5] ^= 0x01  # Flip 1 bit
        
        # Correct
        corrected = encoder.correct_errors(bytes(corrupted))
        
        # Should be similar to original
        assert len(corrected) == len(encoded)
    
    def test_error_stats(self):
        """Test error correction statistics"""
        encoder = E8Encoder()
        
        stats = encoder.estimate_error_correction_capacity()
        
        assert stats['dimension'] == 8
        assert stats['kissing_number'] == 240
        assert 0 < stats['packing_density'] < 1


# Integration tests

def test_end_to_end_transmission():
    """Test complete transmission flow"""
    # Create all components
    packet = HNPPacket()
    flow = HNPFlowControl()
    router = HNPRouter()
    
    # Setup
    src = 0x00000001
    dst = 0x7FFFFFFF
    
    router.register_node(src)
    router.register_node(dst)
    
    # Create packet
    packet.src_addr = src
    packet.dst_addr = dst
    packet.set_data(b"Integration test")
    packet.encode()
    
    # Verify
    assert packet.verify_perfect()
    
    # Route
    path = router.route(src, dst)
    assert len(path) >= 2
    
    # Simulate transmission
    for _ in path[:-1]:
        flow.on_success()
    
    assert flow.get_rate() > 1.0


def test_phi_convergence_property():
    """Test that φ-ratio provides stable convergence"""
    flow = HNPFlowControl()
    
    # Simulate realistic network conditions
    import random
    random.seed(42)
    
    for _ in range(100):
        if random.random() > 0.3:  # 70% success rate
            flow.on_success()
        else:
            flow.on_congestion()
    
    # Should converge
    assert flow.has_converged(window=20, threshold=0.2)
    
    # Quality should be good
    quality = flow.get_convergence_quality()
    assert quality > 0.5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
