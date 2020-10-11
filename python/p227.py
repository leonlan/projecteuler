from collections import defaultdict


def add(state, n, N):
    """Add n to the state according to the circularity of the game."""
    new_state = state + n
    if state + n < 0:
        new_state = -(state + n)
    elif state + n > N:
        new_state = 2*N - (state + n)
    return new_state


def next_states(state, N):
    """Returns a dictionary of the possible next states
    and its probability as key-value pairs.

    State definition: X(t) := Difference between player i and j at turn t

    """
    candidates = defaultdict(int)

    # Players moving into same direction & standing still
    candidates[state] += 2*1/6*1/6
    candidates[state] += 4/6*4/6

    # Players moving in opposite direction
    candidates[add(state, 2, N)] += 1/6*1/6
    candidates[add(state, -2, N)] += 1/6*1/6

    # 1 Player standing still, other moving
    candidates[add(state, 1, N)] += 2*4/6*1/6
    candidates[add(state, -1, N)] += 2*4/6*1/6

    return candidates



def p227(N, alpha=10):
    """Returns the expected number of turns a game lasts
    with a game of N players."""
    M = N//2
    expected = 0
    current, next = {M: 1}, defaultdict(int)

    for t in range(1, alpha+1):
        for curr_state, p in current.items():
            for next_state, q in next_states(curr_state, M).items():
                next[next_state] += p * q
        current = next
        next = defaultdict(int)
        if 0 in current:
            expected += t * current[0]
            del current[0]

    a = len(str(int(expected)))
    return int(expected) + round(expected % 1, 10-a)


if __name__ == "__main__":
    print(p227(100, 100000))
