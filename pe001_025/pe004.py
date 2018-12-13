"""
Problem:
A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Solution:
To consider all the products of two 3-digit numbers , we need to consider at most
900*899/2 unique combinations of such 3-digit numbers (handshake problem). 
Furthermore, it is best to start at the highest 3-digit numbers (999) and count
down to 100, since we are looking for the largest palindrome.

"""

def palindrome(n):
	"""Checks if n is a palindromic. Also works for strings."""
	word = str(n)
	sliceindex = int(len(word)/2)
	if word[:sliceindex] == word[:-sliceindex-1:-1]:
		return True
	else:
		return False


def largest_palindrome():
	"""Returns the largest palindrome made from the prod of two 3-digit num."""
	largest = 0
	for i in range(999, 99, -1):
		for j in range(999, 99, -1):
			product = i*j
			if palindrome(product):
				if product > largest:
					largest = product
				# If we find a palindrome for i, we can continue with i-1.
				break 
	return largest



