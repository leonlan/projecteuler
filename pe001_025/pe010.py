"""
Problem:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Solution 1:
See helperfunctions.py.
"""

import sys
sys.path.append('..')
from helperfunctions import prime, primelist


"""
Solution 2 (from the solutions on Project Euler):
The Sieve of Eratosthenes is another method to solve this problem. Instead of
checking for divisors of p to check whether it is prime or not, we can mark
multiples of primes as composites.
"""

def sieve_of_eratosthenes(n):
	"""Returns a list of primes up to n. Note that this is a computationally
	expensive function since the remove method is not very efficient. """
	checks = [x for x in range(3, n, 2)]
	for i in checks:
		j = 2
		while i*j < n:
			product = i*j
			j += 1
			try:
				checks.remove(product)
			except ValueError:
				pass
	return([2] + checks)


if __name__ == "__main__":
        print(sum(primelist(2000000)))
