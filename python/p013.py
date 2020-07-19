"""
Problem 13: Large sum
https://projecteuler.net/problem=13
"""


def p013(f):
    """
    Returns the first 10 digits of the sum of all numbers in
    the given file f.
    """
    L = open(f).readlines()
    numbers = [int(line.strip()[0:11]) for line in L]
    sum = 0
    for number in numbers:
        sum += number
    return str(sum)[0:10]


if __name__ == "__main__":
    f = '../data/p013.txt'
    print(p013(f))
