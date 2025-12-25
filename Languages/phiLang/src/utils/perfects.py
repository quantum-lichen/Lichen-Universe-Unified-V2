"""
Perfect number utilities for ΦLang
"""

import math
from typing import List, Optional
from .primes import is_prime


def sum_of_divisors(n: int) -> int:
    """
    Calculate sum of all divisors of n (including n)
    
    Args:
        n: Number
        
    Returns:
        Sum of divisors (σ(n))
    """
    if n <= 0:
        return 0
    
    total = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    
    return total


def is_perfect(n: int) -> bool:
    """
    Test if n is a perfect number
    
    A perfect number equals the sum of its proper divisors
    (all divisors except itself)
    
    Args:
        n: Number to test
        
    Returns:
        True if n is perfect, False otherwise
    """
    if n < 6:
        return False
    
    return sum_of_divisors(n) == 2 * n


def is_mersenne_prime(p: int) -> bool:
    """
    Test if 2^p - 1 is prime (Mersenne prime)
    
    Args:
        p: Exponent (must be prime itself)
        
    Returns:
        True if 2^p - 1 is prime
    """
    if not is_prime(p):
        return False
    
    # Lucas-Lehmer test
    if p == 2:
        return True
    
    mersenne = (1 << p) - 1  # 2^p - 1
    
    # Lucas-Lehmer sequence
    s = 4
    for _ in range(p - 2):
        s = (s * s - 2) % mersenne
    
    return s == 0


def generate_perfect(p: int) -> Optional[int]:
    """
    Generate perfect number from Mersenne prime exponent
    
    Uses Euclid-Euler theorem:
    n = 2^(p-1) * (2^p - 1) where 2^p - 1 is Mersenne prime
    
    Args:
        p: Prime exponent
        
    Returns:
        Perfect number if valid, None otherwise
    """
    if not is_prime(p):
        return None
    
    if not is_mersenne_prime(p):
        return None
    
    return (1 << (p - 1)) * ((1 << p) - 1)


def known_perfect_numbers() -> List[int]:
    """
    Return list of known perfect numbers
    
    Returns:
        List of perfect numbers up to reasonable size
    """
    return [6, 28, 496, 8128, 33550336]


def mersenne_exponents() -> List[int]:
    """
    Return known Mersenne prime exponents
    
    Returns:
        List of primes p where 2^p - 1 is prime
    """
    # First known Mersenne exponents
    return [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127]


def next_perfect(n: int) -> Optional[int]:
    """
    Find next perfect number after n
    
    Args:
        n: Starting number
        
    Returns:
        Next perfect number, or None if too large
    """
    perfects = known_perfect_numbers()
    for p in perfects:
        if p > n:
            return p
    return None


def number_of_divisors(n: int) -> int:
    """
    Count number of divisors of n (τ(n))
    
    Args:
        n: Number
        
    Returns:
        Number of divisors
    """
    if n <= 0:
        return 0
    
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    
    return count


def proper_divisors(n: int) -> List[int]:
    """
    Get all proper divisors of n (excluding n itself)
    
    Args:
        n: Number
        
    Returns:
        List of proper divisors
    """
    if n <= 1:
        return []
    
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i and i != 1:
                divisors.append(n // i)
    
    # Remove n itself, keep sorted
    return sorted([d for d in divisors if d != n])


# Standard ΦLang perfect numbers (used as structures)
PHILANG_PERFECTS = {
    6: "Hex",
    28: "Cluster",
    496: "Dimension",
    8128: "Universe",
}


def get_perfect_name(n: int) -> Optional[str]:
    """
    Get the ΦLang name for a perfect number
    
    Args:
        n: Perfect number
        
    Returns:
        Name if defined, None otherwise
    """
    return PHILANG_PERFECTS.get(n)


def get_perfect_from_name(name: str) -> Optional[int]:
    """
    Get perfect number from ΦLang name
    
    Args:
        name: Structure name
        
    Returns:
        Perfect number if found, None otherwise
    """
    for n, nm in PHILANG_PERFECTS.items():
        if nm.lower() == name.lower():
            return n
    return None


def validate_perfect_structure(n: int) -> bool:
    """
    Validate if n is a valid ΦLang structure number
    
    Args:
        n: Number to validate
        
    Returns:
        True if n is in PHILANG_PERFECTS
    """
    return n in PHILANG_PERFECTS
