"""
Problem 21: Amicable numbers
https://projecteuler.net/problem=21
"""
from helperfunctions import properdivisors
import sys
sys.path.append("..")


def amicable_numbers(n):
    """Returns the sum of all amicable numbers up to n."""
    amicablepairs = set()
    amicabledict = {}

    for i in range(2, n):
        amicabledict[i] = sum(properdivisors(i))

    for key, value in amicabledict.items():
        try:
            if amicabledict[value] == key and key != value:
                amicablepairs.add(key)
                amicablepairs.add(value)
        except KeyError:
            pass
    return(sum(amicablepairs))


if __name__ == "__main__":
    print(amicable_numbers(10000))
