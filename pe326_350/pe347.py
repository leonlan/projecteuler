"""
Problem 347: Largest integer divisible by two primes
https://projecteuler.net/problem=347

Solution:
Straightforward brute-force.
"""
import sys
sys.path.append("..")
from helperfunctions import prime_sieve


def pe347(N):
    """Returns S(N)."""
    def M(p, q, N):
        """Returns the largest integer <= N that is divisble by
        p and q only where p < q."""
        largest = 0
        a = 1
        while p**a * q <= N:
            b = 1
            while p**a * q**b <= N:
                largest = max(largest, p**a * q**b)
                b += 1
            a += 1
        return(largest)

    primes = list(prime_sieve((N+1//2)))
    total = 0
    for n in range(len(primes)-1):
        m = n+1
        p = primes[n]
        q = primes[m]
        while p*q <= N:
            total += M(p, q, N)
            m += 1
            q = primes[m]
    return(total)


if __name__ == "__main__":
    print(pe347(10**7))
