"""
Problem 99: Largest exponential
https://projecteuler.net/problem=99

Solution:
For every two numbers, reduce both sides to the 1/(largest exponential).
Then we can easily compare the two numbers.
"""


def largest_exponential(nums):
	"""Returns the line number of the largest exponential in a list of base
	exponent pairs."""
	n = 1
	best_base, best_exp = nums[0]
	for n in range(1, len(nums)):
		base, exp = nums[n]
		max_exp = max(exp, best_exp)
		if base**(exp/max_exp) > best_base**(best_exp/max_exp):
			result = n+1
			print(best_base, best_exp, base, exp)
			best_base, best_exp = base, exp
	return(result)


if __name__ == "__main__":
	f = [x.strip().split(",") for x in open("pe099.txt", "r").readlines()]
	base_exp_list = [[int(x) for x in line] for line in f]
	print(largest_exponential(base_exp_list))