"""
Problem 286: Scoring probabilities
https://projecteuler.net/problem=286

Solution:
DP approach with binary search. Define

p[t, s] = probability of s scores with t throws
"""
def pe286(X, S, chance):
	"""Computes the constant q for X throws from x = 1, 2, ..., X
	with S succesful throws."""
	def probability(q):
		p = [[0 for s in range(t+2)] for t in range(X+1)]
		for x in range(1, X+1):
			Pmiss = x/q
			Phit = 1-x/q
			if x == 1:
				p[x][0] = Pmiss
				p[x][1] = Phit
			else:
				for s in range(0, x+1):
					if s == 0:
						p[x][s] = (p[x-1][s]*Pmiss)
					else:
						p[x][s] = (p[x-1][s]*Pmiss + p[x-1][s-1]*Phit)
		return p[X][S]

	# Bisection method
	low = 50
	high = 100
	accuracy = 10**(-14)
	while high-low > accuracy:
		mid = (high+low)/2
		if probability(mid) < chance:
			high = mid
		else:
			low = mid

	return high


if __name__ == "__main__":
	print(format(pe286(50, 20, 0.02), '2.10f'))
