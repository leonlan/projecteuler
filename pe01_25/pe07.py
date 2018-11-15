import sys
sys.path.append('..')
from helperfunctions import prime, primelist
"""
Problem: 

By listing the first six prime numbers: 
	2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?


Solution:
See helperfunctions.
"""

print(max(primelist(10001, length=True)))