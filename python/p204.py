from math import ceil
from sympy import sieve


def powers_up_to(p, N):
    """A generator function that yields all powers of p up to N."""
    curr = p
    while curr < N:
        yield curr
        curr *= p


def p204(N, k):
    """Finds the number of generalised Hamming numbers of type k up to N."""

    # Initialization
    primes = sieve.primerange(2, k + 1)
    prev = set()
    curr = set([1])

    for i, p in enumerate(primes):
        # Compute all powers of p up to N
        for new in powers_up_to(p, N):
            curr.add(new)
            # print(p, new)

        # Use the previous type Hamming numbers to compute the current ones
        if i > 0:
            for nums in prev:
                for new in powers_up_to(p, ceil(N/nums)+1):
                    curr.add(new*nums)


        prev = curr.copy()
        # print(sorted(list(curr)))

    # Return the number of Hamming numbers
    # Correct the length for the incorrectness of powers_up_to function
    total = 0
    for p in prev:
        if p <= N:
            total += 1

    return total


if __name__ == "__main__":
    # print(p204(10**8, 5) == 1105) # Test case
    print(p204(10**9, 100))
