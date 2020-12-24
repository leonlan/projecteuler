sfrom collections import defaultdict
from sympy import factorint
from tqdm import tqdm


def n2factors(N):
    """Pre-computed number to prime factors table.
    Returns a dictionary with n-prime_factors_dict items.
    The prime_factors dictionary contains primes-multiplicity items.
    """
    n2f = dict()
    for i in range(N+1):
        n2f[i] = factorint(i)
    return n2f


def sigma(p, k, q):
    """Calculates S(pk) = 1 + p + p2 + . . . + pk = (p^(k+1) - 1) / (p-1)
    modulo q. Here Fermats Little Theorem is used to compute the
    multiplicative inverse."""
    flt = ((pow(p, k+1, q) - 1) * pow(p-1, q-2, q)) % q
    return flt


def compute_sum_of_divisors(factors, q):
    """Compute the sum of divisors mod q given a prime factorization."""
    prod = 1
    for p, mult in factors.items():
        prod = (prod * sigma(p, mult, q)) % q
    return prod


def p650(N, p):
    """Compute the sum of all divisors of B(n) mod p for n = 1, ..., N."""
    S = 0
    n2f = n2factors(N)
    for n in tqdm(range(1, N+1)):
        # Compute factors of B(N) using compact expression
        factors = defaultdict(int)
        k = n // 2
        j = (n+1) % 2  # 1 if even

        # Numerator
        for i in range(k):
            power = (2 * (k-i) - j)

            # Numerator elements
            for prime, mult in n2f[n-i].items():
                factors[prime] += mult * power

            # Denominator elements
            for prime, mult in n2f[i+1].items():
                factors[prime] -= mult * power

        # Compute D(N) given p2
        S = (S + compute_sum_of_divisors(factors, p)) % p

    return S


if __name__ == "__main__":
    print("Note: runs in about 3 minutes.")
    print(p650(20000, 10**9+7))
