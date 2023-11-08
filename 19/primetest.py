# prime_library.py

import math
import random

def is_prime_deterministic(n):
    """Deterministic test for checking primality."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_prime_probabilistic(n, k=10):
    """Probabilistic test for checking primality using the Miller-Rabin test."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write (n - 1) as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
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

def find_next_prime(n):
    """Find the next prime number after n."""
    if isinstance(n, float) and not n.is_integer():
        n = math.ceil(n)  # Round up to the next integer if n is a float
    elif not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer or a non-integer float.")
    
    prime_candidate = max(2, n + 1)
    while True:
        if is_prime_probabilistic(prime_candidate):
            return prime_candidate
        prime_candidate += 1

if __name__ == "__main__":
    # Example usage:
    num = 18
    print(f"Is {num} a prime number? {is_prime_deterministic(num)}")
    print(f"Next prime number after {num} is {find_next_prime(num)}")
