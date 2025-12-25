"""
Tests for ΦLang compiler
"""

import pytest
from src.compiler.parser import Parser
from src.compiler.validator import Validator
from src.compiler.encoder import Encoder
from src.compiler.decoder import Decoder


class TestParser:
    """Test parser"""
    
    def test_basic_instruction(self):
        """Test parsing basic instruction"""
        parser = Parser()
        source = "[7-496] :: Ψ(Φ)"
        ast = parser.parse(source)
        
        assert len(ast) == 1
        assert ast[0]['prime'] == 7
        assert ast[0]['perfect'] == 496
        assert ast[0]['parameter'] == 'Φ'
    
    def test_multiple_instructions(self):
        """Test parsing multiple instructions"""
        parser = Parser()
        source = """
        [2-6] :: Ψ(1)
        [7-496] :: Ψ(Φ)
        [13-28] :: Ψ(0)
        """
        ast = parser.parse(source)
        
        assert len(ast) == 3
    
    def test_comments(self):
        """Test parsing with comments"""
        parser = Parser()
        source = """
        # Initialize
        [2-6] :: Ψ(1)
        
        # Optimize
        [7-496] :: Ψ(Φ)
        """
        ast = parser.parse(source)
        
        assert len(ast) == 2


class TestValidator:
    """Test validator"""
    
    def test_valid_instruction(self):
        """Test validating valid instruction"""
        validator = Validator()
        ast = [{'prime': 7, 'perfect': 496, 'parameter': 'Φ'}]
        
        # Should not raise
        validator.validate(ast)
    
    def test_invalid_prime(self):
        """Test validating invalid prime"""
        validator = Validator()
        ast = [{'prime': 8, 'perfect': 496, 'parameter': 'Φ'}]
        
        with pytest.raises(Exception):
            validator.validate(ast)
    
    def test_invalid_perfect(self):
        """Test validating invalid perfect"""
        validator = Validator()
        ast = [{'prime': 7, 'perfect': 100, 'parameter': 'Φ'}]
        
        with pytest.raises(Exception):
            validator.validate(ast)


class TestEncoder:
    """Test encoder"""
    
    def test_encode_basic(self):
        """Test encoding basic instruction"""
        encoder = Encoder()
        ast = [{'prime': 7, 'perfect': 496, 'parameter': 'Φ'}]
        
        bytecode = encoder.encode(ast)
        
        assert isinstance(bytecode, bytes)
        assert len(bytecode) > 0
    
    def test_encode_decode_roundtrip(self):
        """Test encode-decode round trip"""
        encoder = Encoder()
        decoder = Decoder()
        
        original_ast = [
            {'prime': 7, 'perfect': 496, 'parameter': 'Φ'},
            {'prime': 13, 'perfect': 28, 'parameter': '0'}
        ]
        
        bytecode = encoder.encode(original_ast)
        decoded_ast = decoder.decode(bytecode)
        
        assert len(decoded_ast) == len(original_ast)
        assert decoded_ast[0]['prime'] == original_ast[0]['prime']


class TestIntegration:
    """Integration tests"""
    
    def test_full_pipeline(self):
        """Test complete compile-execute-decompile pipeline"""
        # Source
        source = "[7-496] :: Ψ(Φ)"
        
        # Parse
        parser = Parser()
        ast = parser.parse(source)
        
        # Validate
        validator = Validator()
        validator.validate(ast)
        
        # Encode
        encoder = Encoder()
        bytecode = encoder.encode(ast)
        
        # Decode
        decoder = Decoder()
        decoded_ast = decoder.decode(bytecode)
        
        # Verify
        assert len(decoded_ast) == len(ast)
        assert decoded_ast[0]['prime'] == ast[0]['prime']


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
