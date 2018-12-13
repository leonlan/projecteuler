"""
Problem 34: Digit factorials
https://projecteuler.net/problem=34

Solution:
Lower bound is 3! and the lower bound is 7*9! = 2540160.
"""

from math import factorial

def digit_factorial(n):
    return(sum([factorial(int(x)) for x in str(n)]))

def all_digit_factorials():
    sum = 0
    for i in range(3, 2540160+1):
        if i == digit_factorial(i):
            sum += i
    return(sum)

if __name__ == "__main__":
    print(all_digit_factorials())
