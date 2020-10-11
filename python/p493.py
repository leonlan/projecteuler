from collections import defaultdict

def next_states(state):
    """Returns a dictionary of the possible next states
    and its probablity as key-value pairs.

    E.g. if state = (10, 10, 10) then it should return
    {(9, 10, 10): 1/3, (10, 9, 10): 1/3, (10, 10, 9): 1/3}
    """
    candidates = {}
    total = sum(state)
    for i, x in enumerate(state):
        if x > 0:
            p = x / total
            candidate = list(state)
            candidate[i] -= 1
            candidates[tuple(candidate)] = p
    return candidates


def distinct_colors(state):
    """Calculate the number of distinct colors given a state.

    E.g. if state = (10, 9, 8) then it should return 2;
         if state = (10, 10, 10) it should return 0
    """
    colors = 0
    for n in state:
        if n != 10:
            colors += 1
    return colors


def p493():
    """Compute the expected number of distinct colours in
    20 randomly picked balls."""
    T = 20
    expected = 0
    current, next = {(10, 10, 10, 10, 10, 10, 10): 1}, defaultdict(int)
    for t in range(1, T+1):
        for curr_state, p in current.items():
            for next_state, q in next_states(curr_state).items():
                next[next_state] += p*q

        current = next
        next = defaultdict(int)

    for state, p in current.items():
        expected += p * distinct_colors(state)

    return round(expected, 9)

if __name__ == "__main__":
    print(p493())
