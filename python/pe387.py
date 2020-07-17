"""
Problem 387: Harshad Numbers
https://projecteuler.net/problem=387

Solution:
For 1 <= n <= 14,
we check which numbers between 10^(n-1) and 10^(n) are
truncatable Harshad numbers. This is done using memoization.
In every n-th layer, if we have found all truncatable Harshad
numbers, we check if it strong. If it is strong, then we extend
with [1, 3, 7, 9] to check if it is a strong, right-truncatable
Harshad prime.
"""
import sys
sys.path.append("..")
from helperfunctions import prime as is_prime


def pe387(n):
    """Finds all strong, right-truncatable Harshad primes less
    than 10^(n-1)."""

    def is_strong_harshad(n):
        """Checks if n is a strong Harshad number."""
        total = sum([int(c) for c in str(n)])
        return((n%total==0) and (is_prime(n//total)))


    def is_harshad(n):
        """Checks if n is a Harshad number."""
        total = sum([int(c) for c in str(n)])
        return((n%total==0))


    total = 0
    old_pool = [n for n in range(1, 10) if is_harshad(n)]
    for k in range(1, n):
        new_pool = []
        for num in old_pool:
            for ext in range(0, 10):
                new = int(str(num)+str(ext))
                if is_harshad(new):
                    new_pool.append(new)

        for num in new_pool:
            if is_strong_harshad(num):
                for ext in [1, 3, 7, 9]:
                    x = int(str(num)+str(ext))
                    if is_prime(x):
                        total += x
                        print(x)

        old_pool = new_pool

    return(total)


if __name__ == "__main__":
    print(pe387(13))
