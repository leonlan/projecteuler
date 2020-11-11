from math import pow


def is_black(coord):
    """Checks if a given coordinate is black."""
    x, y = coord
    return pow(x-r, 2) + pow(y-r, 2) <= R


def new_coords(coord, position, N):
    """Compute the new coordinates given an initial coordinate
    and its position (Top Left, Top Right, Bottom Left or Bottom Right)."""
    x, y = coord
    D = (2**N)-1
    if position == 'TL':
        return [(x, y), (x+D, y), (x, y-D), (x+D, y-D)]
    elif position == 'TR':
        return [(x-D, y), (x, y), (x-D, y-D), (x, y-D)]
    elif position == 'BL':
        return [(x, y+D), (x+D, y+D), (x, y), (x+D, y)]
    elif position == 'BR':
        return [(x-D, y+D), (x, y+D), (x-D, y), (x, y)]


def same_color(coords, N):
    """Checks if the square (a, b, c, d) is of the same color."""
    return sum([is_black(x) for x in coords]) in [0, 4]


def encode(coords, N, K):
    """Recursive computation of the length of the encoding."""
    if same_color(coords, N) and K != N:
        return 2
    elif K == 1:
        return 9
    else:
        return (1 + encode(new_coords(coords[0], 'TL', K-1), N, K-1) +
                encode(new_coords(coords[1], 'TR', K-1), N, K-1) +
                encode(new_coords(coords[2], 'BL', K-1), N, K-1) +
                encode(new_coords(coords[3], 'BR', K-1), N, K-1))


def p287(N):
    """Find the minimal sequence describing D_N."""
    h = 2**N-1
    L = [(0, h), (h, h), (0, 0), (h, 0)]
    return encode(L, N, N)


if __name__ == "__main__":
    N = 24
    R = pow(2, 2*N-2)
    r = pow(2, N-1)
    print(p287(N))
