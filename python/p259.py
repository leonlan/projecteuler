from itertools import product
from quicktions import Fraction as F


def two_partitions(n):
    """Returns a list of all 2 parititons of a number.
    The partitions are returned as a tuple. """
    partitions = [(i, n-i) for i in range(1, n)]
    return partitions


def concat_num(l, r):
    """Returns the concated number starting at l and ending at r."""
    s = ''.join([str(x) for x in range(l, r+1)])
    return F(s)


def global_operator(a, b):
    """Returns the set of outcomes using a x b,
    where x is +, -, * or /."""
    outcomes = [a+b, a-b, a*b]
    if abs(b) != 0:  # Prevent floating point errors
        outcomes.append(a/b)
    return set(outcomes)


def global_operation(S1, S2):
    """Returns the global operation between the set S1 and S2."""
    new_set = set()
    for a, b in product(S1, S2):
        new_set.update(global_operator(a, b))

    return new_set


def p259():
    """
    """
    N, L, R = 10, 10, 10

    # Initialization
    S = [[[set() for r in range(R)] for l in range(L)] for n in range(N)]
    for n in range(1, N):
        for l in range(1, L):
            for r in range(1, R):
                if r-l+1 == n:
                    S[n][l][r].add(concat_num(l, r))

    # Computation
    for n in range(2, N):
        for l in range(1, N-n+1):
            r = l+n-1
            for a, b in two_partitions(n):
                start_a, end_a = l, l+a-1
                start_b, end_b = l+a, l+a+b-1
                Sa = S[a][start_a][end_a]
                Sb = S[b][start_b][end_b]
                S[n][l][r].update(global_operation(Sa, Sb))

    # Sum all reachable nums that are positive integers
    reachable_nums = sum([int(x) for x in S[9][1][9]
                          if x.denominator == 1 and x >= 0])
    return reachable_nums


if __name__ == "__main__":
    print(p259())
