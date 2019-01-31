"""
Problem 174: Counting the number of "hollow" square laminae that
can form one, two, three, ... distinct arrangements

Solution:
Using the solution from problem 173, we can almost directly solve this
problem. Instead of counting the number of possible square laminaes,
we count the number of tiles of such sq. laminaes and count the
occurences of number of tiles in the dictionary L. Finally, we count
the occurences of L-types using a dictionay N.
"""
from collections import defaultdict


def square_laminae(T, Nmax):
    L = defaultdict(int)

    def sq_lam(n, i):
        """Calculates the number of tiles needed for a square lamniae of size n
        with hole of size i."""
        return(n**2-i**2)

    # Even case
    X = int((T + 4)//4) # Strict upper bound
    for n in range (X, 1, -1):
        i = n - 2
        while sq_lam(n, i) <= T and i >= 1:
            L[sq_lam(n, i)] += 1
            i -= 2

    N = defaultdict(int)
    for k, v in L.items():
        N[v] += 1

    return(sum([v for k, v in N.items() if k <= Nmax]))


if __name__ == "__main__":
    print(square_laminae(10**6, 10))
