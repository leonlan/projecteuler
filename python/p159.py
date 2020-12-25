from sympy import factorint
from itertools import combinations
from collections import defaultdict


def compute_all_dr(N):
    """Compute the digital roots of all numbers below N."""
    def add_digits(n):
        """Adds the digits of a number n."""
        return sum([int(d) for d in str(n)])

    DR = dict()
    for i in range(N):
        x = i
        while int(x) > 9:
            x = add_digits(x)
            if x in DR:
                x = DR[x]
                break
        DR[i] = x

    return DR


def find_pairs(factors):
    """Given a dictionary of factors, find all possible pairs of factors
    that can be multiplied."""
    singles = list(combinations([f for f, v in factors.items() if v >= 1], 2))
    # If factor f has multiplicity over 1, then (f, f) is also a pair
    doubles = [(f, f) for f, v in factors.items() if v >= 2]
    return singles + doubles


def p159(N):
    """Computes the sum of MDRS from n = 2, ..., N-1."""
    DR = compute_all_dr(10**6)

    def DRS(factors):
        """Computes the DRS given a dictionary factorization."""
        return sum([DR[n] * power for n, power in factors.items()])

    def compute_MDRS(n):
        """Computes the MDRS from a number n using greedy local search."""
        candidates = []  # Candidates with local optimal DRS

        def improve(factors):
            """Recursively multiply two factors as long as it
            does not decrease the digital root sum of the factors."""
            factors = defaultdict(int, factors)
            improvement = 0
            for a, b in find_pairs(factors):
                c = a*b
                # If local improvement is possible, create remove the two
                # old factors once and introduce a new one
                if DR[c] >= DR[a] + DR[b]:
                    new_factors = factors.copy()
                    new_factors[a] -= 1
                    new_factors[b] -= 1
                    new_factors[c] += 1
                    improvement += 1
                    improve(new_factors)

            # If no more local improvements are possible then add
            # to the pool of local optima as candidates for MDRS
            if not improvement:
                candidates.append(factors)

        # Compute the potential candidates
        improve(factorint(n))
        return max([DRS(f) for f in candidates])

    # Loop over all numbers.
    total = 0
    for n in range(2, N):
        total += compute_MDRS(n)
    return total


if __name__ == "__main__":
    print("Runnig time is approx. 1:30 minutes.")
    print(p159(10**6))
