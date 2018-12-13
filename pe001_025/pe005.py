import numpy as np
"""
Problem:
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder. What is the smallest positive number that 
is evenly divisible by all of the numbers from 1 to 20?

Solution:
Very lazy solution. Should use LCM in future.

"""

L = np.arange(11,20+1)

i = 0
while True:
    i+=20
    if np.all(i%L==0):
        print(i)
    break