"""
Problem 80: Square root digital expansion
https://projecteuler.net/problem=80

Solution:
I have no clue on how to calculate the decimals of a number without
using built-in modules that expand up to X decimals.
"""
from decimal import Decimal, getcontext


def square_root_digital_expansion(N, D):
    """Finds the total of the digital sums of the first D decimals for all
    the irrational square roots of all natural numbers below N."""
    getcontext().prec = D+5 # Make up for precision
    total = 0
    j = 2
    for i in range(2, N+1):
        if j*j == i:
            j += 1
        else:
            k = str(Decimal(i).sqrt())
            total += sum([int(c) for c in k[2:D+1]]) + int(k[0])
    return(total)


if __name__ == "__main__":
    print(square_root_digital_expansion(100,100))
