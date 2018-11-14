import numpy as np
from helperfunctions import properdivisors

"""
Problem:
https://projecteuler.net/problem=23


Find the sum of all the positive integers which cannot be written as the sum 
of two abundant numbers.
"""

def abundantnumbers(n):
    """Returns the list of abundant numbers up to n."""
    return([i for i in range(1,n) if sum(properdivisors(i)) > i])

def nonabundantsum():
    """Computes the sum of all positive, non-abundant integers."""
    x = np.array(abundantnumbers(28124))
    sum_of_abundantnums = np.unique(x[:,np.newaxis]+x[np.newaxis,:])
    nonabundantnums = np.setdiff1d(np.arange(1,28124), sum_of_abundantnums)
    return(sum(nonabundantnums))
