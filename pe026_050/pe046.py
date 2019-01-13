"""
Problem 46: Goldbach's other conjecture
https://projecteuler.net/problem=46

Solution:
An odd composite numbers takes the form 2*n + 1 where n is a positive integer,
where we exclude the prime numbers.

To check if a number N satisfies the conjecture, we check if N-2*(i^2) (for all i
such that N-2*(i^2) > 2) is prime. If so, then we continue, otherwise we have 
found the smallest composite number that cnanot be written as the sum of a prime
and twice a square.   

I also made another version, which uses the sieve method. Since the answer is a
fairly small number, time differences between the two methods are small.

"""
import sys
sys.path.append("..")
from helperfunctions import prime_sieve


def check(n, prime_set, cache):
	"""Checks if n can be written as the sum of a prime and twice a square."""
	
	def goldbachdiff(n, i):
		return(n-2*i**2)
	
	i = 0
	G = goldbachdiff(n, i)
	while G >= 0:
		if G in cache or G in prime_set:
			cache.add(G)
			return(True)
		else:
			i += 1
			G = goldbachdiff(n, i)
	return(False)


def goldbachs_other_conjecture(N):
	"""Finds the smallest odd composite that cannot be written as the sum
	of a prime and twice a square. Search up to N."""
	primes = set(prime_sieve(N))	
	candidates = [N]
	cache = set()

	# Odd composite type 1: 9 + 6n
	x = 3
	while x < N:
		if not check(x, primes, cache):
			candidates.append(x)
			break
		x += 2
	return(min(candidates))


def version2(N):
	"""Builds a sieve to check which number is not the sum of a prime and
	two squares. Checks up to N."""
	def goldbachsum(n, i):
		return(n+2*i**2)

	sieve = [1]+(N-1)*[0]
	primes = list(prime_sieve(N))
	for p in primes:
		i = 0
		G = goldbachsum(p, i)
		while G < N:
			sieve[G-1] = 1
			i += 1
			G = goldbachsum(p, i)
	return(sieve[::2].index(0)*2+1)


if __name__ == "__main__":
	print(goldbachs_other_conjecture(1000000))
	# second version
	# print(version2(1000000))