"""
Problem 121: Disc game prize fund
https://projecteuler.net/problem=121

Solution:
Dynamic programming. Define

chance[n][m]: probability of picking m blue balls at turn n.

and find sum(chance[15][i] for i >= 8) in fractional form.
Then the maximum prize fund is the floor of the denom/num.
"""
import sys
sys.path.append("..")
from helperfunctions import gcd


def lcm(x, y):
    """Finds the largest common multiple of x and y."""
    lcm = (x*y)//gcd(x,y)
    return(lcm)


def mult(tup1, tup2):
    a, b = tup1
    c, d = tup2
    return((a*c, b*d))


def add(tup1, tup2):
    a, b = tup1
    c, d = tup2
    denom = lcm(b, d)
    num = a*(denom//b) + c*(denom//d)
    return((num, denom))


def disc_game_prize_fund(T):
    """Find the maximum prize fund that should be allocated to
    as single game in which T turns are played."""
    chance = [[(1,1)]*(i+1) for i in range(T+1)]
    n = 0
    for n in range(1, T+1):
        Pred = (n, n+1)
        Pblue = (1, n+1)
        for m in range(n+1):
            if m == 0:
                chance[n][m] = mult(chance[n-1][m], Pred)
            elif n == m:
                chance[n][m] = mult(chance[n-1][m-1], Pblue)
            else:
                chance[n][m] = add(mult(chance[n-1][m], Pred),
                                   mult(chance[n-1][m-1], Pblue))

    win = (0, 0)
    for i in range(T//2+1, T+1):
        if win == (0, 0):
            win = chance[T][i]
        else:
            win = add(win, chance[T][i])
    return(win[1]//win[0])


if __name__ == "__main__":
    # Test case T = 4 should give 10
    # print(disc_game_prize_fund(4))
    print(disc_game_prize_fund(15))
