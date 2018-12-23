"""
Problem 53: Combinatoric selections
https://projecteuler.net/problem=53

Solution:
The difficulty in this exercise is that numbers of type nCr with r = n/2 with n
large gives very big numbers due to the factorial size. However, we do not need
to compute such numbers, since we can use Pascal's triangle identity to find
for each n, what is the first r that gives nCr > 1 million? Knowing that,
we simply know that there are (n+1)-(r*2) of such numbers that are larger
than 1 million.

For more info on Pascal's triangle:
http://mathworld.wolfram.com/PascalsTriangle.html

"""
from math import factorial, ceil


def C(n, r):
    """Returns n choose r. Does not work for super large numbers"""
    return(factorial(n)//(factorial(r)*(factorial(n-r))))


def combinatoric_selections(N, x):
    """Returns how many values of n choose r with 1 <= n <= N are
    greated than x."""
    n = 1
    count = 0

    while n <= N:
        for r in range(ceil((n+1)/2)):
            if C(n, r) > x:
                count += (n+1)-r*2
                break
        n += 1
    return(count)


if __name__ == "__main__":
    print(combinatoric_selections(100, 10**6))
