"""
Problem 69: Totient maximum
https://projecteuler.net/problem=69

Solution:
The maximum is most likely produced by an even number n, since all even
numbers smaller than n are not relatively prime to n (gcd = 2). Therefore,
the denominator remains small and the ratio n/phi(n) is larger. This means
we only need to consider N/2 numbers, which is still not great.

After some experimenting, it seemed to me that any multiple of 6 produces the
best local maximum ratio. I do not have any arguments why this works best,
but it does make this function computable in reasonable time.

Some manual testing resulted finding that 6,30, 210, 2310 and 30030 were the
maximum ratios. I saw a pattern in this: 6*5=30, 30*7=210, 210*11=2310,
2310*13=30030, in other words, the next maximum ratio is found by multiplying
with the next prime number. So 30030*17=510510 is the answer.

"""
import sys
sys.path.append("..")
from helperfunctions import gcd, prime, prime_factors
from math import sqrt


def totient_gcd(n):
    """Determines the number of numbers less than n which are relatively
    prime to n. Also called the Euler's Totient function, or phi funciton."""
    # All numbers smaller than n are relatively prime to n if n is prime
    # Includes base case n = 2
    if prime(n):
        return(n-1)

    # If n is even, phi(2n) = 2*phi(n)
    elif n/2 % 2 == 0:
        return(2*totient(n//2))

    else:
        k, count = 1, 0
        while k < n:
            # Even numbers are not relatively prime
            if k % 2 == 0 and n % 2 == 0:
                pass
            else:
                if gcd(n, k) == 1:
                    count += 1
            k += 1
        return(count)


def totient_product(n):
    """Finds the totient using Euler's product formula."""
    totient = n
    for p in set(prime_factors(n)):
        totient -= totient // p
    return(totient)


def totient_maximum(N, start=2310):
    """Finds the number n <= N for which n/totient(n) is a maximum."""
    n = start
    max_ratio, max_n = 1, 1
    while n < N:
        new_ratio = n/totient_product(n)
        if new_ratio > max_ratio:
            max_ratio = new_ratio
            max_n = n
        n += 2310
    return(max_n)


if __name__ == "__main__":
    print(totient_maximum(10**6))
