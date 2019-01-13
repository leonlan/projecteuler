"""
Problem 33: Digit cancelling fractions
https://projecteuler.net/problem=33

Solution:
We write a function that cancels fractions "the silly way". There are a
few cases that we need to consider:
- If n and d are palindromic, then they we ignore them.
- If n and d have cancelled zeros, then we ignore them (trivial solution).

After we found the product of the four fractions, we use the gcd function 
to find the value of the denominator.
"""

import sys
sys.path.append("..")
from helperfunctions import gcd
from itertools import combinations


def cancel(n, d):
    """Cancels digits of a fraction and returns the fraction as tuple."""
    a = str(n)
    b = str(d)
    for c in str(n):
        if c != '0' and c in b:
            a = a.replace(c, "", 1)
            b = b.replace(c, "", 1)

    # Return trivial if no cancellation has taken place or if n and d are palin
    if (a,b) == (str(n),str(d)) or str(n) == str(d)[::-1]:
        return((1,1))
    else:   
        return((a,b))


def digit_cancelling_fractions():
    N, D = [1, 1]
    for frac in combinations(range(10, 100), 2):
        n, d = frac
        x, y = cancel(n, d)
        if y != '0' and n/d == float(x)/float(y):
            N *= n
            D *= d
    return(D/gcd(N,D))


if __name__ == "__main__":
    print(digit_cancelling_fractions())