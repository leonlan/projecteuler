from math import comb
import numpy as np
from collections import defaultdict
import time


def mcs(T, k):
    """Monte carlo sampling method for p323."""
    def weighted_sum(dd):
        return sum([k*v for k, v in dd.items()]) / sum(dd.values())

    turns = defaultdict(int)
    for t in range(T):
        x = np.zeros(k, dtype="int")
        i = 0
        while any(x != 1):
            y = np.random.randint(2, size=k)
            x = x | y
            i += 1
            Turns[i][sum(x)] += 1
        turns[i] += 1

    return T, weighted_sum(turns)


def p(i, j, k):
    """Calculate the probability that a random k-bit integer
    with i-ones XORs with another random k-bit integer s.t.
    exactly j-ones occurs."""
    return 2**i * comb(k-i, j-i) / (2**k)


def next_states(state, K):
    """Returns a dictionary of the possible next states
    and its probability as key-value pairs.

    State definition: X := number of 1-bits assigned

    E.g. if state = 0 and K = 2, then it should return
    {0: 1/4, 1: 1/2, 2: 1/4}
    """
    candidates = {}
    for j in range(state, K+1):
        candidates[j] = p(state, j, K)
    return candidates


def p323(K, alpha=2):
    """Finds the expected value of N for 0 <= y < 2**K."""
    T = alpha  # Number of turns
    expected = 0
    current, next = {0: 1}, defaultdict(int)

    for t in range(1, T+1):
        for curr_state, p in current.items():
            for next_state, q in next_states(curr_state, K).items():
                next[next_state] += p * q
        current = next
        next = defaultdict(int)

        expected += t * current[K]
        del current[K]

    return round(expected, 10)


if __name__ == "__main__":
    # print(mcs(10000, 32))  # Monte-carlo simulation
    print(p323(32, 200))
