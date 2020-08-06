from collections import defaultdict
from itertools import combinations
import numpy as np


def p201(N, K):
    """Determine the sum of all integers which are the sum of exactly
    one of the K-element subsets of S, where S = {1^2, 2^2, ..., N^2}."""

    # Initialization
    S = [i ** 2 for i in range(1, N + 1)]

    def make_dict(k):
        return {i: defaultdict(int) for i in range(k + 1)}

    prev = make_dict(1)
    curr = make_dict(1)

    # Dynamic programming scheme
    for i, n in enumerate(S):
        for k in range(1, min(i + 2, K + 2)):
            if i == 0:
                curr[1][1] = 1
                curr[0][0] = 0

            else:
                if k == 1:
                    # Add for each previous k-1 items, add the current num
                    curr[k][n] += 1
                if k > 1:
                    # Add for each previous k-1 items, the current num
                    # to get the curr k items
                    # but also, copy the previous k-1 items to the curr k-1 items
                    for s, count in prev[k - 1].items():
                        # Add n on top of previous items
                        curr[k][n + s] += count

                        # Copy previous items
                        curr[k - 1][s] += count

        prev = curr
        curr = make_dict(k+1)

    # Compute the sum of subsets sums which are unique
    total = sum([k for k, v in prev[K].items() if v == 1])

    return total


def p201_old(N, K):
    """
    FIRST VERSION: Runs too slow using np.zeros arrays. Iterating over all s
    takes too long and is in fact unnecessary. Kept for documentation.

    Determine the sum of all integers which are the sum of exactly
    one of the K-element subsets of S, where S = {1^2, 2^2, ..., N^2}."""

    # Initialization
    S = [i ** 2 for i in range(1, N + 1)]
    D = np.zeros((N + 1, K + 1, sum(S) + 1))

    # Dynamic programming scheme
    i = 0
    for n in range(1, N + 1):
        x = S[n - 1]
        partial_sum = sum([i ** 2 for i in range(1, n + 1)])
        for k in range(min(n + 1, K + 1)):
            for s in range(partial_sum + 1):
                # Base case
                if n == 1:
                    if k == 1:
                        D[n][k][1] = 1
                    elif k == 0:
                        D[n][k][0] = 1

                # Steps
                else:
                    D[n][k][s] += D[n - 1][k - 1][s - x]
                    D[n][k][s] += D[n - 1][k][s]

    # Compute the sum of subsets sums which are unique
    total = sum([idx for idx, count in enumerate(D[N][K]) if count == 1])
    print(total)
    return D


def test(N, k):
    """Brute-force test function for small numbers."""
    sums = defaultdict(int)
    S = [i ** 2 for i in range(1, N + 1)]
    for subset in combinations(S, k):
        sums[sum(subset)] += 1

    return sum([k for k, v in sums.items() if v == 1])


if __name__ == "__main__":
    print(p201(100, 50
    ))
