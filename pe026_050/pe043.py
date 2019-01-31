"""
Problem 43: Sub-string divisibility
https://projecteuler.net/problem=43

Solution:
A simple brute-force would take us for ages, as there are
about ~10! ~= 3.6 million different pandigital numbers.

Instead, we use the given information to find a significantly smaller pool of
numbers that might satisfy the given properties.

First, we "create" pandigital numbers that might satisfy the given properties.
How do we create them? We compute the cartesian product of three triples:

(d2d3d4) x (d5d6d7) x (d8d9d10)

Using the given properties, we can significantly reduce the possibilities
of these triples, so that the cartesian product is not extremely large.
Next, we check if no number is repeated, and accordingly add the last
digit to make it a pandigital 0-9 number. For example, (406)x(357)x(289)
satisfies the given properties, so we add the remaining number (1) in front.

(d2d3d4)
- d2d3d4 % 2 => triples of even numbers, without repetition of any numbers.

(d5d6d7)
- d4d5d6 % 5 => d6 must be 0 or 5, i.e. d5d6d7 % 50 < 10
- d5d6d7 & 7 => must be divisible by 7.

(d8d9d10)
- d8d9d10 % 17 => must be divisible by 17.

The above solution is very slow, it runs in 2 seconds. Make it much faster
next time.
"""
from collections import Counter
from itertools import product, chain


def sub_string_divisiblity():
    """Computes the sum of all pandigital numbers that satisfy the
    given substring divisibility properties."""
    total = 0

    # Part 1: Computing triples
    def no_repeated_digits(n):
        """Checks if n has no repeated digits."""
        s = str(n)
        chars = set()
        for c in s:
            if c in chars:
                return(False)
            else:
                chars.add(c)
        return(True)

    triple1 = ["{0:0=3d}".format(x) for x in range(2, 1000, 2)]
    triple2 = ["{0:0=3d}".format(x) for x in range(1, 1000, 1) if x % 7 == 0 and x % 50]
    triple3 = ["{0:0=3d}".format(x) for x in range(1, 1000) if x % 17 == 0]
    triples = [triple1, triple2, triple3]

    for i in range(len(triples)):
        triples[i] = list(filter(no_repeated_digits, triples[i]))

    # Part 2: Computing products
    def add_missing_digit(n):
        """Returns the missing digit to make n a 0-9 pandigital number.
        The input number must not have any repeated digits and have length 9."""
        s = str(n)
        for i in range(0, 10):
            if str(i) not in s:
                return(int(str(i)+s))

    def sub_string_properties(n):
        """Checks if n satisfies all sub string properties."""
        x = str(n)
        divisions = [2, 3, 5, 7, 11, 13, 17]
        for i in range(1, 8):
            if int(x[i:i+3]) % divisions[i-1]:
                return(False)
        return(True)

    for prod in product(triples[0], triples[1], triples[2]):
        # Concatenate the triples
        x = ''
        for triple in prod:
            x += triple
        if no_repeated_digits(x):
            x = add_missing_digit(x)
            if x != 0 and sub_string_properties(x):
                total += x
    return(total)


if __name__ == "__main__":
    print(sub_string_divisiblity())
