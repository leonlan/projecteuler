"""
Problem 45: Triangular, pentagonal, and hexagonal
https://projecteuler.net/problem=45

Solution:
We use a brute force method by creating 2 sets of length N 
with all pentagonal and hexagonal numbers respectively.
Then we intersect the three arrays to see which numbers are in all
three arrays. Note that all hexagonal numbers are triangular, so
we do not need to check the triangular numbers.
"""


def tri_penta_hex(N):
	"""Finds the second triangle number that is also pentagonal and hexagonal.
	Searches up to the index N."""
	def pen(n):
		return(n*(3*n-1)//2)

	def hex(n):
		return(n*(2*n-1))

	# 1. Initialize the arrays
	pennums = set()
	hexnums = set()

	j = 144
	while j < N:
		pennums.add(pen(j))
		j += 1
	
	k = 144
	while k < N:
		hexnums.add(hex(k))
		k += 1

	# 2. Intersection
	tripenhex = pennums.intersection(hexnums)
	return(min(tripenhex))


if __name__ == "__main__":
	print(tri_penta_hex(100000))