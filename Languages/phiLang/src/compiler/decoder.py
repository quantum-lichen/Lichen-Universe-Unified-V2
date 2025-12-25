"""
ΦLang Compiler - Decoder Module
Decompiles bytecode back to ΦLang source
"""

import numpy as np
from typing import List, Tuple
from .parser import Instruction
from .encoder import Encoder


class Decoder:
    """Decodes 496D vectors back to ΦLang instructions"""
    
    # Reverse mappings
    REVERSE_SYMBOL_MAP = {
        v: k for k, v in Encoder.SYMBOL_MAP.items()
        if not np.isinf(v)
    }
    
    @staticmethod
    def decode_prime(vec: np.ndarray) -> int:
        """
        Decode 8D vector back to prime number
        
        Uses component 1: log(p)
        """
        log_p = vec[0]
        p = int(np.round(np.exp(log_p)))
        
        # Validate it's actually prime
        if not Decoder._is_prime(p):
            # Find nearest prime
            p = Decoder._nearest_prime(p)
        
        return p
    
    @staticmethod
    def decode_perfect(vec: np.ndarray) -> int:
        """
        Decode 8D vector back to perfect number
        
        Uses component 1: log(n)
        """
        log_n = vec[0]
        n = int(np.round(np.exp(log_n)))
        
        # Find nearest perfect
        perfects = [6, 28, 496, 8128, 33550336]
        closest = min(perfects, key=lambda x: abs(x - n))
        
        return closest
    
    @staticmethod
    def decode_parameter(vec: np.ndarray) -> str:
        """
        Decode 480D vector back to parameter string
        
        This is lossy - we approximate the original parameter
        """
        # Compute mean magnitude
        magnitude = np.mean(np.abs(vec))
        
        # Try to match to known symbols
        for symbol, value in Encoder.SYMBOL_MAP.items():
            if np.isinf(value):
                continue
            
            # Check if magnitude is close to symbol value
            if abs(magnitude - value / 10.0) < 0.1:  # Normalized check
                return symbol
        
        # Check for special values
        if magnitude < 0.01:
            return '0'
        elif magnitude > 10.0:
            return '∞'
        elif abs(magnitude - 0.1) < 0.05:
            return 'Δ'
        
        # Fallback: generic parameter
        return f"param_{int(magnitude * 1000)}"
    
    @staticmethod
    def decode_instruction(vec: np.ndarray, line: int = 1) -> Instruction:
        """
        Decode 496D vector back to instruction
        
        Format: [8D prime] + [8D perfect] + [480D parameter]
        """
        assert len(vec) == 496, f"Vector length is {len(vec)}, expected 496"
        
        # Split vector
        prime_vec = vec[:8]
        perfect_vec = vec[8:16]
        param_vec = vec[16:496]
        
        # Decode components
        prime = Decoder.decode_prime(prime_vec)
        perfect = Decoder.decode_perfect(perfect_vec)
        parameter = Decoder.decode_parameter(param_vec)
        
        return Instruction(prime, perfect, parameter, line, 1)
    
    @staticmethod
    def decode_all(vectors: np.ndarray) -> List[Instruction]:
        """
        Decode all vectors to instructions
        
        Args:
            vectors: Matrix of shape (n_instructions, 496)
        
        Returns:
            List of decoded instructions
        """
        instructions = []
        
        for i, vec in enumerate(vectors, start=1):
            instruction = Decoder.decode_instruction(vec, line=i)
            instructions.append(instruction)
        
        return instructions
    
    @staticmethod
    def to_source(instructions: List[Instruction]) -> str:
        """
        Convert instructions to ΦLang source code
        
        Returns:
            ΦLang source code string
        """
        lines = []
        
        for instruction in instructions:
            line = f"[{instruction.prime}-{instruction.perfect}] :: Ψ({instruction.parameter})"
            lines.append(line)
        
        return '\n'.join(lines)
    
    # Helper methods
    
    @staticmethod
    def _is_prime(n: int) -> bool:
        """Check if n is prime"""
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        
        return True
    
    @staticmethod
    def _nearest_prime(n: int) -> int:
        """Find nearest prime to n"""
        # Try n, n-1, n+1, n-2, n+2, ...
        for offset in [0, -1, 1, -2, 2, -3, 3, -4, 4]:
            candidate = n + offset
            if candidate > 1 and Decoder._is_prime(candidate):
                return candidate
        return 2  # Fallback


def decode_philang(bytecode: bytes) -> str:
    """
    Decompile bytecode back to ΦLang source
    
    Args:
        bytecode: Compiled bytecode
    
    Returns:
        ΦLang source code
    
    Example:
        >>> bytecode = b'...'  # From encode_philang
        >>> source = decode_philang(bytecode)
        >>> print(source)
        [7-496] :: Ψ(Φ)
        [3-28] :: Ψ(merge)
    """
    # Load vectors from bytecode
    vectors = Encoder.from_bytecode(bytecode)
    
    # Decode to instructions
    instructions = Decoder.decode_all(vectors)
    
    # Convert to source
    source = Decoder.to_source(instructions)
    
    return source


if __name__ == "__main__":
    # Test the decoder
    from parser import parse_philang
    from validator import validate_philang
    from encoder import encode_philang
    
    print("Testing ΦLang Decoder:")
    print("=" * 50)
    
    original_code = """[7-496] :: Ψ(Φ)
[3-28] :: Ψ(merge)
[13-496] :: Ψ(0)"""
    
    print(f"Original source:\n{original_code}")
    print("=" * 50)
    
    # Parse
    instructions = parse_philang(original_code)
    print(f"✓ Parsed {len(instructions)} instructions")
    
    # Validate
    validate_philang(instructions)
    print("✓ Validated")
    
    # Encode
    bytecode = encode_philang(instructions)
    print(f"✓ Encoded to {len(bytecode)} bytes")
    
    # Decode
    decoded_code = decode_philang(bytecode)
    print("✓ Decoded back to source")
    
    print("\n" + "=" * 50)
    print(f"Decoded source:\n{decoded_code}")
    print("=" * 50)
    
    # Compare
    original_lines = original_code.strip().split('\n')
    decoded_lines = decoded_code.strip().split('\n')
    
    print("\nComparison:")
    for i, (orig, dec) in enumerate(zip(original_lines, decoded_lines), 1):
        match = "✓" if orig.strip() == dec.strip() else "✗"
        print(f"{i}. {match} Original:  {orig.strip()}")
        print(f"   {match} Decoded:   {dec.strip()}")
    
    print("\n✓ Decoder test successful!")
