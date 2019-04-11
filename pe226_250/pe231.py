"""
Problem 231: The prime factorisation of binomial coefficients
https://projecteuler.net/problem=231

Solution:
An n choose k number (k = min(k, n-k)) can be described as:

n * n-1 * ... * n-k+1
---------------------
1 * 2 * ... * k

Using a sieve-like technique, we can calculate all the prime
factors in the numerator and denominator.
"""
import sys
sys.path.append("..")
from helperfunctions import prime_sieve
from collections import defaultdict
from math import ceil


def pe231(N, K):
    """Finds the sum of the terms in the prime factorization of
    N choose K."""
    K = min(K, N-K)

    # Calculate prime factors of N, N-1, ..., N-k+1
    divsN = defaultdict(int)
    for p in prime_sieve(N):
        if p <= N//2:
            i = ceil((N-K+1)/p)
            while p*i <= N:
                n = p*i
                multiplicity = 0
                while n % p == 0:
                    multiplicity += 1
                    n //= p
                divsN[p] += multiplicity
                i += 1
        elif p > (N-K+1):
            divsN[p] += 1

    # Calculate prime factors of 1, 2, ..., k
    divsK = defaultdict(int)
    for p in prime_sieve(K+1):
        i = 1
        while p*i <= K:
            n = p*i
            multiplicity = 0
            while n % p == 0:
                multiplicity += 1
                n //= p
            divsK[p] += multiplicity
            i += 1

    total = 0
    for k, v in divsN.items():
        total += (v - divsK[k])*k
    return(total)


if __name__ == "__main__":
    print(pe231(2*10**7, 15*10**6))
