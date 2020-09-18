"""
Idea from:
https://smsxgz.github.io/post/pe/counting_square_free_numbers/#ref02
"""

from math import sqrt
from sympy import sieve
from tqdm import tqdm


def mobius(n):
    """Generates all the mobius numbers up to n."""
    primes = sieve.primerange(2, n+1)
    mobius = [0] + [1] * n

    for p in primes:
        for j in range(1, n // p + 1):
            mobius[j * p] *= -1
        for j in range(1, n // (p**2) + 1):
            mobius[j * p**2] = 0
    return mobius


def p193(N):
    """Finds the last nine digits of the sum of all 0 < n < N,
    such that f(n) is a perfect square."""
    S = 0
    mu = mobius(int(sqrt(N))+1)
    for d in tqdm(range(1, int(sqrt(N)) + 1)):
        S += mu[d] * (N // d**2)

    return S


if __name__ == "__main__":
    print(p193(2**50))
