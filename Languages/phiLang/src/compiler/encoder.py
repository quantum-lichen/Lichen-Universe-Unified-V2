"""
ΦLang Compiler - Encoder Module
Encodes instructions into 496-dimensional vectors
"""

import numpy as np
import struct
from typing import List, Dict
from .parser import Instruction


class Encoder:
    """Encodes ΦLang instructions to 496D vectors"""
    
    PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
    
    # Parameter symbol mappings
    SYMBOL_MAP = {
        'Φ': PHI,
        'φ': PHI,
        'π': np.pi,
        'Π': np.pi,
        '∞': float('inf'),
        'Δ': 1.0,  # Change/delta
        '0': 0.0,  # Ground state
        '1': 1.0,  # Unity
    }
    
    @staticmethod
    def embed_prime(p: int) -> np.ndarray:
        """
        Embed prime number into 8D vector
        
        Components:
        1. log(p)
        2. sqrt(p)
        3. p mod 8
        4. π(p) - prime counting function (approx)
        5. φ(p) - Euler's totient = p-1 for primes
        6. sin(2π/p)
        7. cos(2π/p)
        8. entropy(p) - normalized
        """
        vec = np.zeros(8)
        
        vec[0] = np.log(p)
        vec[1] = np.sqrt(p)
        vec[2] = p % 8
        vec[3] = p / np.log(p)  # Approx prime counting
        vec[4] = p - 1  # Totient for prime
        vec[5] = np.sin(2 * np.pi / p)
        vec[6] = np.cos(2 * np.pi / p)
        vec[7] = -np.log(p) / np.log(100)  # Normalized entropy
        
        return vec
    
    @staticmethod
    def embed_perfect(n: int) -> np.ndarray:
        """
        Embed perfect number into 8D vector
        
        Components:
        1. log(n)
        2. sqrt(n)
        3. σ(n)/n = 2 for perfect numbers
        4. τ(n) - number of divisors
        5. n mod 496
        6. sin(2πn/260) - Tzolk'in phase
        7. cos(2πn/260) - Tzolk'in phase
        8. packing density
        """
        vec = np.zeros(8)
        
        vec[0] = np.log(n)
        vec[1] = np.sqrt(n)
        vec[2] = 2.0  # σ(n)/n = 2 for perfect
        vec[3] = Encoder._count_divisors(n)
        vec[4] = n % 496
        vec[5] = np.sin(2 * np.pi * n / 260)
        vec[6] = np.cos(2 * np.pi * n / 260)
        vec[7] = np.log(n) / np.log(496)  # Packing density
        
        return vec
    
    @staticmethod
    def _count_divisors(n: int) -> int:
        """Count number of divisors"""
        count = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                count += 1
                if i != n // i:
                    count += 1
            i += 1
        return count
    
    @staticmethod
    def embed_parameter(param: str) -> np.ndarray:
        """
        Embed parameter into 480D vector
        
        For simplicity, we use a hash-based embedding
        In production, this would use learned embeddings
        """
        vec = np.zeros(480)
        
        # Parse parameter for known symbols
        value = 0.0
        for symbol, val in Encoder.SYMBOL_MAP.items():
            if symbol in param:
                if np.isinf(val):
                    value = 1e6  # Cap infinity
                else:
                    value += val
        
        # If no known symbols, use hash
        if value == 0.0:
            hash_val = hash(param) % 1000000
            value = hash_val / 1000000.0
        
        # Distribute value across vector using sinusoidal encoding
        for i in range(480):
            freq = (i + 1) / 480.0
            vec[i] = value * np.sin(2 * np.pi * freq * value)
            vec[i] += value * np.cos(2 * np.pi * freq * value) * 0.5
        
        # Normalize
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec /= norm
        
        return vec
    
    @staticmethod
    def encode_instruction(instruction: Instruction) -> np.ndarray:
        """
        Encode single instruction to 496D vector
        
        Format: [8D prime] + [8D perfect] + [480D parameter] = 496D
        """
        prime_vec = Encoder.embed_prime(instruction.prime)
        perfect_vec = Encoder.embed_perfect(instruction.perfect)
        param_vec = Encoder.embed_parameter(instruction.parameter)
        
        # Concatenate
        vector = np.concatenate([prime_vec, perfect_vec, param_vec])
        
        assert len(vector) == 496, f"Vector length is {len(vector)}, expected 496"
        
        return vector
    
    @staticmethod
    def encode_all(instructions: List[Instruction]) -> np.ndarray:
        """
        Encode all instructions to matrix
        
        Returns:
            Matrix of shape (n_instructions, 496)
        """
        vectors = []
        
        for instruction in instructions:
            vec = Encoder.encode_instruction(instruction)
            vectors.append(vec)
        
        return np.array(vectors)
    
    @staticmethod
    def to_bytecode(vectors: np.ndarray) -> bytes:
        """
        Convert vectors to bytecode
        
        Format:
        - 4 bytes: number of instructions
        - For each instruction:
          - 496 * 4 bytes: float32 values
        """
        n_instructions = vectors.shape[0]
        
        # Header: number of instructions
        bytecode = struct.pack('I', n_instructions)
        
        # Vectors: flatten and convert to float32
        for vec in vectors:
            vec_float32 = vec.astype(np.float32)
            bytecode += vec_float32.tobytes()
        
        return bytecode
    
    @staticmethod
    def from_bytecode(bytecode: bytes) -> np.ndarray:
        """
        Load vectors from bytecode
        
        Returns:
            Matrix of shape (n_instructions, 496)
        """
        # Read header
        n_instructions = struct.unpack('I', bytecode[:4])[0]
        
        # Read vectors
        offset = 4
        vectors = []
        
        for _ in range(n_instructions):
            # Read 496 float32 values
            vec_bytes = bytecode[offset:offset + 496 * 4]
            vec = np.frombuffer(vec_bytes, dtype=np.float32)
            vectors.append(vec)
            offset += 496 * 4
        
        return np.array(vectors)


def encode_philang(instructions: List[Instruction]) -> bytes:
    """
    Encode ΦLang instructions to bytecode
    
    Args:
        instructions: Parsed and validated instructions
    
    Returns:
        Bytecode (binary format)
    
    Example:
        >>> from parser import parse_philang
        >>> from validator import validate_philang
        >>> code = "[7-496] :: Ψ(Φ)"
        >>> instructions = parse_philang(code)
        >>> validate_philang(instructions)
        >>> bytecode = encode_philang(instructions)
        >>> print(f"Bytecode size: {len(bytecode)} bytes")
    """
    # Encode to vectors
    vectors = Encoder.encode_all(instructions)
    
    # Convert to bytecode
    bytecode = Encoder.to_bytecode(vectors)
    
    return bytecode


if __name__ == "__main__":
    # Test the encoder
    from parser import parse_philang
    from validator import validate_philang
    
    print("Testing ΦLang Encoder:")
    print("=" * 50)
    
    test_code = """
    [7-496] :: Ψ(Φ)
    [3-28] :: Ψ(merge)
    [13-496] :: Ψ(0)
    """
    
    print(f"Source code:\n{test_code}")
    print("=" * 50)
    
    # Parse
    instructions = parse_philang(test_code)
    print(f"Parsed {len(instructions)} instructions")
    
    # Validate
    validate_philang(instructions)
    print("✓ Validation passed")
    
    # Encode
    bytecode = encode_philang(instructions)
    print(f"✓ Encoded to {len(bytecode)} bytes")
    
    # Decode back
    vectors = Encoder.from_bytecode(bytecode)
    print(f"✓ Decoded to {vectors.shape} matrix")
    
    # Show first vector
    print(f"\nFirst instruction vector (496D):")
    print(f"  Prime embedding (8D): {vectors[0, :8]}")
    print(f"  Perfect embedding (8D): {vectors[0, 8:16]}")
    print(f"  Parameter embedding (480D): {vectors[0, 16:496][:5]}... (truncated)")
    print(f"  Vector norm: {np.linalg.norm(vectors[0]):.4f}")
    
    print("\n✓ Encoder test successful!")
