"""
Problem 117: Red, green and blue tiles
https://projecteuler.net/problem=117

Solution:
Define

mixed[n]: number of ways that a row measuring n units can be
filled with mixed RGB blocks.
"""
def pe117(N):
    """Returns the number of ways that a row of measuring N
    units can be filled with RGB blocks."""
    mixed = [0]*(N+1)
    for n in range(N+1):
        mixed[n] += mixed[n-1]
        if n < 2:
            mixed[n] = 1
        if n >= 2:
            mixed[n] += mixed[n-2]
        if n >= 3:
            mixed[n] += mixed[n-3]
        if n >= 4:
            mixed[n] += mixed[n-4]
    return(mixed[N])


if __name__ == "__main__":
    # Test case N = 5 should give 15
    print(pe117(5) == 15)
    print(pe117(50))
