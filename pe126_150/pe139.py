"""
Problem 139: Pythagorean tiles
https://projecteuler.net/problem=139

Solution:
Given (a, b, c), if c % (b-a), then tiling is possible.
Use Euclid's algorithm to produce all primitive Pythagorean triples
and then include all Pythagorean triples with perimeter less than 10**8.

Running time is high (1 min 11s) but can be improved by finding better upper
bounds for m and n.
"""
import sys
sys.path.append("..")
from helperfunctions import gcd


def pe139(p):
    """Given a maximum perimeter p, how many Pythagorean triangles
    allow a tiling?"""
    count = 0
    m = 1
    while m**2 < p//2:
        n = 1
        while n < m or m**2 + n**2 < p//2:
            a = 2*m*n
            b = m**2 - n**2
            c = m**2 + n**2
            if c % (b-a) == 0 and gcd(a, b) == 1:
                count += p//(a+b+c)
            n += 1
        m += 1
    return(count)


if __name__ == "__main__":
    print(pe139(10**8))
