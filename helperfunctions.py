from math import ceil, sqrt
"""
Prime numbers
	* prime(n)
		A number n is prime if:
			- It is not even.
			- It does not have a divisor smaller than sqrt(n).
			- From the above conditions, we can exclude even divisors.
	* 

"""

def prime(n):
	"""Returns whether n is prime or not."""
	
	# Case 1: n is even
	if n % 2 == 0:
		return False

	# Case 2: n is odd	
	for i in range(3, ceil(sqrt(n))+1, 2):
		if n % i == 0:
			return False

	return True
	
def primelist(n, length=False):
	"""Returns the list of primes up to n. 
	If length = TRUE, return the first n prime numbers."""
	primes = [2]
	
	# Case 1: all primes up to n.
	if not length:
		for i in range(3, n+1, 2):
			if prime(i):
				primes.append(i)

	# Case 2: the first n prime numbers.
	else:
		j = 3
		while len(primes) < n:
			if prime(j):
				primes.append(j)
			j += 1
	return(primes)