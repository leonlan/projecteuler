"""
Problem 118: Pandigital prime sets
https://projecteuler.net/problem=118

Solution:
From problem 41, it follows that there are no 7+ digit pandigital numbers. 
Therefore, we don't need to compute any 9 digit primes, and we only compute
the primes up to (and including) 8 digits that do not contain any repeated
digits. 

Using these prime numbers, we compute all possible prime combinations that
are pandigital. 

"""
import sys
sys.path.append("..")
from helperfunctions import prime_sieve
from itertools import combinations


def pe118(n):
	"""Returns the number of distinct pandigital prime sets."""

	def repeated_digits(n):
		"""Checks if n contains repeated digits."""
		s = str(n)
		digits = set()
		for c in s:
			if c not in digits:
				digits.add(c)
			else:
				return True
		return False

	def zero(n):
		"""Checks if n contains 0."""
		s = str(n)
		if '0' in s:
			return True
		else:
			return False

	# Compute all primes up to 8 digits
	P = [set() for x in range(n+1)] # P[n] = Primes with n-digits
	for p in prime_sieve(10**(min(8,n))):
		# Exclude repeated digit primes and primes with 0
		if not repeated_digits(p) and not zero(p): 
			P[len(str(p))].add((str(p),))

	# Compute all combinations of prime numbers
	C = [set() for x in range (n+1)] # C[n] = Possible combinations prime nums with n-digits
	for d in range(1, n+1):
		C[d] = P[d]
		for i in range(1, (d+1)//2+1):
			S1 = C[i]
			S2 = C[d-i]
			for el1 in S1:
				for el2 in S2:
					s = ''.join(el1+el2)
					if not repeated_digits(s):
						# If el1+el2 has no repeated digits, add to C[d]
						# and then also el2+el1 does not contain repeated digits
						C[d].update([el1+el2, el2+el1])
						
	# Compute the distinct sets of pandigital prime sets
	distinct_pdp = set()
	for poss in C[n]:
		distinct_pdp.add(frozenset(poss))
	return len(distinct_pdp)


if __name__ == "__main__":
	print(pe118(9))