"""
Problem 109: Darts
https://projecteuler.net/problem=109

Solution:

"""
from itertools import combinations_with_replacement
from collections import defaultdict


def darts_value(d1):
	"""Computes the value of a dart."""
	letters_to_mult = {'S': 1, 'D':2, 'T':3}
	return letters_to_mult[d1[0]]*int(d1[1:])


def pe109(N):
	nums = [x for x in range(1, 20+1)]
	darts = ['S25', 'D25']
	letters = ['S', 'D', 'T']
	for n in nums:
		for l in letters:
			darts.append(l+str(n))

	# Possible values of single darts
	singledarts = defaultdict(int)
	for d in darts:
		D = darts_value(d)
		singledarts[D] += 1

	# Possible values of double darts
	doubledarts = defaultdict(int)
	for d in combinations_with_replacement(darts, 2):
		D = darts_value(d[0]) + darts_value(d[1])
		doubledarts[D] += 1

	# Ways to checkout
	checkout = [2*x for x in range(1, 20+1)] + [50]
	ways = 0
	for score in range(2, N):
		for c in checkout:
			rem = score - c
			if rem > 0:
				ways += singledarts[rem] + doubledarts[rem]
			elif rem == 0:
				ways += 1
			else:
				break
	print(singledarts[1], doubledarts[1])
	return ways


if __name__ == "__main__":
	print(pe109(100))
