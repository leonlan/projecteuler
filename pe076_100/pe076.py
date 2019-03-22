"""
Problem 76: Counting summations
https://projecteuler.net/problem=76

Solution:
Dynamic programming. I first struggled with overlap between
number counts, but after a while I figured to keep track of
ways[n][m] with m < n, which is the number of ways that n can
be written as a sum of integers smaller or equal to m.
"""
def counting_summations(N):
    """Computes in how many different ways N can be written as a summation
    of positive integers."""
    ways = [[0]*(i+1) for i in range(N+1)]
    for n in range(1, N+1):
        for m in range(1, n+1):
            if m == 1:
                ways[n][m] = 1
            elif m == n:
                ways[n][m] = ways[n][m-1] + 1
            else:
                ways[n][m] = ways[n-m][min(m, n-m)] + ways[n][m-1]
    return(ways[N][N-1])


if __name__ == "__main__":
    print(counting_summations(100))
