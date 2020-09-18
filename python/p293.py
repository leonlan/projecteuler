from sympy import nextprime, primefactors
from math import prod


def test(N):
    """Brute-force test function."""

    def is_admissable(L):
        """Checks if the given prime factors make an admissable number."""
        a = L[0]
        for i, p in enumerate(L):
            if i == 0:
                if a != 2:
                    return False
            else:
                if p == nextprime(a):
                    a = p
                else:
                    return False
        return True


    # Throw error if input value is too large.
    if N > 100000:
        raise ValueError("N is too large. Try N < 100000.")

    # Check for admissable numbers
    admissable = set()
    for a in range(2, N):
        if is_admissable(primefactors(a)):
            admissable.add(a)

    # Compute the sum of all distinct pseudo-Fortunate numbers
    distinct_pf = set()
    for a in admissable:
        distinct_pf.add(pseudoFortunate(a))

    return sum(distinct_pf)



def pseudoFortunate(n):
    """Finds the pseudo-Fortunate number for n."""
    p = nextprime(n)
    M = p - n

    # Must be that M > 1
    if M == 1:
        M = nextprime(p) - n

    return M


def get_primes(N):
    """Get a list of consecutive primes whose product is less than N."""
    primes = []
    p = 2
    while prod(primes) < N:
        primes.append(p)
        p = nextprime(p)
    return primes


def powers_up_to(p, N):
    """A generator function that yields all powers of p up to N."""
    curr = p
    while curr < N:
        yield curr
        curr *= p


def p293(N):
    """Finds all pseudo-Fortunate numbers for admissable numbers less than N."""

    # Initialization
    admissable = set()
    prev = set()
    curr = set()
    primes = get_primes(N)

    for i, p in enumerate(primes):
        if i == 0:
            for n in powers_up_to(p, N):
                curr.add(n)
        else:
            for candidate in prev:
                for n in powers_up_to(p, N):
                    new_candidate = n * candidate
                    if new_candidate < N:
                        curr.add(new_candidate)

        admissable.update(curr)
        prev = curr
        curr = set()

    # Compute the sum of all distinct pseudo-Fortunate numbers
    distinct_pf = set()
    for a in admissable:
        distinct_pf.add(pseudoFortunate(a))

    return sum(distinct_pf)


if __name__ == "__main__":
    print(p293(10**9))
