"""
Problem:
https://projecteuler.net/problem=25

What is the index of the first term in 
the Fibonacci sequence to contain 1000 digits?

"""

def fibonnaci_digit(n):
    """Returns the idx of the first term in the Fibonacci seq with n digits."""
    x = [1,1]
    idx = 2
    while len(str(x[1])) != n:
        x[1] = x[1] + x[0]
        x[0] = x[1] - x[0]
        idx += 1
    return(idx)

print(fibonnaci_digit(1000))