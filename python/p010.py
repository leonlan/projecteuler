from sympy import sieve


def p010(n):
    """Finds the sum of all the primes below n."""
    return sum(sieve.primerange(2, n))


if __name__ == "__main__":
    print(p010(2*10**6))
