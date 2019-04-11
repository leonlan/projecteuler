"""
Problem 203: Squarefree Binominal Coefficients
https://projecteuler.net/problem=203

Solution:
The know that nCk is represented as

n * (n-1) * ... (n-k+1)
-----------------------
1 * 2 * ... * k

So for every element in the products we can find the prime
factorization and use a cache to track the prime factors
of the numerator and denominator. The number of prime factors
in the number nCk is then the difference of the prime factors.
"""
import sys
sys.path.append("..")
from helperfunctions import prime_factors
import numpy as np


def pe203(N):
    """Find the sum of the distinct squarefree numbers numbers in
    the first N rows Pascal's triangle."""
    cache = np.array((N+1)*[np.zeros(N+1)], dtype="int32")
    for n in range(2, N+1):
        for p in prime_factors(n):
            cache[n][p] += 1

    distinct = set([1])
    for n in range(1, N):
        for k in range(n//2+1):
            factors = np.zeros(N+1, dtype="int32")
            for i in range(n, n-k, -1):
                factors += cache[i]
            for j in range(1, k+1):
                factors -= cache[j]
            if all(factors <= 1):
                distinct.add(np.prod([el*factors[el]
                                      for el in range(len(factors))
                                      if factors[el] > 0], dtype="int64"))
    return(sum(distinct))


if __name__ == "__main__":
    print(pe203(51))
