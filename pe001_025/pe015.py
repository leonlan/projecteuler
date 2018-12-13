"""
Problem 15: Lattice paths
https://projecteuler.net/problem=15

Solution:
This is a case of permutations with repetitions. See this link
for example: https://brilliant.org/wiki/permutations-with-repetition/
"""
from math import factorial

if __name__ == "__main__":
    print(factorial(40)/factorial(20)/factorial(20))
