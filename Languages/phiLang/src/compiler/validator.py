"""
ΦLang Compiler - Validator Module
Validates instructions for mathematical correctness
"""

from typing import List, Tuple
from .parser import Instruction


class ValidationError(Exception):
    """Raised when instruction validation fails"""
    pass


class Validator:
    """Validates ΦLang instructions"""
    
    # Known perfect numbers (first 5)
    PERFECT_NUMBERS = [6, 28, 496, 8128, 33550336]
    
    @staticmethod
    def is_prime(n: int) -> bool:
        """
        Check if n is prime
        
        Uses trial division with optimizations:
        - Check 2 and 3 first
        - Then check 6k±1 form
        """
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
    def is_perfect(n: int) -> bool:
        """
        Check if n is perfect number
        
        A perfect number equals the sum of its proper divisors
        n = Σ(divisors of n, excluding n)
        """
        if n < 6:
            return False
        
        # Quick check against known perfects
        if n in Validator.PERFECT_NUMBERS:
            return True
        
        # For large numbers, use Euclid-Euler theorem
        # Perfect numbers have form 2^(p-1) * (2^p - 1)
        # where 2^p - 1 is Mersenne prime
        
        # Find if n = 2^k * m where m is odd
        k = 0
        m = n
        while m % 2 == 0:
            k += 1
            m //= 2
        
        # Check if m = 2^(k+1) - 1 (Mersenne form)
        if m == (2 ** (k + 1)) - 1:
            # Check if m is prime
            return Validator.is_prime(m)
        
        # Fallback: compute sum of divisors
        divisor_sum = 1  # 1 is always a divisor
        i = 2
        while i * i <= n:
            if n % i == 0:
                divisor_sum += i
                if i != n // i:  # Avoid counting square root twice
                    divisor_sum += n // i
            i += 1
        
        return divisor_sum == n
    
    @staticmethod
    def get_prime_name(p: int) -> str:
        """Get semantic name for prime number"""
        prime_names = {
            2: "Duality",
            3: "Fusion",
            5: "Mutation",
            7: "Cycle",
            11: "Interface",
            13: "Anchor",
            17: "Oracle",
            19: "Guardian",
            23: "Catalyst",
            29: "Weaver",
            31: "Sentinel",
        }
        return prime_names.get(p, f"Prime-{p}")
    
    @staticmethod
    def get_perfect_name(n: int) -> str:
        """Get semantic name for perfect number"""
        perfect_names = {
            6: "Hex",
            28: "Cluster",
            496: "Dimension",
            8128: "Universe",
            33550336: "Cosmos",
        }
        return perfect_names.get(n, f"Perfect-{n}")
    
    def validate_instruction(self, instruction: Instruction) -> Tuple[bool, str]:
        """
        Validate single instruction
        
        Returns:
            (is_valid, error_message)
        """
        # Validate prime
        if not self.is_prime(instruction.prime):
            return False, (
                f"Invalid prime number: {instruction.prime}\n"
                f"  {instruction.prime} is not prime\n"
                f"  Valid primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, ..."
            )
        
        # Validate perfect
        if not self.is_perfect(instruction.perfect):
            # Calculate what it should be
            divisor_sum = sum(i for i in range(1, instruction.perfect) 
                             if instruction.perfect % i == 0)
            
            return False, (
                f"Invalid perfect number: {instruction.perfect}\n"
                f"  σ({instruction.perfect}) = {divisor_sum} ≠ 2×{instruction.perfect}\n"
                f"  Valid perfect numbers: 6, 28, 496, 8128, ..."
            )
        
        # Validate parameter syntax (basic check)
        param = instruction.parameter
        if not param:
            return False, "Parameter cannot be empty"
        
        return True, ""
    
    def validate_all(self, instructions: List[Instruction]) -> Tuple[bool, List[str]]:
        """
        Validate all instructions
        
        Returns:
            (all_valid, error_messages)
        """
        errors = []
        
        for i, instruction in enumerate(instructions, 1):
            is_valid, error_msg = self.validate_instruction(instruction)
            
            if not is_valid:
                errors.append(
                    f"Instruction {i} (line {instruction.line}): {error_msg}"
                )
        
        return len(errors) == 0, errors
    
    @staticmethod
    def suggest_prime(n: int) -> int:
        """Suggest nearest prime number"""
        # Check n-1, n, n+1, ...
        for offset in [0, -1, 1, -2, 2, -3, 3]:
            candidate = n + offset
            if candidate > 1 and Validator.is_prime(candidate):
                return candidate
        return 2  # Fallback
    
    @staticmethod
    def suggest_perfect(n: int) -> int:
        """Suggest nearest perfect number"""
        perfects = [6, 28, 496, 8128, 33550336]
        
        # Find closest
        closest = perfects[0]
        min_diff = abs(n - perfects[0])
        
        for p in perfects:
            diff = abs(n - p)
            if diff < min_diff:
                min_diff = diff
                closest = p
        
        return closest


def validate_philang(instructions: List[Instruction]) -> None:
    """
    Validate ΦLang instructions (raises ValidationError if invalid)
    
    Args:
        instructions: List of parsed instructions
    
    Raises:
        ValidationError: If any instruction is invalid
    
    Example:
        >>> from parser import parse_philang
        >>> code = "[7-496] :: Ψ(Φ)"
        >>> instructions = parse_philang(code)
        >>> validate_philang(instructions)  # OK
        
        >>> bad_code = "[8-496] :: Ψ(Φ)"
        >>> instructions = parse_philang(bad_code)
        >>> validate_philang(instructions)  # Raises ValidationError
    """
    validator = Validator()
    is_valid, errors = validator.validate_all(instructions)
    
    if not is_valid:
        error_msg = "\n\n".join(errors)
        raise ValidationError(f"Validation failed:\n\n{error_msg}")


if __name__ == "__main__":
    # Test the validator
    from parser import parse_philang
    
    print("Testing ΦLang Validator:")
    print("=" * 50)
    
    # Valid code
    valid_code = "[7-496] :: Ψ(Φ)"
    print(f"Testing valid code: {valid_code}")
    instructions = parse_philang(valid_code)
    
    try:
        validate_philang(instructions)
        print("✓ Validation passed!")
    except ValidationError as e:
        print(f"✗ Validation failed: {e}")
    
    print("\n" + "=" * 50)
    
    # Invalid prime
    invalid_prime = "[8-496] :: Ψ(Φ)"
    print(f"Testing invalid prime: {invalid_prime}")
    instructions = parse_philang(invalid_prime)
    
    try:
        validate_philang(instructions)
        print("✓ Validation passed!")
    except ValidationError as e:
        print(f"✗ Validation failed:\n{e}")
    
    print("\n" + "=" * 50)
    
    # Invalid perfect
    invalid_perfect = "[7-100] :: Ψ(Φ)"
    print(f"Testing invalid perfect: {invalid_perfect}")
    instructions = parse_philang(invalid_perfect)
    
    try:
        validate_philang(instructions)
        print("✓ Validation passed!")
    except ValidationError as e:
        print(f"✗ Validation failed:\n{e}")
