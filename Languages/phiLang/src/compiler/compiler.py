#!/usr/bin/env python3
"""
ΦLang Compiler
Compiles ΦLang source code to bytecode and decompiles back

Author: Lichen Collective (Bryan Ouellette & Claude AI)
Version: 1.0.0
License: Apache 2.0
"""

import re
import sys
import struct
import pickle
from typing import List, Tuple, Optional, Dict, Any
from dataclasses import dataclass
from pathlib import Path

# Import utilities
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.primes import is_prime, get_prime_index
from utils.perfects import is_perfect, get_perfect_index


# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class Token:
    """Lexical token"""
    type: str
    value: Any
    line: int
    column: int


@dataclass
class Instruction:
    """Parsed ΦLang instruction"""
    prime: int
    perfect: int
    parameter: str
    line: int
    
    def __repr__(self):
        return f"[{self.prime}-{self.perfect}] :: Ψ({self.parameter})"


@dataclass
class BytecodeInstruction:
    """Compiled bytecode instruction"""
    vector: List[float]  # 496-dimensional vector
    metadata: Dict[str, Any]
    
    def serialize(self) -> bytes:
        """Serialize to bytes"""
        return pickle.dumps({
            'vector': self.vector,
            'metadata': self.metadata
        })
    
    @staticmethod
    def deserialize(data: bytes) -> 'BytecodeInstruction':
        """Deserialize from bytes"""
        obj = pickle.loads(data)
        return BytecodeInstruction(
            vector=obj['vector'],
            metadata=obj['metadata']
        )


# ============================================================================
# LEXER
# ============================================================================

class Lexer:
    """Lexical analyzer for ΦLang"""
    
    TOKEN_PATTERNS = [
        ('COMMENT', r'#[^\n]*'),
        ('LBRACKET', r'\['),
        ('RBRACKET', r'\]'),
        ('DOUBLE_COLON', r'::'),
        ('DASH', r'-'),
        ('PSI', r'Ψ'),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('NUMBER', r'\d+'),
        ('SYMBOL', r'[ΦπΔ∞⟷↔→←⊕⊗∅]'),
        ('IDENT', r'[a-zA-Z_][a-zA-Z0-9_\.]*'),
        ('STRING', r'"[^"]*"'),
        ('EQUALS', r'='),
        ('WHITESPACE', r'[ \t]+'),
        ('NEWLINE', r'\n'),
    ]
    
    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
    
    def tokenize(self) -> List[Token]:
        """Tokenize source code"""
        while self.pos < len(self.source):
            matched = False
            
            for token_type, pattern in self.TOKEN_PATTERNS:
                regex = re.compile(pattern)
                match = regex.match(self.source, self.pos)
                
                if match:
                    value = match.group(0)
                    
                    # Skip whitespace and comments
                    if token_type not in ('WHITESPACE', 'COMMENT'):
                        self.tokens.append(Token(
                            type=token_type,
                            value=value,
                            line=self.line,
                            column=self.column
                        ))
                    
                    # Update position
                    self.pos = match.end()
                    if token_type == 'NEWLINE':
                        self.line += 1
                        self.column = 1
                    else:
                        self.column += len(value)
                    
                    matched = True
                    break
            
            if not matched:
                raise SyntaxError(
                    f"Unexpected character '{self.source[self.pos]}' "
                    f"at line {self.line}, column {self.column}"
                )
        
        return self.tokens


# ============================================================================
# PARSER
# ============================================================================

class Parser:
    """Syntactic parser for ΦLang"""
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        self.instructions: List[Instruction] = []
    
    def parse(self) -> List[Instruction]:
        """Parse tokens into instructions"""
        while self.pos < len(self.tokens):
            # Skip newlines
            if self.current_token().type == 'NEWLINE':
                self.advance()
                continue
            
            instruction = self.parse_instruction()
            if instruction:
                self.instructions.append(instruction)
        
        return self.instructions
    
    def current_token(self) -> Token:
        """Get current token"""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return Token('EOF', None, 0, 0)
    
    def advance(self) -> Token:
        """Advance to next token"""
        token = self.current_token()
        self.pos += 1
        return token
    
    def expect(self, token_type: str) -> Token:
        """Expect specific token type"""
        token = self.current_token()
        if token.type != token_type:
            raise SyntaxError(
                f"Expected {token_type}, got {token.type} "
                f"at line {token.line}, column {token.column}"
            )
        return self.advance()
    
    def parse_instruction(self) -> Optional[Instruction]:
        """Parse single instruction: [prime-perfect] :: Ψ(parameter)"""
        # [
        self.expect('LBRACKET')
        
        # prime
        prime_token = self.expect('NUMBER')
        prime = int(prime_token.value)
        
        # -
        self.expect('DASH')
        
        # perfect
        perfect_token = self.expect('NUMBER')
        perfect = int(perfect_token.value)
        
        # ]
        self.expect('RBRACKET')
        
        # ::
        self.expect('DOUBLE_COLON')
        
        # Ψ
        self.expect('PSI')
        
        # (
        self.expect('LPAREN')
        
        # parameter (can be complex)
        parameter = self.parse_parameter()
        
        # )
        self.expect('RPAREN')
        
        return Instruction(
            prime=prime,
            perfect=perfect,
            parameter=parameter,
            line=prime_token.line
        )
    
    def parse_parameter(self) -> str:
        """Parse parameter (everything until closing paren)"""
        parts = []
        depth = 0
        
        while True:
            token = self.current_token()
            
            if token.type == 'RPAREN' and depth == 0:
                break
            
            if token.type == 'LPAREN':
                depth += 1
            elif token.type == 'RPAREN':
                depth -= 1
            
            parts.append(token.value)
            self.advance()
        
        return ''.join(parts)


# ============================================================================
# VALIDATOR
# ============================================================================

class Validator:
    """Validates ΦLang instructions"""
    
    @staticmethod
    def validate(instruction: Instruction) -> bool:
        """Validate single instruction"""
        # Check prime
        if not is_prime(instruction.prime):
            raise ValueError(
                f"Invalid prime number {instruction.prime} "
                f"at line {instruction.line}"
            )
        
        # Check perfect
        if not is_perfect(instruction.perfect):
            raise ValueError(
                f"Invalid perfect number {instruction.perfect} "
                f"at line {instruction.line}"
            )
        
        # Check compatibility (basic)
        # More sophisticated checks could be added here
        
        return True
    
    @staticmethod
    def validate_all(instructions: List[Instruction]) -> bool:
        """Validate all instructions"""
        for instruction in instructions:
            Validator.validate(instruction)
        return True


# ============================================================================
# ENCODER
# ============================================================================

class Encoder:
    """Encodes instructions to 496D vectors"""
    
    @staticmethod
    def embed_prime(prime: int) -> List[float]:
        """Embed prime number into 8D vector"""
        import math
        
        idx = get_prime_index(prime)
        
        return [
            math.log(prime),                    # 0: log
            math.sqrt(prime),                   # 1: sqrt
            prime % 8,                          # 2: mod 8
            idx,                                # 3: prime index
            prime % 2,                          # 4: parity
            math.sin(2 * math.pi / prime),      # 5: sin
            math.cos(2 * math.pi / prime),      # 6: cos
            len(str(prime))                     # 7: digit count
        ]
    
    @staticmethod
    def embed_perfect(perfect: int) -> List[float]:
        """Embed perfect number into 8D vector"""
        import math
        
        idx = get_perfect_index(perfect)
        divisors = [i for i in range(1, perfect) if perfect % i == 0]
        
        return [
            math.log(perfect),                  # 0: log
            math.sqrt(perfect),                 # 1: sqrt
            sum(divisors) / perfect,            # 2: sigma/n (should be 2.0)
            len(divisors),                      # 3: tau (number of divisors)
            perfect % 496,                      # 4: mod 496
            math.sin(2 * math.pi * perfect / 260),  # 5: Tzolk'in phase sin
            math.cos(2 * math.pi * perfect / 260),  # 6: Tzolk'in phase cos
            idx                                 # 7: perfect index
        ]
    
    @staticmethod
    def embed_parameter(parameter: str) -> List[float]:
        """Embed parameter into 480D vector"""
        # Simple hash-based embedding
        # In production, use proper NLP embedding
        import hashlib
        
        # Hash to bytes
        hash_bytes = hashlib.sha256(parameter.encode()).digest()
        
        # Convert to 480D vector (repeat hash 15 times: 32 bytes * 15 = 480 bytes)
        vector = []
        for i in range(15):
            hash_i = hashlib.sha256(f"{parameter}:{i}".encode()).digest()
            vector.extend([b / 255.0 for b in hash_i])
        
        return vector[:480]
    
    @staticmethod
    def encode(instruction: Instruction) -> BytecodeInstruction:
        """Encode instruction to 496D vector"""
        # Embed components
        prime_vec = Encoder.embed_prime(instruction.prime)
        perfect_vec = Encoder.embed_perfect(instruction.perfect)
        param_vec = Encoder.embed_parameter(instruction.parameter)
        
        # Concatenate
        vector = prime_vec + perfect_vec + param_vec
        
        # Ensure 496D
        assert len(vector) == 496, f"Vector dimension mismatch: {len(vector)}"
        
        # Create bytecode instruction
        return BytecodeInstruction(
            vector=vector,
            metadata={
                'prime': instruction.prime,
                'perfect': instruction.perfect,
                'parameter': instruction.parameter,
                'line': instruction.line
            }
        )


# ============================================================================
# DECODER
# ============================================================================

class Decoder:
    """Decodes bytecode back to instructions"""
    
    @staticmethod
    def decode_prime(vector: List[float]) -> int:
        """Decode prime from 8D vector"""
        # Use prime index (component 3)
        idx = int(round(vector[3]))
        
        # Get prime at index
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        if idx < len(primes):
            return primes[idx]
        
        # Fallback to metadata
        return None
    
    @staticmethod
    def decode_perfect(vector: List[float]) -> int:
        """Decode perfect from 8D vector"""
        # Use perfect index (component 7)
        idx = int(round(vector[7]))
        
        # Get perfect at index
        perfects = [6, 28, 496, 8128]
        if idx < len(perfects):
            return perfects[idx]
        
        # Fallback to metadata
        return None
    
    @staticmethod
    def decode(bytecode: BytecodeInstruction) -> Instruction:
        """Decode bytecode to instruction"""
        # Try to decode from vector
        prime_vec = bytecode.vector[:8]
        perfect_vec = bytecode.vector[8:16]
        
        prime = Decoder.decode_prime(prime_vec)
        perfect = Decoder.decode_perfect(perfect_vec)
        
        # Fallback to metadata if decoding fails
        if prime is None:
            prime = bytecode.metadata['prime']
        if perfect is None:
            perfect = bytecode.metadata['perfect']
        
        parameter = bytecode.metadata['parameter']
        line = bytecode.metadata['line']
        
        return Instruction(
            prime=prime,
            perfect=perfect,
            parameter=parameter,
            line=line
        )


# ============================================================================
# COMPILER
# ============================================================================

class Compiler:
    """Main compiler class"""
    
    def __init__(self):
        self.lexer = None
        self.parser = None
        self.validator = Validator()
        self.encoder = Encoder()
    
    def compile(self, source: str) -> List[BytecodeInstruction]:
        """Compile source code to bytecode"""
        # Lex
        self.lexer = Lexer(source)
        tokens = self.lexer.tokenize()
        
        # Parse
        self.parser = Parser(tokens)
        instructions = self.parser.parse()
        
        # Validate
        self.validator.validate_all(instructions)
        
        # Encode
        bytecode = [self.encoder.encode(inst) for inst in instructions]
        
        return bytecode
    
    def decompile(self, bytecode: List[BytecodeInstruction]) -> str:
        """Decompile bytecode to source code"""
        decoder = Decoder()
        instructions = [decoder.decode(bc) for bc in bytecode]
        
        # Generate source
        lines = []
        for inst in instructions:
            lines.append(str(inst))
        
        return '\n'.join(lines)
    
    def compile_file(self, input_path: str, output_path: str):
        """Compile source file to bytecode file"""
        # Read source
        with open(input_path, 'r') as f:
            source = f.read()
        
        # Compile
        bytecode = self.compile(source)
        
        # Write bytecode
        with open(output_path, 'wb') as f:
            # Magic number
            f.write(b'PHI\x00')
            # Version
            f.write(struct.pack('H', 1))  # version 1.0
            # Number of instructions
            f.write(struct.pack('I', len(bytecode)))
            # Instructions
            for bc in bytecode:
                data = bc.serialize()
                f.write(struct.pack('I', len(data)))
                f.write(data)
    
    def decompile_file(self, input_path: str, output_path: str):
        """Decompile bytecode file to source file"""
        bytecode = []
        
        # Read bytecode
        with open(input_path, 'rb') as f:
            # Check magic number
            magic = f.read(4)
            if magic != b'PHI\x00':
                raise ValueError("Invalid bytecode file (bad magic number)")
            
            # Check version
            version = struct.unpack('H', f.read(2))[0]
            if version != 1:
                raise ValueError(f"Unsupported bytecode version: {version}")
            
            # Read instructions
            num_instructions = struct.unpack('I', f.read(4))[0]
            for _ in range(num_instructions):
                length = struct.unpack('I', f.read(4))[0]
                data = f.read(length)
                bc = BytecodeInstruction.deserialize(data)
                bytecode.append(bc)
        
        # Decompile
        source = self.decompile(bytecode)
        
        # Write source
        with open(output_path, 'w') as f:
            f.write(source)


# ============================================================================
# CLI
# ============================================================================

def main():
    """Command-line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='ΦLang Compiler - Compile and decompile ΦLang code'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command')
    
    # Compile command
    compile_parser = subparsers.add_parser('compile', help='Compile source to bytecode')
    compile_parser.add_argument('input', help='Input source file (.phi)')
    compile_parser.add_argument('-o', '--output', help='Output bytecode file (.phic)')
    
    # Decompile command
    decompile_parser = subparsers.add_parser('decompile', help='Decompile bytecode to source')
    decompile_parser.add_argument('input', help='Input bytecode file (.phic)')
    decompile_parser.add_argument('-o', '--output', help='Output source file (.phi)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    compiler = Compiler()
    
    if args.command == 'compile':
        output = args.output or args.input.replace('.phi', '.phic')
        print(f"Compiling {args.input} -> {output}")
        compiler.compile_file(args.input, output)
        print(f"✅ Compilation successful!")
    
    elif args.command == 'decompile':
        output = args.output or args.input.replace('.phic', '_decompiled.phi')
        print(f"Decompiling {args.input} -> {output}")
        compiler.decompile_file(args.input, output)
        print(f"✅ Decompilation successful!")


if __name__ == '__main__':
    main()
