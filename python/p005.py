from collections import defaultdict
from math import prod
from sympy import factorint


def lcm(L):
    """
    Finds the least common multiple of all numbers in L.
    Calculated using the prime-factorization techinque.
    """
    max_primefactors = defaultdict(int)

    # Find the largest prime powers
    for n in L:
        for p, multiplicity in factorint(n).items():
            max_primefactors[p] = max(max_primefactors[p], multiplicity)

    # Calculate the product of all largest prime powers
    least_common_multiple = prod(
        [k ** v for k, v in max_primefactors.items() if k != 0]
    )
    return least_common_multiple


def p005(N):
    """Finds the smallest positive number that is evenly divisible
    by all numbers from 1 to 20."""
    return lcm(list(range(20 + 1)))


if __name__ == "__main__":
    print(p005(20))
