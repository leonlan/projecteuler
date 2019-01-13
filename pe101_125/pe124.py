"""
Problem 124: Ordered radicals
https://projecteuler.net/problem=124

Solution:
Quite straight-forward problem. We compute the rad for each number n < 10**6
and store it in a dictionary. Then we sort the dictionary on the value and
retrieve the desired index.

Note: this prime facotrization algorithm is rather slow, so it takes about
~10 seconds for n < 10**6 with (assumed) O(n^2).
"""


import sys
sys.path.append("..")
from helperfunctions import prime_sieve
from functools import reduce
from operator import mul


def rad(n, prime_list):
    """Returns a list of prime factors of n."""
    factors = set()
    for p in prime_list:
        while n % p == 0:
            factors.add(p)
            n /= p
        if n == 1:
            return(reduce(mul, factors, 1))
    return(n)


def ordered_radicals(N, idx):
    """Returns E(idx), where E(k) is the kth element in the sorted
    rad(n) columns for n < N."""
    primes = list(prime_sieve(N))
    unsortedE = {}
    for n in range(1, N+1):
        unsortedE[n] = rad(n, primes)
    E = sorted(unsortedE.items(), key=lambda kv: kv[1])
    return(E[idx])
