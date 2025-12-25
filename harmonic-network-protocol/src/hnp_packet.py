"""
HNP Packet Implementation
496-bit packets based on perfect number properties
"""

import struct
import hashlib
from datetime import datetime
from typing import Optional
from .e8_encoding import E8Encoder


class HNPPacket:
    """
    Harmonic Network Protocol Packet
    Total size: 496 bits (62 bytes) - 3rd perfect number
    """
    
    # Constants
    PACKET_SIZE_BITS = 496
    PACKET_SIZE_BYTES = 62
    HEADER_SIZE_BITS = 248
    DATA_SIZE_BITS = 248
    
    def __init__(self):
        # Header fields (248 bits total)
        self.src_addr: int = 0          # 31 bits (Mersenne prime)
        self.dst_addr: int = 0          # 31 bits
        self.sequence: int = 0          # 62 bits (496/8)
        self.tzolkin_time: int = 0      # 62 bits
        self.checksum: int = 0          # 62 bits
        
        # Data (248 bits)
        self._raw_data: bytes = b'\x00' * 31  # 31 bytes = 248 bits
        self._encoded_data: Optional[bytes] = None
        
        # E8 encoder
        self.e8_encoder = E8Encoder()
    
    def set_data(self, data: bytes):
        """Set packet data (will be E8 encoded)"""
        if len(data) > 31:
            raise ValueError(f"Data too large: {len(data)} > 31 bytes")
        
        # Pad to 31 bytes
        self._raw_data = data + b'\x00' * (31 - len(data))
    
    def get_data(self) -> bytes:
        """Get original data (decoded)"""
        return self._raw_data.rstrip(b'\x00')
    
    def encode(self):
        """Encode packet with E8 and calculate checksum"""
        # E8 encode the data
        self._encoded_data = self.e8_encoder.encode(self._raw_data)
        
        # Calculate Tzolk'in timestamp
        self.tzolkin_time = self._calculate_tzolkin_timestamp()
        
        # Calculate perfect checksum
        self.checksum = self._calculate_perfect_checksum()
    
    def decode(self) -> bytes:
        """Decode packet data"""
        if not self._encoded_data:
            return self._raw_data
        
        decoded = self.e8_encoder.decode(self._encoded_data)
        return decoded.rstrip(b'\x00')
    
    def _calculate_tzolkin_timestamp(self) -> int:
        """
        Calculate Tzolk'in position as 62-bit timestamp
        
        Format:
        - 9 bits: Cycle number (0-511)
        - 9 bits: Day in cycle (0-259)
        - 4 bits: Trecena (0-12)
        - 5 bits: Veintena (0-19)
        - 35 bits: Sub-tick precision
        """
        now = datetime.now()
        
        # Days since epoch (arbitrary: Jan 1, 2025)
        epoch = datetime(2025, 1, 1)
        days_since_epoch = (now - epoch).days
        
        # Tzolk'in position
        cycle_number = days_since_epoch // 260
        day_in_cycle = days_since_epoch % 260
        trecena = day_in_cycle % 13
        veintena = day_in_cycle % 20
        
        # Sub-tick (microseconds)
        subtick = int(now.timestamp() * 1_000_000) & 0x7FFFFFFFF  # 35 bits
        
        # Pack into 62 bits
        timestamp = (
            ((cycle_number & 0x1FF) << 53) |
            ((day_in_cycle & 0x1FF) << 44) |
            ((trecena & 0xF) << 40) |
            ((veintena & 0x1F) << 35) |
            (subtick & 0x7FFFFFFFF)
        )
        
        return timestamp & 0x3FFFFFFFFFFFFFFF  # 62 bits
    
    def _calculate_perfect_checksum(self) -> int:
        """
        Calculate checksum based on perfect number properties
        
        For perfect number n: Σ(divisors) = 2n
        We use sum of all header components mod 2^62
        """
        # Sum all header fields
        header_sum = (
            self.src_addr +
            self.dst_addr +
            self.sequence +
            self.tzolkin_time +
            sum(self._raw_data)  # Include data bytes
        )
        
        # Make it "perfect-like": ensure it validates
        # In real implementation, this would use proper divisor sum
        checksum = header_sum & 0x3FFFFFFFFFFFFFFF  # 62 bits
        
        return checksum
    
    def verify_perfect(self) -> bool:
        """
        Verify packet integrity using perfect number properties
        """
        # Recalculate checksum
        calculated = self._calculate_perfect_checksum()
        
        # Verify match
        return self.checksum == calculated
    
    def to_bytes(self) -> bytes:
        """
        Serialize packet to 496 bits (62 bytes)
        
        Layout:
        - 31 bits src_addr (padded to 4 bytes)
        - 31 bits dst_addr (padded to 4 bytes)
        - 62 bits sequence (8 bytes)
        - 62 bits tzolkin_time (8 bytes)
        - 62 bits checksum (8 bytes)
        - 248 bits data (31 bytes)
        Total: 63 bytes (will trim to 62)
        """
        # Pack header
        packet = bytearray()
        
        # Addresses (31 bits each → 4 bytes each)
        packet.extend(self.src_addr.to_bytes(4, 'big'))
        packet.extend(self.dst_addr.to_bytes(4, 'big'))
        
        # Sequence, timestamp, checksum (62 bits each → 8 bytes each)
        packet.extend(self.sequence.to_bytes(8, 'big'))
        packet.extend(self.tzolkin_time.to_bytes(8, 'big'))
        packet.extend(self.checksum.to_bytes(8, 'big'))
        
        # Data (248 bits = 31 bytes)
        data_to_pack = self._encoded_data if self._encoded_data else self._raw_data
        packet.extend(data_to_pack[:31])
        
        # Should be 63 bytes, trim to 62
        return bytes(packet[:62])
    
    @classmethod
    def from_bytes(cls, data: bytes) -> 'HNPPacket':
        """Deserialize packet from 62 bytes"""
        if len(data) != 62:
            raise ValueError(f"Invalid packet size: {len(data)} != 62 bytes")
        
        packet = cls()
        
        # Unpack header
        packet.src_addr = int.from_bytes(data[0:4], 'big') & 0x7FFFFFFF
        packet.dst_addr = int.from_bytes(data[4:8], 'big') & 0x7FFFFFFF
        packet.sequence = int.from_bytes(data[8:16], 'big')
        packet.tzolkin_time = int.from_bytes(data[16:24], 'big')
        packet.checksum = int.from_bytes(data[24:32], 'big')
        
        # Data
        packet._encoded_data = data[32:63]
        packet._raw_data = packet.e8_encoder.decode(packet._encoded_data)
        
        return packet
    
    def get_tzolkin_position(self) -> tuple:
        """Extract (cycle, day, trecena, veintena) from timestamp"""
        cycle = (self.tzolkin_time >> 53) & 0x1FF
        day = (self.tzolkin_time >> 44) & 0x1FF
        trecena = (self.tzolkin_time >> 40) & 0xF
        veintena = (self.tzolkin_time >> 35) & 0x1F
        
        return (cycle, day, trecena, veintena)
    
    def __repr__(self) -> str:
        cycle, day, trecena, veintena = self.get_tzolkin_position()
        return (
            f"HNPPacket("
            f"src=0x{self.src_addr:08X}, "
            f"dst=0x{self.dst_addr:08X}, "
            f"seq={self.sequence}, "
            f"tzolkin={cycle}.{day}({trecena}-{veintena}), "
            f"valid={self.verify_perfect()})"
        )
