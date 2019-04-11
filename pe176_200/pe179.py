"""
Problem 179: Consecutive positive divisors
https://projecteuler.net/problem=179

Solution:
The number of divisors of a number n is equal to product of
multiplicity + 1 of all primes that divide n. For example,
n = 14 has divisors 2 and 7 both with multiplicity 1. Then
the number of divisors is 2*2 = 4, namely 1, 2, 7 and 14.
"""
import sys
sys.path.append("..")
from helperfunctions import prime_sieve


def pe179(N):
    """Finds the number of integers 1 < n < N for which n and n + 1 have the same
    number of positive divisors."""
    divs = [1]*(N+1)
    primes = list(prime_sieve((N+1)//2))
    for p in primes:
        i = 1
        while p*i < N:
            n = p*i
            multiplicity = 1
            while n % p == 0:
                multiplicity += 1
                n //= p
            divs[p*i] *= multiplicity
            i += 1

    count = 0
    for x in range(1, len(divs)-1):
        if divs[x] == divs[x+1]:
            count += 1

    return(count)


if __name__ == "__main__":
    print(pe179(10**7))
