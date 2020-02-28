"""
Problem 90: Cube digit pairs
https://projecteuler.net/problem=90

Solution:
-
"""
from itertools import combinations


def sq_num(die1, die2):
	"""Checks if die1 and die2 can display all square numbers."""
	sqn = ['01', '04', '09', '16', '25', '36', '49', '64', '81']
	poss = set()
	for d1 in die1:
		for d2 in die2:
			poss.add(d1+d2)
			poss.add(d2+d1)
			if d1 == '6':
				poss.add('9'+d2)
				poss.add(d2+'9')
			if d1 == '9':
				poss.add('6'+d2)
				poss.add(d2+'6')
			if d2 == '6':
				poss.add(d1+'9')
				poss.add('9'+d1)
			if d2 == '9':
				poss.add(d1+'6')
				poss.add('6'+d1)

	# print(poss)
	for n in sqn:
		if n not in poss:
			return(False)
	return(True)


def distinct_sets(set1, set2):
	"""Checks if set 1 is distinct from set 2."""
	s10, s11 = set1[0], set1[1] 
	s20, s21 = set2[0], set2[1]
	if (s10 == s20 and s11 == s21) or (s10 == s21 and s11 == s20):
		return(False)
	else:
		return(True)


def pe090():
	"""Computes the number of distinct arrangements of two dice
	for all square numbers to be displayed."""
	dice = list(combinations([str(n) for n in range(10)], 6))
	distinct = []
	for die1 in dice:
		for die2 in dice:
			if sq_num(die1, die2):
				distinct.append([set(die1), set(die2)])
	return(len(distinct)//2)


if __name__ == "__main__":
	print(pe090())