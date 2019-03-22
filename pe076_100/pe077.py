"""
Problem 77: Prime summations
https://projecteuler.net/problem=77

Solution:
Similar to Problem 76, but a bit more difficult since we need to
keep track of primes and can't use indices directly. We define

ways[n][m] with m < n

as the number of ways that n can be written as the sum of primes
where the primes are smaller than m.
"""
import sys
import pprint
sys.path.append("..")
from helperfunctions import prime_sieve


def prime_summations(N):
    """Finds the first value that can be written as a sum of primes
    in more than N different ways."""
    p = set(prime_sieve(10**4))
    ways = [[0],[0,0]]
    n = 1
    while ways[n-1][n-2] < N: # I count one n too much somewhere
        ways.append([0]*(n+2))
        m = 0
        for m in range(1, n+1):
            if m in p:
                if m == n:
                    ways[n][m] = ways[n][m-1] + 1
                else:
                    ways[n][m] = ways[n-m][min(m, n-m)] + ways[n][m-1]
            else:
                ways[n][m] = ways[n][m-1]
        n += 1
    return(n-1)



if __name__ == "__main__":
    print(prime_summations(5000))
