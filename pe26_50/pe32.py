"""
Problem 32: Pandigital products
https://projecteuler.net/problem=32

Solution:
Brute-force all possible products digits such that the total
number of digits used is 9 (so that it could be pandigital)
"""


def is_pandigital(s):
    return('123456789' == ''.join(sorted(s)))


def pandigital_products():
    S = set()
    for n in [1, 2]:
        for i in range(10**(n-1), 10**n):
            for j in range(10**(4-n), 10**4):
                digits = str(i) + str(j) + str(i*j)
                if is_pandigital(digits):
                    S.add(i*j)
    return(sum(S))


if __name__ == "__main__":
    print(pandigital_products())
