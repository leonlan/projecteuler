"""
Problem 215: Crack-free Walls
https://projecteuler.net/problem=215

Solution:
(Taken from the PE forum)
* calculate the 3329 possible row arrangements of size 2 and size 3 bricks recursively
* for each row, determine where the cracks are by cumulative summing of the brick sizes
* for each row, determine which other rows can follow it, depending on crack locations
* calculate the number of possible wall configurations by a memoized recursive function which tells you how much configurations there are if you still need r rows and the previous row is given

"""
import numpy as np
from sympy.utilities.iterables import multiset_permutations
from math import factorial as f


def pe215(N, K):
    xypairs = []
    x = 0
    while N-(x*3) >= 0:
        if (N-(x*3)) % 2 == 0:
            y = (N-(x*3))//2
            xypairs.append((x, y))
        x += 1


    # Preprocessing: number of possible walls
    total = 0
    for (x, y) in xypairs:
        total += f(x+y)//(f(x)*f(y))
    walls = np.zeros([total, N+1])


    # Calculate each type of wall
    n = 0
    for xy in xypairs:
        x, y = xy
        for wall in multiset_permutations(x*'3'+y*'2'):
            wall_length = 0
            for brick in wall:
                wall_length += int(brick)
                walls[n][wall_length] = 1
            n += 1


    # Calculates for every wall how many walls its compatible with
    compatible = []
    for n in range(len(walls)):
        friends = []
        wall1 = walls[n]
        for m in range(len(walls)):
            wall2 = walls[m]
            if all(wall1[:-1]+wall2[:-1] < 2):
                friends.append(m)
        compatible.append(friends)


    # Calculate the number of compatible k-walls
    crackfree = np.zeros([K, total])
    crackfree[0] += 1
    for k in range(1, K):
        for n in range(len(walls)):
            wall1 = walls[n]
            count = 0
            for m in compatible[n]:
                wall2 = walls[m]
                # Make sure that wall cracks do not overlap and exclude
                # last element of the wall
                if all(wall1[:-1]+wall2[:-1] < 2):
                    count += crackfree[k-1][m]
            crackfree[k][n] = count
    return(sum(crackfree[-1]))


if __name__ == "__main__":
    print(pe215(32, 10))
