"""
Problem 37: Truncatable primes
https://projecteuler.net/problem=37

Solution:
- Only numbers starting with {2, 3, 5, 7} or ending with {3, 7} should
be considered as primes.

"""
import sys
sys.path.append("..")
from helperfunctions import prime


def is_truncatable(n):
    """Checks if n is a truncatable prime."""
    s = str(n)

    # First digit in {3, 5, 7} and last digit in {3, 7}
    if len(s) > 1 and s[0] in ['2', '3', '5', '7'] and s[-1] in ['3', '7']:
        for i in range(len(s)-1):
            if not (prime(int(s[:len(s)-i])) and prime(int(s[i:len(s)]))):
                return(False)
        return(True)
    else:
        return(False)


def truncatable_primes():
    """Finds the sum of the 11 truncatable primes."""
    result = 0
    n, count = 1, 0
    while count < 11:
        if is_truncatable(n):
            result += n
            count += 1
        n += 2
    return(result)


if __name__ == "__main__":
    print(truncatable_primes())
