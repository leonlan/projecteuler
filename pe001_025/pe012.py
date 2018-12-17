from math import ceil
"""
Problem: 
https://projecteuler.net/problem=12

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 
    1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 

The first ten terms would be:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred 
divisors?


Solution:
I was unable to find a clever mathematical solution, so I'll try an optimized
brute-force approach by finding the divisors of each triangle number. 

Let n be a triangle number. Then for each divisor k < sqrt(n), there exists
another divisor n/k > sqrt(n) (mutliply both sides by n, take reciprocal).
Thus we can brute-force search for the divisors up to sqrt(n) and multiply
the number of divisors by two. 

Note that if n is divisible by its square root, then we add one more to 
the number of divisors (since its "complementary" divisor is itself).
"""

def trianglenumdivisors(n):
    """Returns the value of the first triangle number with over n divisors."""
    divcount = 0
    trianglenum, i = [0,0]
    while divcount <= n:
        divcount = 0
        i += 1
        trianglenum += i

        # Search for divisors up to sqrt(trianglenum)
        for j in range(1, int(ceil(trianglenum**0.5))):
            if trianglenum % j == 0:
                divcount += 2

        # Special case the trianglenum is a square
        if int(trianglenum**0.5)**2 == trianglenum:
            divcount += 1

    return(trianglenum)

print(trianglenumdivisors(500))