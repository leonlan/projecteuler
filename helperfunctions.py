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
	# Case 0: n is 0, 1 or negative
	if n < 2:
		return False
	
	# Case 1: n = 2
	elif n == 2:
		return True

	# Case 1: n is even
	elif n % 2 == 0:
		return False

	# Case 2: n is odd	
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


def properdivisors(n):
	"""Returns the list of proper divisors of n."""
	propdiv = [1]

	for i in range(2, ceil(sqrt(n))):
		if n%i == 0:
			propdiv.extend([i, n//i])

	# If n is a perfect square, also add the square root.
	# Note: this does not work for VERY LARGE n. 
	if sqrt(n).is_integer() and n != 1:
		propdiv.append(int(sqrt(n)))
	
	return(propdiv)
	


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

