"""
Problem 71: Ordered fractions
https://projecteuler.net/problem=71

Solution:
Given d, find the largest n such that n/d < 3/7. The n can easily be
found given that n < floor(3d/7).

"""
from math import floor, ceil


def ordered_fractions(D):
    """Find the numerator of the fraction immediately left of 3/7 for
    all reduced proper fractions for d <= D."""
    best_frac = (3,7)
    curr_diff = 1
    for d in range(1, D+1):
        n = floor(3*d/7)
        if n/d < 3/7 and 3/7 - n/d < curr_diff:
            curr_diff = 3/7-n/d
            best_frac = (n, d)
    return(best_frac)


if __name__ == "__main__":
    print(ordered_fractions(10**6))
