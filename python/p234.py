from sympy import sieve, nextprime
from math import sqrt


def L(p, q):
    """Returns smallest and largest number for which lps(n)=p and ups(n)=q."""
    return p**2+1, q**2-1


def find_multiples(d, a, b):
    """Returns the set of numbers between a and b which are divisible by d."""
    multiples = set()

    if a % d != 0:
        a += (d - a % d)

    while a <= b:
        multiples.add(a)
        a += d

    return multiples


def symmetric_difference(A, B):
    """Computes the symmetric difference between sets A and B."""
    return (A-B).union(B-A)


def p234(n):
    """Finds the sum of all semidivisible numbers not exceeding n."""
    total = 0
    primes = list(sieve.primerange(2, nextprime(sqrt(n)) + 1))

    for idx, p in enumerate(primes[:-1]):
        q = primes[idx+1]
        start, end = L(p, q)
        # Correct for upper bound
        if end > n:
            end = n

        # Find all semidivisible numbers in L(p, q)
        semidivisible = symmetric_difference(
            find_multiples(p, start, end),
            find_multiples(q, start, end)
        )

        total += sum(semidivisible)

    return total


if __name__ == "__main__":
    print(p234(999966663333))
