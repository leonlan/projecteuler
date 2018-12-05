"""
Problem:
https://projecteuler.net/problem=40

Solution:
It's quite  easy to compute this product by hand, but I made a more
general version that could take any list of indices.
"""


def champernownes(digits):
    """Given a list of indices, return the product of the
    digits of Champernowne's constant  at the given indices"""
    prod = 1
    n = 1
    lower, upper = [1, 9]

    for d in digits:
        while d > upper:
            n += 1
            lower += 10**(n-2)*9*(n-1)
            upper += 10**(n-1)*9*n
        num = (d-lower) // n
        idx = (d-lower) % n
        prod *= int(str(num + 10**(n-1))[idx])
    return(prod)

if __name__ == '__main__':
    champernownes([1,100,1000,10000,100000,1000000])
