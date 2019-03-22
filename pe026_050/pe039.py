"""
Problem 39: Integer right triangles
https://projecteuler.net/problem=39

Solution:
We have the following constraints:
a < b < c
a^2 + b^2 = c^2
p = a + b + c

From the second constraint follows

sqrt(a^2 + b^2) = c

From the third constraint it follows that c < 600.
So we look for all a, b s.t. the square root is integer.

"""
from math import sqrt


def integer_right_triangles(P):
    """Finds the value of p <= P for which the number of Pythagorean triples
    with perimeter p is maximized."""
    count = {i:0 for i in range(P+1)}
    for b in range(1, P//2):
        for a in range(1, b, 2):
            c = sqrt(a**2+b**2)
            if c == int(c):
                p = int(a+b+c)
                if p in count:
                    count[p] += 1
    return(max(count, key=count.get))


if __name__ == "__main__":
    print(integer_right_triangles(1000))
