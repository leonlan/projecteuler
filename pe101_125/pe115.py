"""
Problem 115: Counting block combinations II
https://projecteuler.net/problem=115

Solution:

"""
def counting_block_combinations_II(M, target):
    """Returns the first n such that F(m, n) exceeds target."""
    ways = [0]
    n = 0
    while ways[n] < target:
        n += 1
        ways += [0]
        if n < M:
            ways[n] = 1
        else:
            ways[n] += ways[n-1]
            for m in range(M, n+1):
                k = max(n - (m+1), 0)
                ways[n] += ways[k]
    return(n-2)


if __name__ == "__main__":
    # Test case M = 3, target = 10**6 should return n = 30
    print(counting_block_combinations_II(3, 10**6) == 30)
    # Test case M = 10, target = 10**6 should return n = 57
    print(counting_block_combinations_II(10, 10**6) == 57)
    print(counting_block_combinations_II(50, 10**6))
