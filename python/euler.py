from math import ceil, sqrt
from collections import Counter
import random

def isprime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False

    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True

    for i in range(8):#number of trials
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True

def prime(n):
    """Returns whether n is prime or not."""
    # Case 0: n is 0, 1 or negative
    if n < 2:
        return False

    # Case 1: n = 2
    elif n == 2:
        return True

    # Case 2: n is even
    elif n % 2 == 0:
        return False

    # Case 3: n is odd
    for i in range(3, ceil(sqrt(n))+1, 2):
        if n % i == 0:
            return False

    return True


def primelist(n, start=2, length=False):
    """Returns the list of primes up to n (starting from start=3).
    If length = TRUE, return the first n prime numbers."""
    # Separate case for 2 since it is even
    if start > 2:
        primes = []
    else:
        primes = [2]

    # Primes cannot be even
    if start % 2 == 0:
        start += 1

    # Case 1: all primes up to n.
    if not length:
        for i in range(start, n+1, 2):
            if prime(i):
                primes.append(i)

    # Case 2: the first n prime numbers.
    else:
        j = start
        while len(primes) < n:
            if prime(j):
                primes.append(j)
                j += 2
    return(primes)


def prime_sieve(n):
    """Returns a list of primes up to n using the Sieve of Erastosthenes.
    Source: https://bit.ly/2BweHDN"""
    li = [True] * n
    li[0] = li[1] = False

    for (i, isprime) in enumerate(li):
        if isprime:
            yield i
            for j in range(i*i, n, i):
                li[j] = False
    return(li)


def properdivisors(n):
    """Returns the list of proper divisors of n."""
    propdiv = [1]
    start, step = [2, 1]

    # Odd numbers only have odd divisors
    if n % 2 == 1:
        start, step = [3, 2]

    for i in range(start, ceil(sqrt(n)), step):
        if n % i == 0:
            propdiv.extend([i, n//i])

    # If n is a perfect square, also add the square root.
    # Note: this does not work for VERY LARGE n.
    if sqrt(n).is_integer() and n != 1:
        propdiv.append(int(sqrt(n)))

    return(propdiv)


def primefactors(n):
    """Returns a list of prime factors of n."""
    factors = []
    primes = prime_sieve(n)

    for p in primes:
        while n % p == 0:
            factors.append(p)
            n /= p
        if n == 1:
            return(factors)
    return([n])


def primefactors_with_multiplicity(n):
    """Returns a dictionary of prime factors of n."""
    factors = []
    primes = prime_sieve(n)

    for p in primes:
        while n % p == 0:
            factors.append(p)
            n /= p
        if n == 1:
            return(factors)
    return([n])


"""
Uncategorized helperfunctions
"""


def sort(n, integer=False):
    """Takes a string/integer as input and lexicographically sorts it.
    If integer is True, it returns it as integer type."""
    x = ''.join(sorted(str(n)))
    if integer:
        return(int(x))
    else:
        return(x)


def gcd(a, b):
    """Finds the greatest common divisors of a and b using Euclid's."""
    while b != 0:
        t = b
        b = a % b
        a = t
    return(a)


def lcm(x, y):
    """Finds the largest common multiple of x and y."""
    lcm = (x*y)//gcd(x,y)
    return(lcm)


def is_permutation(a, b):
    """Checks if a is a permutation of b."""
    a, b = str(a), str(b)
    return(len(a) == len(b) and Counter(a) == Counter(b))


def reverse(n):
    """Returns the reverse of n."""
    return(int(str(n)[::-1]))


def is_palindrome(n):
    """Checks if n is palindromic."""
    return(n == reverse(n))

def is_pandigital(s):
    """Input string s."""
    digits = [False] * 10
    for i in range(len(s)):
        digits[int(s[i])]
