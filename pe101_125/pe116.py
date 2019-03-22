"""
Problem 116: Red, green or blue tiles

Solution:
Let R/G/B way[n] be the number of ways that a grey row of size n
can be placed with R/G/B tiles, where |R| = 2, |G| = 3, |B| = 5.
"""
def pe116(N):
    """Computes in how many different ways a grey row of size N
    can be covered with R/G/B tiles."""
    Rway = [0]*(N+1)
    Gway = [0]*(N+1)
    Bway = [0]*(N+1)
    R, G, B = [2, 3, 4]
    for n in range(R, N+1):
        Rway[n] = 1 + Rway[n-1] + Rway[n-R]
        if n >= G:
            Gway[n] = 1 + Gway[n-1] + Gway[n-G]
        if n >= B:
            Bway[n] = 1 + Bway[n-1] + Bway[n-B]
    return(Rway[N] + Gway[N] + Bway[N])


if __name__ == "__main__":
    print(pe116(50))
