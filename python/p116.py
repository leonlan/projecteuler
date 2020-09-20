"""
Problem 116: Red, green or blue tiles
"""
def p116(N):
    """Computes in how many different ways a grey row of size N
    can be covered with red/green/blue tiles."""
    R = [0]*(N+1)
    G = [0]*(N+1)
    B = [0]*(N+1)
    r, g, b = [2, 3, 4]  # Tile sizes

    for n in range(0, N+1):
        if n >= r:
            R[n] = 1 + R[n-1] + R[n-r]
        if n >= g:
            G[n] = 1 + G[n-1] + G[n-g]
        if n >= b:
            B[n] = 1 + B[n-1] + B[n-b]

    return R[N] + G[N] + B[N]


if __name__ == "__main__":
    print(p116(50))
