from sympy import sieve, isprime
from collections import defaultdict


def p249(N):
    # Initialization
    total = 0
    S = list(sieve.primerange(2, N))
    curr = defaultdict(int)
    prev = defaultdict(int)

    # Dynamic programming
    for n, p in enumerate(S):
        if n == 0:
            curr[p] += 1
        else:
            curr[p] += 1
            for sum, v in prev.items():
                curr[sum] += v
                curr[sum+p] += v
        prev = curr
        curr = defaultdict(int)

    # Add up all subset sums that are prime
    for k, v in prev.items():
        if isprime(k):
            total = (total + v) % 10**16

    return total


if __name__ == "__main__":
    print(p249(5000))
