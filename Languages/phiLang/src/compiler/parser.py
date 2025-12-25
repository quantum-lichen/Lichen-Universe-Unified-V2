"""
ΦLang Compiler - Parser Module
Lexical analysis and parsing for ΦLang instructions
"""

import re
from dataclasses import dataclass
from typing import List, Optional, Tuple
from enum import Enum, auto


class TokenType(Enum):
    """Token types for ΦLang"""
    LBRACKET = auto()      # [
    RBRACKET = auto()      # ]
    DASH = auto()          # -
    DOUBLE_COLON = auto()  # ::
    PSI = auto()           # Ψ
    LPAREN = auto()        # (
    RPAREN = auto()        # )
    NUMBER = auto()        # 123
    SYMBOL = auto()        # Φ, π, ∞, Δ, etc.
    OPERATOR = auto()      # →, ↔, ⟷
    IDENTIFIER = auto()    # custom names
    COMMENT = auto()       # # ...
    NEWLINE = auto()       # \n
    EOF = auto()           # end of file


@dataclass
class Token:
    """Token with type, value, and position"""
    type: TokenType
    value: str
    line: int
    column: int
    
    def __repr__(self):
        return f"Token({self.type.name}, '{self.value}', {self.line}:{self.column})"


@dataclass
class Instruction:
    """Parsed ΦLang instruction"""
    prime: int
    perfect: int
    parameter: str
    line: int
    column: int
    
    def __repr__(self):
        return f"[{self.prime}-{self.perfect}] :: Ψ({self.parameter})"


class Lexer:
    """Lexical analyzer for ΦLang"""
    
    # Token patterns
    PATTERNS = [
        (TokenType.COMMENT, r'#[^\n]*'),
        (TokenType.DOUBLE_COLON, r'::'),
        (TokenType.LBRACKET, r'\['),
        (TokenType.RBRACKET, r'\]'),
        (TokenType.DASH, r'-'),
        (TokenType.PSI, r'Ψ'),
        (TokenType.LPAREN, r'\('),
        (TokenType.RPAREN, r'\)'),
        (TokenType.NUMBER, r'\d+'),
        (TokenType.SYMBOL, r'[ΦφπΠ∞Δ]'),
        (TokenType.OPERATOR, r'[→↔⟷⊕⊗]'),
        (TokenType.IDENTIFIER, r'[a-zA-Z_][a-zA-Z0-9_]*'),
        (TokenType.NEWLINE, r'\n'),
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
            # Skip whitespace (except newlines)
            if self.source[self.pos] in ' \t\r':
                self.advance()
                continue
            
            # Try to match token
            matched = False
            for token_type, pattern in self.PATTERNS:
                regex = re.compile(pattern)
                match = regex.match(self.source, self.pos)
                
                if match:
                    value = match.group(0)
                    
                    # Skip comments
                    if token_type == TokenType.COMMENT:
                        self.advance(len(value))
                        matched = True
                        break
                    
                    # Create token
                    token = Token(token_type, value, self.line, self.column)
                    self.tokens.append(token)
                    
                    # Advance position
                    self.advance(len(value))
                    matched = True
                    break
            
            if not matched:
                raise SyntaxError(
                    f"Unexpected character '{self.source[self.pos]}' "
                    f"at line {self.line}, column {self.column}"
                )
        
        # Add EOF token
        self.tokens.append(Token(TokenType.EOF, '', self.line, self.column))
        return self.tokens
    
    def advance(self, count: int = 1):
        """Advance position and track line/column"""
        for _ in range(count):
            if self.pos < len(self.source):
                if self.source[self.pos] == '\n':
                    self.line += 1
                    self.column = 1
                else:
                    self.column += 1
                self.pos += 1


class Parser:
    """Parser for ΦLang instructions"""
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        self.current_token = tokens[0] if tokens else None
    
    def parse(self) -> List[Instruction]:
        """Parse tokens into instructions"""
        instructions = []
        
        while self.current_token.type != TokenType.EOF:
            # Skip newlines
            if self.current_token.type == TokenType.NEWLINE:
                self.advance()
                continue
            
            # Parse instruction
            instruction = self.parse_instruction()
            if instruction:
                instructions.append(instruction)
        
        return instructions
    
    def parse_instruction(self) -> Optional[Instruction]:
        """
        Parse single instruction
        Grammar: [prime-perfect] :: Ψ(parameter)
        """
        start_line = self.current_token.line
        start_column = self.current_token.column
        
        # Expect [
        self.expect(TokenType.LBRACKET)
        
        # Parse prime
        prime_token = self.expect(TokenType.NUMBER)
        prime = int(prime_token.value)
        
        # Expect -
        self.expect(TokenType.DASH)
        
        # Parse perfect
        perfect_token = self.expect(TokenType.NUMBER)
        perfect = int(perfect_token.value)
        
        # Expect ]
        self.expect(TokenType.RBRACKET)
        
        # Expect ::
        self.expect(TokenType.DOUBLE_COLON)
        
        # Expect Ψ
        self.expect(TokenType.PSI)
        
        # Expect (
        self.expect(TokenType.LPAREN)
        
        # Parse parameter (anything until ))
        parameter = self.parse_parameter()
        
        # Expect )
        self.expect(TokenType.RPAREN)
        
        return Instruction(prime, perfect, parameter, start_line, start_column)
    
    def parse_parameter(self) -> str:
        """Parse parameter (can be complex expression)"""
        parts = []
        
        while self.current_token.type != TokenType.RPAREN:
            if self.current_token.type == TokenType.EOF:
                raise SyntaxError("Unexpected EOF while parsing parameter")
            
            parts.append(self.current_token.value)
            self.advance()
        
        return ''.join(parts)
    
    def expect(self, token_type: TokenType) -> Token:
        """Expect specific token type"""
        if self.current_token.type != token_type:
            raise SyntaxError(
                f"Expected {token_type.name}, got {self.current_token.type.name} "
                f"at line {self.current_token.line}, column {self.current_token.column}"
            )
        
        token = self.current_token
        self.advance()
        return token
    
    def advance(self):
        """Move to next token"""
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
            self.current_token = self.tokens[self.pos]


def parse_philang(source: str) -> List[Instruction]:
    """
    Main parsing function
    
    Args:
        source: ΦLang source code
    
    Returns:
        List of parsed instructions
    
    Example:
        >>> code = "[7-496] :: Ψ(Φ)"
        >>> instructions = parse_philang(code)
        >>> print(instructions[0])
        [7-496] :: Ψ(Φ)
    """
    # Tokenize
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    # Parse
    parser = Parser(tokens)
    instructions = parser.parse()
    
    return instructions


if __name__ == "__main__":
    # Test the parser
    test_code = """
    # Test program
    [7-496] :: Ψ(Φ)
    [3-28] :: Ψ(merge)
    [13-496] :: Ψ(0)
    """
    
    print("Testing ΦLang Parser:")
    print("=" * 50)
    print(f"Source:\n{test_code}")
    print("=" * 50)
    
    instructions = parse_philang(test_code)
    
    print("\nParsed Instructions:")
    for i, inst in enumerate(instructions, 1):
        print(f"{i}. {inst}")
    
    print("\n✓ Parser test successful!")
