"""
Problem 55: Lychrel numbers
https://projecteuler.net/problem=55

"""
import sys
sys.path.append("..")
from helperfunctions import is_palindrome, reverse


def lychrel_numbers(N):
    """Finds all Lychrel numbers below N."""
    count = 0
    non_lychrel = set()

    for k in range(0, N):
        n = k + reverse(k)
        seq = set([n])

        for _ in range(50):
            if is_palindrome(n) or n in non_lychrel:
                count += 1
                # If we find a non-Lychrel, store these numbers
                for x in seq:
                    non_lychrel.add(x)
                print(k)
                break
            else:
                n += reverse(n)
                seq.add(n)
    return(N-count)


if __name__ == "__main__":
    print(lychrel_numbers(10**4))
