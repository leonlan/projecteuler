"""
Problem 38: Pandigital multiple
https://projecteuler.net/problem=38

Solution:
The problem states a lower bound for the pandigital number, namely
918273645. This means that we need to start searching with at x = 91.

We can surely exclude 3-digit numbers because of the previous statement.
Since any 3-digit number must start with 91 or larger, each double (2x)
and triple multiple (3x) of such number will contain 4 digits each. The
total number of digits exceeds 9, so it cannot be 9-digit pandigital.

The same applies to 2-digit numbers. We have that 2x, 3x and 4x
has triple digits each, so the total number of digit equals 2+3+3+3 = 11.
In other words, using 2-digit of 3-digit numbers we can never form
concatenated 9-digit pandigital numbers. (This also does not hold for
1-digit numbers, which has only one case with x = 9.)

The only case that remains is 4-digit numbers. Here, we see that it is
possible to form 9 digit numbers since any 4-digit number starting with 91
has a double multiple (2x) with 5 digits. The solution is to check all
4-digit numbers starting with at least 91 and check if it forms a pandigital
number when concatenated with its double multiple. So:

9100 <= x <= 9999

Since we are looking for the largest number, we can start with x = 9999 and
search in decreasing order.

Note that any number with repeated digits should be excluded, but since
our search pool is small, there's no need to exclude them.
"""


def is_pandigital(n):
    """Checks whether n is a 9-digit pandigital number."""
    return('123456789' == "".join(sorted(str(n))))


def pandigital_multiple():
    for x in range(9999, 9100-1, -1):
        n = str(x) + str(x*2)
        if is_pandigital(n):
            return(int(n))


if __name__ == "__main__":
    print(pandigital_multiple())
