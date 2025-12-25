"""
Prime number utilities for ΦLang
"""

import math
from typing import List, Optional


def is_prime(n: int) -> bool:
    """
    Test if n is prime using trial division
    
    Args:
        n: Number to test
        
    Returns:
        True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def is_prime_miller_rabin(n: int, k: int = 5) -> bool:
    """
    Miller-Rabin primality test (probabilistic)
    
    Args:
        n: Number to test
        k: Number of rounds (higher = more accurate)
        
    Returns:
        True if n is probably prime, False if composite
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop
    import random
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True


def next_prime(n: int) -> int:
    """
    Find the next prime number after n
    
    Args:
        n: Starting number
        
    Returns:
        Next prime after n
    """
    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate


def primes_up_to(n: int) -> List[int]:
    """
    Generate all primes up to n using Sieve of Eratosthenes
    
    Args:
        n: Upper limit
        
    Returns:
        List of all primes <= n
    """
    if n < 2:
        return []
    
    # Initialize sieve
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    # Sieve
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    
    # Collect primes
    return [i for i in range(n + 1) if sieve[i]]


def prime_factorization(n: int) -> List[int]:
    """
    Get prime factorization of n
    
    Args:
        n: Number to factor
        
    Returns:
        List of prime factors (with repetition)
    """
    factors = []
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    if n > 1:
        factors.append(n)
    
    return factors


def nth_prime(n: int) -> int:
    """
    Get the nth prime number (1-indexed)
    
    Args:
        n: Index (1 = first prime = 2)
        
    Returns:
        The nth prime number
    """
    if n == 1:
        return 2
    
    count = 1
    candidate = 3
    
    while count < n:
        if is_prime(candidate):
            count += 1
        if count < n:
            candidate += 2
    
    return candidate


def prime_pi(x: float) -> int:
    """
    Prime counting function π(x)
    Number of primes <= x
    
    Args:
        x: Upper limit
        
    Returns:
        Number of primes <= x
    """
    return len(primes_up_to(int(x)))


# Standard ΦLang primes (used as actions)
PHILANG_PRIMES = {
    2: "Duality",
    3: "Fusion", 
    5: "Mutation",
    7: "Cycle",
    11: "Interface",
    13: "Anchor",
    17: "Transform",
    19: "Validate",
    23: "Compute",
    29: "Sync",
    31: "Merge",
    37: "Split",
    41: "Balance",
    43: "Adapt",
    47: "Evolve",
    53: "Optimize",
}


def get_prime_name(p: int) -> Optional[str]:
    """
    Get the ΦLang name for a prime
    
    Args:
        p: Prime number
        
    Returns:
        Name if defined, None otherwise
    """
    return PHILANG_PRIMES.get(p)


def get_prime_from_name(name: str) -> Optional[int]:
    """
    Get prime number from ΦLang name
    
    Args:
        name: Action name
        
    Returns:
        Prime number if found, None otherwise
    """
    for p, n in PHILANG_PRIMES.items():
        if n.lower() == name.lower():
            return p
    return None
