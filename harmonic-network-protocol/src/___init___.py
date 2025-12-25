"""
Harmonic Network Protocol (HNP)
A revolutionary networking protocol based on perfect numbers,
golden ratio, and astronomical synchronization.

Author: Bryan Ouellette & Claude AI
License: Apache 2.0
"""

__version__ = "1.0.0"
__author__ = "Bryan Ouellette & Claude AI"

from .hnp_packet import HNPPacket
from .hnp_flow import HNPFlowControl
from .hnp_router import HNPRouter
from .e8_encoding import E8Encoder

__all__ = [
    'HNPPacket',
    'HNPFlowControl',
    'HNPRouter',
    'E8Encoder',
    'send_data',
    'receive_data',
]


def send_data(data: bytes, destination: int, flow_control=None):
    """
    Convenience function to send data using HNP
    
    Args:
        data: Data to send (bytes)
        destination: 31-bit destination address
        flow_control: Optional HNPFlowControl instance
    
    Returns:
        bool: Success status
    """
    packet = HNPPacket()
    packet.dst_addr = destination
    packet.set_data(data)
    packet.encode()
    
    if not flow_control:
        flow_control = HNPFlowControl()
    
    # Simulated send (would interface with actual network layer)
    success = packet.verify_perfect()
    
    if success:
        flow_control.on_success()
    else:
        flow_control.on_congestion()
    
    return success


def receive_data(packet_bytes: bytes):
    """
    Convenience function to receive and decode HNP packet
    
    Args:
        packet_bytes: Raw packet data (496 bits)
    
    Returns:
        tuple: (data, src_addr, valid)
    """
    packet = HNPPacket.from_bytes(packet_bytes)
    
    if packet.verify_perfect():
        data = packet.decode()
        return (data, packet.src_addr, True)
    else:
        return (None, None, False)
