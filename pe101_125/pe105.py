"""
Problem 105: Special subset sums: testing
https://projecteuler.net/problem=105

Solution:
We implement a function that checks
1)  S(B) ≠ S(C); that is, sums of subsets cannot be equal.
2)  If B contains more elements than C then S(B) > S(C).

How? Let's take some set A for example. For each possible
subset B with 2 <= |B| <= |A|, we find all possible subsets
C with 1 <= |C| <= |B|. If |C| = |B|, we check for equality,
as per the first requirement. Otherwise, we check for strict
inequality for the second requirement. 

Finding all possible subsets can be easily done with the
combinations function from itertools. Moreover, the set
operations will come in handy as well.

Note that defining a second function will make life much
easier, as you don't need to break all for loops. Instead,
returning 0 if requirement 1) or 2) does not hold yields
the correct results.
"""
from itertools import combinations

def specialsumset(A):
	"""Returns S(A) if A is a special sumset"""
	for i in range(2, len(A)):
		# Create subsets B
		subsetsB = combinations(A, i)
		for B in subsetsB:
			sumB = sum(B)
			remaining = A-set(B)
			for j in range(1, i+1):
				# Create subsets C
				subsetsC = combinations(remaining, j)
				for C in subsetsC:
					if j == i:
						if sum(B) == sum(C):
							return(0)
					else:
						if sum(B) <= sum(C):
							return(0)
	return(sum(A))


def pe105(sets):
	"""Returns S(A) for all special sum sets in sets"""
	S = 0
	for A in sets:
		# Check for duplicate elements
		if len(set(A)) == len(A):
			S += specialsumset(set(A))
	return(S)


if __name__ == "__main__":
	f = open("pe105.txt").readlines()
	A = [x.rstrip().split(',') for x in f]
	sets = [[int(x) for x in set] for set in A]
	print(pe105(sets))
