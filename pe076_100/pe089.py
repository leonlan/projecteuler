"""
Problem 89: Roman numerals
https://projecteuler.net/problem=89

Solution:
We create two functions, one that computes the numerical value 
from the given "inefficient" Roman numerals, and the other that
computes the shortest representation of a number in Roman numerals.
"""

def roman_numerals(list_of_words):
	roman_num_dict = {1000: 'M', 500: 'D', 100: 'C', 
						50: 'L', 10: 'X', 5: 'V', 1: 'I'}
	num_roman_dict = {v:k for k, v in roman_num_dict.items()}
	nums = [1000, 500, 100, 50, 10, 5, 1]

	def shortest_representation(n):
		"""Returns the shortest representations of n in Roman numerals."""
		s = ''
		for i in range(len(nums) - 1):
			while n >= nums[i]:
				n -= nums[i]
				s += roman_num_dict[nums[i]]
			step = 2 if i % 2 == 0 else 1
			while n >= nums[i] - nums[i+step]:
				n -= nums[i] - nums[i+step]
				s += roman_num_dict[nums[i+step]] + roman_num_dict[nums[i]]
		# Add last Is
		s += 'I'*n
		return(s)

	def roman_to_num(s):
		"""Computes the numerical value of a roman numeral string."""
		total = 0
		for n in range(len(s)):
			if n != len(s)-1 and num_roman_dict[s[n+1]] > num_roman_dict[s[n]]:
				total -= num_roman_dict[s[n]]
			else:
				total += num_roman_dict[s[n]]
		return(total)
	
	result = 0
	for word in list_of_words:
		result += len(word) - len(shortest_representation(roman_to_num(word)))
	return(result)


if __name__ == "__main__":
	numerals = [x.strip() for x in open("pe089.txt", "r").readlines()]
	print(roman_numerals(numerals))


