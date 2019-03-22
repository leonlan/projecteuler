"""
Problem 128: Hexagonal tile differences
https://projecteuler.net/problem=128

Solution:
For every tile, the goal is to find the neighborhood of tiles.
The process for the neighborhood points is different for corner
points and non-corner point. A corner point is defined as a tile
that lies at one of the 6 corners of the corresponding hexagon-ring.

It can be shown that only corner points or the last non-corner point
can have PD(n) = 3.
"""
import sys
sys.path.append("..")
from helperfunctions import prime


def hexagonal_tile_differences(N):
    """Finds the N-th tile in the PD(n) sequence."""

    def PD(n, nbhd):
        """Calculates the number of primes in the difference nbhd of n."""
        count = 0
        for i in nbhd:
            if prime(abs(i-n)):
                count += 1
        return(count)

    def H(n):
        """Returns number of total tiles in a hexagon tile with n rings."""
        return(1+6*((n+1)*(n)//2))

    def R(n):
        """Returns the length of the n-th hexagon ring."""
        if n == 0:
            return(1)
        else:
            return(6*n)

    def M(n, k):
        """Returns the tile number on the n-th hexagon ring and k-th position."""
        if n == 0:
            return(1)
        else:
            return(H(n-1) + 1 + k)

    n = 1
    PDcount = [1]
    while len(PDcount) < N:
        i = 0
        prevR = R(n-1)
        currR = R(n)
        nextR = R(n+1)
        prevn = n - 1
        nextn = n + 1
        pool = list(range(0, currR, n))
        if n > 1:
            pool.append(currR-1)

        for k in pool:
            tile = M(n, k)
            nbhd = []
            nbhd.extend([M(n, (k+1)%currR), M(n, (k-1)%currR)])

            # Corner point
            if k % n == 0:
                nbhd.extend(
                    [M(nextn, i*nextn),
                     M(nextn, (i*nextn-1) % nextR),
                     M(nextn, (i*nextn+1) % nextR),
                     M(prevn, i*prevn)])
                i += 1

            # Non-corner point
            else:
                nbhd.extend(
                    [M(nextn, k+i),
                     M(nextn, k+i-1),
                     M(prevn, k-i),
                     M(prevn, (k-i+1) % prevR)
                    ])

            if PD(tile, nbhd) == 3:
                PDcount.append(tile)
        n += 1
    return(PDcount[N-1])


if __name__ == "__main__":
    print(hexagonal_tile_differences(2000))
