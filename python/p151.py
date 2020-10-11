from collections import defaultdict


def next_states(state):
    """Returns a dictionary of the possible next states
    and its probability as key-value pairs.

    E.g. if state = [0, 0, 0, 1, 1] then it should return
    {[0, 0, 0, 0, 2]: 1/2, [0, 0, 0, 1, 0]: 1/2}
    """
    candidates = {}
    n = len(state)
    total = sum(state)
    for i, x in enumerate(state):
        if x > 0:
            p = x / total
            candidate = list(state)
            candidate[i] -= 1
            for j in range(i+1, n):
                candidate[j] += 1
            candidates[tuple(candidate)] = p
    return candidates


def p151():
    """Find the expected number of times that the supervisor finds
    a single sheet in the envelop."""
    T = 16
    expected = 0
    single_t = {8: (0, 1, 0, 0, 0), 12: (0, 0, 1, 0, 0), 14: (0, 0, 0, 1, 0)}
    current, next = {(1, 0, 0, 0, 0): 1},  defaultdict(int)
    for t in range(1, T+1):
        for curr_state, p in current.items():
            for next_state, q in next_states(curr_state).items():
                next[next_state] += p*q

        if t in single_t:
            expected += next[single_t[t]]

        current = next
        next = defaultdict(int)

    return round(expected, 6)


if __name__ == "__main__":
    print(p151())
