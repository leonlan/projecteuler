from math import floor

def summultiple(i, n):
	"""Calculates the sum of all multiples ì s.t. i < n."""
	cap = floor(n/i)
	summation = cap*(cap+1)/2
	return i*summation


# Find the sum of all the multiples of 3 or 5 below 1000.
n = 1000
print(summultiple(3,n)+summultiple(5,n)-summultiple(3*5,n))
