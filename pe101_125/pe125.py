"""
Problem 125: Palindromic sums
https://projecteuler.net/problem=125

Solution:
This problem is similar to problem 50. There exists a O(n) algorithm
which checks if a particular number is the sum of some subsequence of
the array.
- First we generate all palindromes up to N.
- Then we use the O(n) algorithm to check all palindromes as consecutive
sums of an array. The only note-worthy optimization is that we can
stop searching for palindrome p if for the starting position start we
have squares[start]*2 > p, as we cannot find sums beyond index start
that would equal p (they would exceed p).


"""
from math import ceil


def palindromic_numbers(D):
    """Generates all palindromic numbers up to D digits."""

    def reverse(n):
        return(str(n)[::-1])

    palindromes = []
    for d in range(1, D+1):
        for n in range(10**(ceil(d/2)-1), 10**(ceil(d/2))):
            if d != 1:
                if d % 2 == 0:
                    x = int(str(n)+reverse(n))
                else:
                    x = int(str(n)+reverse(str(n)[:-1]))
            else:
                x = n
            palindromes.append(x)
    return(palindromes)


def palindromic_sums(N):
    """Returns all numbers below N which are palindromic and the sum of
    square numbers."""
    squares = [x**2 for x in range(1, int(N**0.5+2))]
    palindromes = [x for x in palindromic_numbers(9) if x < N]
    max_idx = len(squares)
    total = 0
    n = 0
    for p in palindromes:
        idx = 1
        start = 0
        consecutive_sum = squares[0]
        while idx < max_idx and squares[start]*2 <= p:
            consecutive_sum += squares[idx]

            # Remove starting numbers of the sum exceeds p
            while consecutive_sum > p:
                consecutive_sum -= squares[start]
                start += 1

            # Exclude palindromes that are squares themselves
            if consecutive_sum == p and start != idx:
                total += consecutive_sum
                n+=1
                break
            idx += 1

    return(total)


if __name__ == "__main__":
    print(palindromic_sums(10**8))
