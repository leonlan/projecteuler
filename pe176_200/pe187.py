"""
Problem 187: Semiprimes
https://projecteuler.net/problem=187

Solution:
Brute-forcing this problem by checking the prime factors for every n would
take an eternity to finish. Instead, we can do something more clever. Since
we are looking for all composite numbers that have precisly two prime factors,
the largest a prime factor could be is ~5*10^7 (since multiplying by 2 exceeds
our upper bound N = 10**8). Now that we know our upper bound for the prime factor,
we do the following:

- For every prime p1 <= sqrt(N), we calculate the product with another prime p2 >= p1
until the product exceeds N. Then, the number of products calculated is the number of
semiprimes.

By the unique prime factorization, we know that every composite number is unique.

Unfortunately, this algorithm has O(n^2) complexity, and takes about 10 seconds to
compute for N = 10^7. There is a better way to do this by directly finding p2.
Let p1 be a prime number, then we calculate x = N//p1. Using the bisect function,
we can almost directly find the index of x. This approach has complexity O(nlogn)!

"""
import sys
sys.path.append("..")
from helperfunctions import prime_sieve
from bisect import bisect_left


def semiprimes(N):
    """Calculates the number of composite integers under N that have precisly two,
    not necessarily distinct, prime factors."""
    count = 0
    primes = list(prime_sieve(N//2))
    for i in range(len(primes)):
        p1 = primes[i]

        # Find the index of the largest prime for which p1*p2 < N
        if p1 <= int(N**0.5):
            x = N//p1
            j = bisect_left(primes, x)
            # Check if we got the right index. Either +1 or -1.
            if p1 != 2:
                if primes[j] * p1 > N:
                    j = j - 1
                elif primes[j+1] * p1 < N:
                    j = j + 1
                j += 1 # Correction for counting (except for p1=2)
            count += j-i
        else:
            return(count)