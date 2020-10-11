from itertools import product
import numpy as np


def next_moves(x, y):
    """Calculates the possible next positions given current position x, y."""
    two_moves = {(0, 0): [(0, 1), (1, 0)],
                 (0, 29): [(0, 28), (1, 29)],
                 (29, 0): [(29, 1), (28, 0)],
                 (29, 29): [(28, 29), (29, 28)]}

    # 2-possible moves
    if (x, y) in two_moves.keys():
        return two_moves[(x, y)]

    # 3-possible moves
    elif x == 0:
        return [(x+1, y), (x, y+1), (x, y-1)]

    elif x == 29:
        return [(x-1, y), (x, y+1), (x, y-1)]

    elif y == 0:
        return [(x, y+1), (x+1, y), (x-1, y)]

    elif y == 29:
        return [(x, y-1), (x+1, y), (x-1, y)]

    # 4-possible moves
    else:
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]


def compute_position_distribution(x, y, t):
    """
    Compute the probability distribution of a flea that
    starts at position (x, y) after t rings of the bell.
    """
    current = np.zeros((30, 30))
    next = np.zeros((30, 30))
    current[x][y] = 1

    for _ in range(t):
        for x, y in product(range(30), range(30)):
            if current[x][y] > 0:
                moves = next_moves(x, y)
                p = 1/len(moves)
                for i, j in moves:
                    next[i][j] += p*current[x][y]
        current = np.copy(next)
        next = np.zeros((30, 30))

    return current


def p213():
    """
    Computes the expected number of unoccupied squares
    after 50 rings of the bell. Answer rounded to 6 decimal places.
    """
    unoccupied = np.ones((30, 30))
    for x, y in product(range(30), range(30)):
        flea_position = compute_position_distribution(x, y, 50)
        unoccupied *= 1 - flea_position

    total = np.round(np.sum(unoccupied), decimals=6)
    return total


if __name__ == "__main__":
    print(p213())
