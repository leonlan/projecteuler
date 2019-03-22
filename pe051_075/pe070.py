"""
Problem 70: Totient permutation
https://projecteuler.net/problem=70

Solution:
Note the following observations:
* Since phi(n) = n-1, it is highly unlikely that any prime number is a
permutation of phi(n). So we exclude prime numbers.
* Since we are looking for the minimum ratio, it is unlikely that we
are looking for an even number, since even numbers produce high ratios.
* phi(p**n) = (p-1) * p**(n-1)
* phi(a*b) = phi(a) * phi(b) if gcd(a, b) = 1
* If N = (p1**k1) * (p2**k2) * (p3**k3) * ....
then phi(N) = phi(p1**k1) * phi(p2**k2) * phi(p3**k3) ...
"""
import sys
sys.path.append("..")
from collections import Counter
from helperfunctions import prime_sieve


def is_permutation(a, b):
    """Checks if a is a permutation of b."""
    a, b = str(a), str(b)
    return(len(a) == len(b) and Counter(a) == Counter(b))


def totient_sieve(N):
    totients = [1]*N
    for p in range(2, N):
        if p == N-1:
            print(p)
        # Sieve for each prime number p
        if totients[p] == 1:
            powers = set()
            k = 2

            # Calculate each power of the prime number
            while p**k < N:
                powers.add(p**k)
                k += 1

            # Multiply with phi(p) = p-1 for every number divisible by p
            for i in range(p, N, p):
                totients[i] *= p-1

            # Multiply with p to count for multiplicity
            for power in powers:
                for j in range(power, N, power):
                    totients[j] *= p

    ratios_and_permutations = [(n, n/totients[n]) for n in range(N) if
                               is_permutation(n, totients[n])][1:]  # Exclude 1
    return(min(ratios_and_permutations, key=lambda t: t[1])[0])


if __name__ == "__main__":
    print(totient_sieve(10**7))
