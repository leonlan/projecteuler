"""
Problem 57: Square root convergents
https://projecteuler.net/problem=57

Solution:
Simple calculation for each iteration of the sq root convergents.
"""


def square_root_convergents(n):
    """Returns how many of the first n-expansions fractions contain a
    numerator with more digits than the denominator."""
    count = 0
    for i in range(n):
        frac = [1, 2]
        for j in range(i, 0, -1):
            frac[0] += 2*frac[1]
            frac = frac[::-1]
        frac[0] += frac[1]
        if len(str(frac[0])) > len(str(frac[1])):
            count += 1
    return(count)


if __name__ == "__main__":
    print(square_root_convergents(1000))
