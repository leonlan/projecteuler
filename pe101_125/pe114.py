"""
Problem 114: Counting block combinations I
https://projecteuler.net/problem=114

Solution:
Define

ways[n]: the number of ways that a row measuring n units
can be filled in length with blocks.
"""
def counting_block_combinations_I(N):
    """Returns the number of ways that a row measuring N units
    can be filled in length."""
    ways = [0]*(N+1)
    for n in range(N+1):
        if n < 3:
            ways[n] = 1
        else:
            ways[n] += ways[n-1]
            for m in range(3, n+1):
                k = max(n - (m+1), 0)
                ways[n] += ways[k]
    return(ways[N])


if __name__ == "__main__":
    # Test case N = 7 should return 17
    print(counting_block_combinations_I(7) == 17)
    print(counting_block_combinations_I(50))
