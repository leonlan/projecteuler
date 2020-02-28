"""
Problem 26: Reciprocal cycles
https://projecteuler.net/problem=26
"""
def pe026(N):
	"""Finds the fraction 1/n with n = 1, ..., N with the largest
	repeating cycle."""
	cycles = [0 for x in range(N)]
	for n in range(1, N):
		count = 0
		rems = set()
		rem = 1
		while rem not in rems:
			rems.add(rem)
			rem = (rem * 10) % n
			count += 1
		cycles[n] = count
	return(cycles.index(max(cycles)))


if __name__ == "__main__":
	print(pe026(1000))