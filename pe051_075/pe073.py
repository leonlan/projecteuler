"""
Problem 73: Counting fractions in a range
https://projecteuler.net/problem=73

Solution:
Brute force search between the range 2/d < n < 3d for all d <= D.

"""
from math import floor, ceil


def counting_fractions_in_a_range(D):
    """Returns the number of fractions that lie between 1/3 and 1/2 in
    the sorted set of reduced proper fractions for d <= D."""
    rpf = set()
    for d in range(2, D+1):
        upper = floor(d/2)
        lower = ceil(d/3)
        for n in range(lower, upper+1):
            if n/d > 1/3 and n/d < 1/2:
                rpf.add(n/d)
    return(len(rpf))


if __name__ == "__main__":
    print(counting_fractions_in_a_range(12000))
