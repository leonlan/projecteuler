"""
Problem 31: Coin sums
https://projecteuler.net/problem=31

Solution:
This is a case of dynamic programming
https://interactivepython.org/courselib/static/pythonds/Recursion/DynamicProgramming.html

"""
from collections import defaultdict


def coin_sums(N, coin_list):
    cache = {}
    for amount in range(1, N+1):
        ways = set()
        for coin in coin_list:
            if amount-coin == 0:
                ways.add((coin,))
            elif amount-coin > 0:
                for x in cache[amount-coin]:
                    ways.add(tuple(sorted(x + (coin,))))
            else:
                break
        cache[amount] = ways
    return(len(cache[200]))


if __name__ == "__main__":
    coin_list = [1, 2, 5, 10, 20, 50, 100, 200]
    print(coin_sums(200, coin_list))
