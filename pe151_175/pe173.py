"""
Problem 173: Using up to one million tiles how many different
"hollow" square laminae can be formed?
https://projecteuler.net/problem=173

Solution:
Let T be the number of tiles that can be used.

An square laminea is of the form:
n^2 - i^2 < T
n > i > 2
n, i same parity

Our approach is as follows:
- Calculate the upper bound N for n, which is the largest n such that
n**2 - (n-1)**2 < T.
- For every number n smaller than N and bigger than 1, check if n**2 - i**2 is less than
the number of tiles T. Here i is a multiple of 2 smaller than n and also less than n.
If this is indeed the case, add 1 to the counter.

This solves the problem.
"""
def square_laminae(T):
    """Calculates how many square lamniae can be formed with up to T tiles."""
    total = 0

    def sq_lam(n, i):
        """Calculates the number of tiles needed for a square lamniae of size n
        with hole of size i."""
        return(n**2-i**2)

    N = int((T + 4)//4) # Strict upper bound
    for n in range (N, 1, -1):
        i = n - 2
        while sq_lam(n, i) <= T and i >= 1:
            total += 1
            i -= 2
    return(total)


if __name__ == "__main__":
    print(square_laminae(10**6))
