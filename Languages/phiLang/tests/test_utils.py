"""
Tests for ΦLang utilities
"""

import pytest
from src.utils.primes import is_prime, next_prime, primes_up_to
from src.utils.perfects import is_perfect, sum_of_divisors


class TestPrimes:
    """Test prime number utilities"""
    
    def test_is_prime(self):
        """Test prime checking"""
        assert is_prime(2)
        assert is_prime(3)
        assert is_prime(5)
        assert is_prime(7)
        assert is_prime(11)
        assert is_prime(13)
        
        assert not is_prime(0)
        assert not is_prime(1)
        assert not is_prime(4)
        assert not is_prime(6)
        assert not is_prime(8)
        assert not is_prime(9)
    
    def test_next_prime(self):
        """Test finding next prime"""
        assert next_prime(2) == 3
        assert next_prime(3) == 5
        assert next_prime(7) == 11
        assert next_prime(10) == 11
    
    def test_primes_up_to(self):
        """Test generating primes"""
        primes = primes_up_to(20)
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        assert primes == expected


class TestPerfects:
    """Test perfect number utilities"""
    
    def test_is_perfect(self):
        """Test perfect number checking"""
        assert is_perfect(6)
        assert is_perfect(28)
        assert is_perfect(496)
        assert is_perfect(8128)
        
        assert not is_perfect(1)
        assert not is_perfect(10)
        assert not is_perfect(100)
    
    def test_sum_of_divisors(self):
        """Test sum of divisors"""
        assert sum_of_divisors(6) == 12  # 1+2+3+6
        assert sum_of_divisors(28) == 56  # 1+2+4+7+14+28
        
        # Perfect numbers satisfy σ(n) = 2n
        assert sum_of_divisors(6) == 2 * 6
        assert sum_of_divisors(28) == 2 * 28


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
