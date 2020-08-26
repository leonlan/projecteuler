import numpy as np


def p008(L, n):
    """Finds the n adjacent digits in the series L with the greatest product."""
    max_prod = 0
    numlength = n
    serieslength = len(L)
    i = 0
    while i < (serieslength - numlength + 1):
        num = L[i:i+numlength]
        # If there is a zero in the number, move to the index after the zero
        if 0 in num:
            i += max(np.where(num==0)[0]) + 1
        # Else calculate the product of the digits in the number
        else:
            new_prod = np.multiply.reduce(num)
            max_prod = max(max_prod, new_prod)
            i += 1
    return max_prod


if __name__ == "__main__":
    L = open("../../data/p008.txt", "r").readlines()
    series = np.array([int(x) for x in ''.join(line.strip() for line in L)], dtype='int64')
    print("The largest product of four adjacent digits are:",
        p008(series, 4))
    print("The largest product of thirteen adjacent digits are:",
        p008(series, 13))
