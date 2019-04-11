"""
Problem 75: Singular integer right triangles
https://projecteuler.net/problem=75

Solution:
Use Euclid's algorithm to produce all primitive triples.
Solution can be optimized by finding better upper bounds for m and n.
Similarly, instead of using a list W it is more memory-efficient to
use a dictionary to count the frequency of numbers.
"""
import sys
sys.path.append("..")
from helperfunctions import gcd


def pe075(L):
    """Returns for how many values l <= L there are exactly one integer
    sided right triangle with perimter l."""
    def a(m, n):
        return(m**2-n**2)

    def b(m, n):
        return(2*m*n)

    def c(m, n):
        return(m**2+n**2)

    def abc(a, b, c):
        return(a + b + c)

    W = (L+1)*[0]
    m = 1
    while m**2 < L-1:
        n = 1
        while n < m and m**2 + n**2 < L//2:
            A = a(m, n)
            B = b(m, n)
            C = c(m, n)
            ABC = abc(A, B, C)
            if gcd(A, B) == 1:
                k = 1
                while k * ABC < L:
                    W[k*ABC] += 1
                    k += 1
            n += 1
        m += 1
    return(sum([1 for i in range(len(W)) if W[i] == 1]))


if __name__ == "__main__":
    print(pe075(15*10**5))
