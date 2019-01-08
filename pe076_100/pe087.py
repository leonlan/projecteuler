"""
Problem 87: Prime power triples
https://projecteuler.net/problem=87

Solution:
Since the epression takes the form x^2+y^3+z^4, we find an upper bound
for x with y,z = 2. Given this upper bound, which we call X, we know
that we need to iterate over all values 2 < x < X, such that x is prime.
Moreover, we iterate over all prime values of y, z as long as the
given expression is below 50 million.

To iterate over the prime numbers, we use the indices i, j, k for x, y, z
respectively. We apply memoization to keep a set of unique values of numbers
below 50 million.

"""
import sys
sys.path.append("..")
from helperfunctions import prime_sieve
from math import ceil


def power_triple(a, b, c):
    return(a**2+b**3+c**4)


def prime_power_triples(N):
    """Returns how many numbers below N can be expressed as a prime power
    triple of the form: x^2 + y^2 + z^2 < N."""
    count = set()
    X = ceil((N-2**3-2**4)**(1/2))
    upper_bound = [X]
    primes = list(prime_sieve(X))
    for bound in upper_bound:
        for i in range(max([primes.index(x) for x in primes if x < bound])+1):
            j, k = [0, 0]
            while power_triple(primes[i], primes[j], primes[k]) < N:
                while power_triple(primes[i], primes[j], primes[k]) < N:
                    count.add(power_triple(primes[i], primes[j], primes[k]))
                    k += 1
                j += 1
                k = 0
    return(len(count))


if __name__ == "__main__":
    prime_power_triples(5*10**7)
