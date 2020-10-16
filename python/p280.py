from collections import defaultdict
import time


def next_moves(x, y, N):
    """Calculates the possible next positions given current position x, y
    in a (N+1) by (N+1) grid. Also returns the probability."""
    two_moves = {(0, 0): [(0, 1), (1, 0)],
                 (0, N): [(0, N-1), (1, N)],
                 (N, 0): [(N, 1), (N-1, 0)],
                 (N, N): [(N-1, N), (N, N-1)]}

    # 2-possible moves
    if (x, y) in two_moves.keys():
        return two_moves[(x, y)]

    # 3-possible moves
    elif x == 0:
        return [(x+1, y), (x, y+1), (x, y-1)]

    elif x == N:
        return [(x-1, y), (x, y+1), (x, y-1)]

    elif y == 0:
        return [(x, y+1), (x+1, y), (x-1, y)]

    elif y == N:
        return [(x, y-1), (x+1, y), (x-1, y)]

    # 4-possible moves
    else:
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]


def next_states(state):
    """Returns a dictionary of the possible next states
    and its probabiliy as key-value pairs.abs

    State definition: X(t) := Position (i, j) with upper row and lower row
    defined as binary strings to indicate where a seed lies and 0/1 variable
    to denote holding state

    Example of state:
    - Starting state: (2, 2, 11111, 00000, 0)
    - Picked up seed at (4, 4): (4, 4, 11110, 00000, 1)
    - Dropped off seed at (4, 0): (4, 0, 11110, 00001, 0)

    """
    candidates = defaultdict(int)
    i, j, lower, upper, carrying = state
    for x, y in next_moves(i, j, 4):
        q = 1/len(next_moves(i, j, 4))
        if carrying == 1 and y == 4 and upper[x] == 0:
            new_upper = list(upper)
            new_upper[x] = 1
            new_state = (x, y, lower, tuple(new_upper), 0)
        elif carrying == 0 and y == 0 and lower[x] == 1:
            new_lower = list(lower)
            new_lower[x] = 0
            new_state = (x, y, tuple(new_lower), upper, 1)
        else:
            new_state = (x, y, lower, upper, carrying)
        candidates[new_state] = q
    return candidates


def p280(alpha=10000):
    """Calculates the expected number of steps until all seeds have been
    droped in the top row in a 5x5 grid. Answer rounded to 6 decimal places."""
    expected = 0
    current, next = {(2, 2, (1,1,1,1,1), (0,0,0,0,0), 0): 1}, defaultdict(int)

    for t in range(1, alpha+1):
        for curr_state, p in current.items():
            for next_state, q in next_states(curr_state).items():
                if next_state[3] == (1,1,1,1,1):
                    expected += t * p * q
                else:
                    next[next_state] += p * q
        current = next
        next = defaultdict(int)

    return round(expected, 6)


if __name__ == "__main__":
    print(p280(3000))
