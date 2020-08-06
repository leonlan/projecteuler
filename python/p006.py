def p006(n):
    """
    Finds the difference between the sum of squares of
    the first n natural numbers and the square of the sum.
    """
    sumsq = n * (n + 1) * (2 * n + 1) / 6
    sqsum = (n ** 2) * ((n + 1) ** 2) / 4
    return sqsum - sumsq


if __name__ == "__main__":
    print(p006(100))
