"""
Problem:
The sum of the squares of the first ten natural numbers is,
	1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
	(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

Solution:
The sum of the sequence of squared positive integers up to n is:
	1^2 + 2^2 + ... + n^2 = n(n+1)(2n+1)/6

The sum of the sequence of positive integers up to n is:
	1 + 2 + ... + n = n(n+1)/2

Hence the square of the sum of the sequence of n is
	n^2(n-1)^2/4

"""

def diff_sumsq_sqsum(n):
	"""Finds the difference between the sum of squares of the first n natural
	numbers and the square of the sum"""
	sumsq = n*(n+1)*(2*n+1)/6
	sqsum = (n**2)*((n+1)**2)/4
	return(sqsum-sumsq)