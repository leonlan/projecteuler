"""
Problem 113: Non-bouncy numbers
https://projecteuler.net/problem=113

Solution:
Dynamic programming. Let 

increasing_ways[n][d] := number of ways that a n-digit number
is increasing with last digit d

Similarly, define decreasing_ways[n][d]. 

Note that increasing numbers and decreasing numbers overlap
in numbers such as 1111 or 2222. Hence, we need to correct
for such numbers in the total of ways.
"""

def pe113(N):
	"""Calculates the number of non-bouncy numbers below 10^N."""
	ways = 0
	increasing_ways = [[0 for _ in range(10)] for _ in range(N+1)]
	decreasing_ways = [[0 for _ in range(10)] for _ in range(N+1)]
	for n in range(1, N+1):
		if n == 1:
			for d in range(0, 10):
				increasing_ways[n][d] += 1
				decreasing_ways[n][d] += 1
		else: 
			for d in range(0, 10):
				increasing_ways[n][d] = sum([increasing_ways[n-1][p] for p in range(0, d+1)])
			for d in range(9, -1, -1):
				decreasing_ways[n][d] = sum([decreasing_ways[n-1][p] for p in range(9, d-1, -1)])

	ways += sum([sum(x[1:]) for x in increasing_ways]) # Ignore 0-th entry
	ways += sum([sum(x[1:]) for x in decreasing_ways]) # Ignore 0-th entry
	ways -= 9*N # Overlapping numbers
	return ways


if __name__ == "__main__":
	print(pe113(100))