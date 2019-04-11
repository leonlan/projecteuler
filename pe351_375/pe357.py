"""
Problem 357: Prime generating integers
https://projecteuler.net/problem=357

Solution:
We only need to consider n such that n+1 is prime.

Running time is ~5 min. Too high, but gives the right answer.
"""
import sys
sys.path.append("..")
from helperfunctions import properdivisors, prime_sieve


def pe357(N):
    """Finds the sum of all positive integers not exceed N such that
    every divisor d of n, d+n/d is prime."""
    primes_list = list(prime_sieve(N))[1:]
    primes_set = set(primes_list)
    total = 1
    for p in primes_list:
        n = p-1
        if 2 + n//2 in primes_set:
            for d in properdivisors(n)[::2]:
                if d+(n//d) not in primes_set:
                    break
            else:
                total += n
    return(total)


if __name__ == "__main__":
    print(pe357(10**8))
