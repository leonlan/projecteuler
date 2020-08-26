from sympy import nextprime


def p007(n):
    """Finds the n-th prime number."""
    p = 0
    for i in range(n):
        p = nextprime(p)
    return p


if __name__ == "__main__":
    print(p007(10001))
