"""
Problem 47: Distinct prime factors
https://projecteuler.net/problem=47

Solution:
We iteratively list all the primes (up to 10**7) using a prime sieve generator.
If the distance between two primes is bigger than n, then we know that there
are at least n consecutive composite numbers between these prime numbers. In
this case, we check for each composite number if it has n distinct prime factors
and we keep count.

"""
import sys
sys.path.append("..")
from helperfunctions import prime_sieve


def distinct_prime_factors(n):
    """Finds the first n consecutive integers to have n dstinct prime
    factors each."""
    primes_gen = prime_sieve(10**7)
    current_prime = next(primes_gen)
    primes_list = [current_prime]

    def prime_factors(n, primes):
        factors = []
        for p in primes:
            power = 0
            if n % p == 0:
                # Keep dividing by p until its not a divisor anymore
                while n % p == 0 and n != 1:
                    n //= p
                    power += 1
                factors.append(p**power)
                # Stop if we have found all divisors
                if n == 1:
                    return(len(factors))

    while True:
        current_prime = next(primes_gen)
        primes_list.append(current_prime)
        previous_prime = primes_list[-2]
        # There are at least n consecutive composite numbers to check
        if current_prime - previous_prime > n:
            count = 0
            for consec in range(previous_prime + 1, current_prime):
                factorization = prime_factors(consec, primes_list)
                if factorization == n:
                    count += 1
                    if count == n:
                        return(consec-n+1)
                # If one of the consecutive numbers has != n divisors, start counting again
                else:
                    count = 0


if __name__ == "__main__":
    print(distinct_prime_factors(4))
