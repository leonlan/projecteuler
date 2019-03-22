"""
Problem 127: abc-hits
https://projecteuler.net/problem=127

Solution:
There are four properties that (a, b, c) needs to satisfy in order to be an
abc-hit:
1. GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
2. a < b
3. a + b = c
4. rad(abc) < c

Let's try to distill as many optimizations as we can from these conditions.
- From 1. we can deduce that all doubles (a, b), (a, c) and (b, c) cannot
contain two even numbers, since the GCD would then be at least two. So for
every triple (a, b, c), we can only have one even number. We can make this
even more precise: if c is even, then both a and b must be odd. If c is
odd, then either a is odd or b is odd but not both.

- From 2. and 3. it follows that 0.5c + 1 <= b <= c-1. and 1 <= a <= b - 1.

- From 4. it follows that c cannot be prime, otherwise rad(abc) >= c. So we
only need to check for c that are composite numbers. Moreover, we cannot
have that b is prime since then rad(abc) <= rad(a) * rab(b) * rad(c) and then
since rad(c) > 2 we have that rad(b)*rad(c) >= c+2.


A few other properties to keep in mind:
- rad(abc) <= rad(a) * rad(b) * rad(c)

# Issues
Runs too slow. At c < 1000, it takes already about 1 second. There needs to be a fast
way of computing for every c which b are eligible. Which b are relative prime to c?

If we check max(factors(c)) * 4 < c, then ~20000 of the c's are excluded by 4.

By 1., we know that a, b, c may not have the same prime factors.




"""
import sys
#sys.path.append("..")
from helperfunctions import prime, gcd, prime_sieve, prime_factors
from itertools import filterfalse, combinations
from functools import reduce
from operator import mul

def abc_hits(N):
    """Finds the sum of all abc-hits for c under N."""
    count = 0

    gcd_cache = {}
    def gcd_checker(a, b, c):
        """Checks if gcd(a,b) = gcd(b,c) = gcd(a,c) = 1."""
        for double in combinations([a, b, c], 2):
            if double not in gcd_cache:
                gcd_cache[double] = gcd(*double)
            if gcd_cache[double] != 1:
                return(False)
        return(True)


    primes = set(prime_sieve(N))
    def rad(n):
        """Returns a list of prime factors of n."""
        factors = set()
        for p in primes:
            while n % p == 0:
                factors.add(p)
                n /= p
            if n == 1:
                return(reduce(mul, factors, 1))
        return(n)


    pool_c = list(filterfalse(prime, range(1, N)))
    for c in pool_c:
        step = 2 if c % 2 == 0 else 1
        for b in range(c//2+1, c, step):
            if b not in primes:
                a = c-b
                if gcd_checker(a, b, c):#and rad(a*b*c) < c:
                    count += c
#                    print(a, b, c)

    return(count)



if __name__ == "__main__":
#    print(abc_hits(2000))
    # def gcd_checker(a, b, c):
    #     """Checks if gcd(a,b) = gcd(b,c) = gcd(a,c) = 1."""
    #     for double in combinations([a, b, c], 2):
    #         if double not in gcd_cache:
    #             gcd_cache[double] = gcd(*double)
    #         if gcd_cache[double] != 1:
    #             return(False)
    #     return(True)
    # gcd_cache = {}

    # for c in range(1, 2000):
    #     for b in range(c//2+1, c, 2):
    #         gcd_checker(1,b,c)
    N = 100000
    primes = set(prime_sieve(N))
    def rad(n):
        """Returns a list of prime factors of n."""
        factors = set()
        for p in primes:
            while n % p == 0:
                factors.add(p)
                n /= p
            if n == 1:
                return(list(factors))
        return([n])

    count = 0

    for c in range(2,20000):
        if max(rad(c))*6>c:
            count += 1
    print(count)
