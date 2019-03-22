"""
Problem 123: Prime square remainders
https://projecteuler.net/problem=123

Solution:
Similar to Problem 120. In this case, we do not need to maximize
the remainder. Instead, for every n we check

r_n = 2np_n mod (p_n)^2

We can skip every even n since the remainder will be 2.
"""
import sys
sys.path.append("..")
from helperfunctions import prime_sieve


def prime_square_remainders(target):
    """Finds the least value of n for which the remainder
    exceeds target."""
    p = [0] + list(prime_sieve(10**6))
    for n in range(1, len(p), 2):
        r = 2*n*p[n] % p[n]**2
        if r > target:
            return(n)
    return(0)


if __name__ == "__main__":
    print(prime_square_remainders(10**10))
