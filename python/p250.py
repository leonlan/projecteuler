from collections import defaultdict
from itertools import chain, combinations


def p250(N):
    """Finds the number of non-empy subsets of {1^1, 2^2, ..., N^N},
    the sum whose elements is divisible by 250."""

    # Initialization
    total = 0
    S = [pow(i, i, 250) for i in range(1, N+1)]
    curr = defaultdict(int)
    prev = defaultdict(int)

    # Dynamic programming scheme
    for i, n in enumerate(S):
        if i == 0:
            curr[n] += 1
        else:
            curr[n] += 1
            for k, v in prev.items():
                curr[k] += v
                curr[(k+n) % 250] += v
            for k, v in curr.items():
                curr[k] = curr[k] % 10**16
        prev = curr
        curr = defaultdict(int)
    return prev[0]



def test(n):
    """Brute-force test function for input values up to n=23."""
    if n > 23:
        return "Input size too large. Try something smaller than 24."""

    def powerset(iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

    total = 0
    S = [i**i for i in range(1, n+1)]
    L = []
    for x in powerset(S):
        if sum(list(x)) % 250 == 0 and x:
            total += 1
    return total


if __name__ == "__main__":
    print(p250(250250))
