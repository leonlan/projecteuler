"""
Problem 50: Consecutive prime sum
https://projecteuler.net/problem=50

Solution:

"""
import sys
sys.path.append("..")
from helperfunctions import prime_sieve


def consecutive_prime_sum(N):
    """Returns the prime bellow N which can be written as the sum of the
    most consecutive primes."""
    pool = list(prime_sieve(N))
    primes = list(prime_sieve(N//2))
    max_idx = len(primes)
    largest_chain = 0
    largest_prime = 0

    for p in pool:
        idx = 1
        start = 0
        consecutive_sum = primes[start]
        while idx < max_idx and primes[start]*largest_chain < p:
            consecutive_sum += primes[idx]

            # Remove the starting values of the chain
            while consecutive_sum > p:
                consecutive_sum -= primes[start]
                start += 1

            if consecutive_sum == p:
                chain_length = idx - start + 1
                if chain_length > largest_chain:
                    largest_chain = chain_length
                    largest_prime = p
            idx += 1
    return(largest_prime)


if __name__ == "__main__":
    print(consecutive_prime_sum(10**6))
