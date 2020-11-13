from math import exp
from sympy import factorint
from collections import defaultdict


def compute_k(N):
    """Returns k* for which (N/k)^k is maximized."""
    return round(N*exp(-1))


def is_terminating(n, d):
    """Checks if the fraction n/d is terminating or not."""
    fn = defaultdict(int, factorint(n))
    fd = defaultdict(int, factorint(d))

    # Cancel terms which occur both in fn and fd
    for k, v in fn.items():
        c = min(fn[k], fd[k])
        fn[k] -= c
        fd[k] -= c

    # Check if denominator only contains 2s and 5s
    for k, v in fd.items():
        if k not in [2, 5]:
            if v > 0:
                return False
    return True


def D(N, k):
    """Returns N if N/k is non-terminating decimal and -N otherwise."""
    if is_terminating(N, k):
        return -N
    else:
        return N


def p183(N):
    """Finds the sum of all D(n) for 5 <= n <= N."""
    total = 0
    for n in range(5, N+1):
        k = compute_k(n)
        total += D(n, k)
    return total


#if __name__ == "__main__":
print(p183(10000))
