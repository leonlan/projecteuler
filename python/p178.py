from itertools import product
import numpy as np


def next_index_mapping():
    """
    Args:
    - N/A

    Returns:
    - mapper: A dictionary of key-value pairs where each key corresponds
    to an index and its value is another dictionary. This dictionary contains
    key-value pairs, where the key is the added digit and value is the
    new index.
    """
    # Get all binary strings in sorted manner
    binary_strings = [list(x) for x in list(product([0, 1], repeat=10))]

    # Define a helperfunction to find the "next" index
    def find_next(idx, i):
        """Finds the index of the newly computed binary strings."""
        s = binary_strings[idx].copy()
        s[i] = 1
        new_idx = binary_strings.index(s)
        return new_idx

    # Create a dictionary that maps each index to its next index (based on new digit)
    mapper = {}
    for idx in range(len(binary_strings)):
        mapper[idx] = {i: find_next(idx, i) for i in range(10)}

    return mapper


def p178(N):
    """Calculates the number of step numbers up to (and including) N digits."""
    # Use a pre-computed mapper dictionary to find next indices
    mapper = next_index_mapping()

    def f(idx, d):
        """Finds the new index"""
        return mapper[idx][d]

    # Initialize cache
    D = np.zeros((N + 1, 10 + 1, 1024 + 1))

    # Dynamic programming scheme
    for n in range(1, N + 1):
        for l in range(10):
            for i in range(1024):
                if n == 1:
                    # 1-digit numbers should correspond to their binary string
                    # with the exception of 0
                    if i == 0 and l != 0:
                        D[n][l][f(i, l)] += 1
                    else:
                        pass
                else:
                    if l == 0:
                        D[n][l + 1][f(i, l + 1)] += D[n - 1][l][i]
                    elif l == 9:
                        D[n][l - 1][f(i, l - 1)] += D[n - 1][l][i]
                    else:
                        D[n][l + 1][f(i, l + 1)] += D[n - 1][l][i]
                        D[n][l - 1][f(i, l - 1)] += D[n - 1][l][i]

    # Get the total count of numbers with idx 1023 (i.e. pandigital)
    total = 0
    for n in range(N + 1):
        for l in range(10):
            total += D[n][l][1023]
    return total


if __name__ == "__main__":
    # assert(p178(10)==1)
    print(p178(40))
