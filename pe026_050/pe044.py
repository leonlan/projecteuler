"""
Problem 44: Pentagon numbers
https://projecteuler.net/problem=44

Solution:
Checking if x is a pentagon number is equivalent to checking
whether n = (1+sqrt(1+24x))//6 is an integer (see Wikipedia).

Next, we loop over all n >= 1 and check for all m < n whether
(Pn-Pm) and (Pn+Pm) is pentagonal. We decreasingly loop over m
since we are looking for the minimum difference.

"""
from itertools import combinations


def pent(n):
    """Returns the n-th pentagon number."""
    return(n*(3*n-1)//2)


def is_pentagon(x):
    """Checks if x is a pentagon number."""
    return((1+(1+24*x)**0.5)%6==0)



def pentagon_numbers():
    """Returns the minimum difference of two pentagon numbers of
    which the difference and sum is also a pentagon number."""
    n = 1
    while True:
        m = n - 1
        while m > 0:
            if is_pentagon(pent(n)-pent(m)) and is_pentagon(pent(n)+pent(m)):
                return(pent(n)-pent(m))
            else:
                m -= 1
        n += 1


if __name__ == "__main__":
    print(pentagon_numbers())
