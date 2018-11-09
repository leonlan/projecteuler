from math import ceil, sqrt
from helperfunctions import *

"""
Problem:
What is the largest prime factor of the number 600851475143?

Solution:
By the Fundamental Theorem of Arithmetic, we know that every number has a unique
prime factorization. So to find the largest prime factor, we can instead find
the prime factorization. 
 	
"""
def largestprimefactor(n):
	"""Returns the largest prime factor of n."""
	divisors = []
	remainder = n
	primes = primelist(ceil(sqrt(n)))

	if prime(n):
		return(n)

	while remainder != 1:
		for i in primes:
			print(i)
			if remainder % i == 0:
				divisors.append(i)
				remainder = int(remainder/i)
				break

	return max(divisors)