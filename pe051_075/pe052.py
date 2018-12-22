"""
Problem 52: Permuted multiples
https://projecteuler.net/problem=52

Solution:
- The length of the multipels must contain the same number of digits, so
len(x) = len(2x) = ... = len(6x). That means that given 3 digits, we only
need to consider 100 < x < 166, since 166*6 < 1000 and 167*7 > 1000.
We can generalize this for D digits: we only need to consider
10**(D-1) < x < 10**(D)/6 given D digits.
"""
import sys
sys.path.append("..")
from helperfunctions import is_permutation


def has_n_permuted_multiples(x, n):
    """Checks if x has exactly n consecutive permuted multiples."""
    multiples = []
    for i in range(1, n+1):
        multiples.append(i*x)

    for mult in multiples:
        if not is_permutation(x, mult):
            return(False)
    return(True)


def permuted_multiples(n):
    """Finds the smallest positive integer x, such that 2x, 3x, ..., nx
    contain the same amount of digits."""
    D = 1
    while True:
        for x in range(10**(D-1), 10**(D)//6+1):
            if has_n_permuted_multiples(x, n):
                return(x)
        D += 1


if __name__ == "__main__":
    print(permuted_multiples(6))
