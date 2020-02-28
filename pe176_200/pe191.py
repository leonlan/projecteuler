"""
Problem 191: Prize Strings
https://projecteuler.net/problem=191

Solution:
Dynamic programming with 3 variables. Define

ways[n][a][l] := the number of prize strings of length n
with the last a letters as Absent days and l late days total.
"""
import numpy as np


def pe191(d):
    """Finds the number of prize strings over a period of d days.""" 
    p = np.zeros((d+1, 3, 2), dtype="int32")
    for n in range(1, d+1):
        for a in range(0, 3):
            for l in range(0, 2):
                if a + l > n:
                    p[n][a][l] = 0
                elif n == 1:
                    p[n][l][a] = 1
                else:
                    if a > 0:
                        # Add A (1x)
                        p[n][a][l] = p[n-1][a-1][l]
                    else:
                        if l == 0:
                            # Add O (3x)
                            p[n][a][l] = (p[n-1][0][l] + p[n-1][1][l] + p[n-1][2][l])
                        else:
                            # Add O (3x) or add L (3x)
                            p[n][a][l] = (p[n-1][0][l] + p[n-1][1][l] + p[n-1][2][l]+
                                p[n-1][0][l-1] + p[n-1][1][l-1] + p[n-1][2][l-1])
    return(sum([p[d][x][y] for x in range(3) for y in range(2)]))


if __name__ == "__main__":
    print(pe191(30))
