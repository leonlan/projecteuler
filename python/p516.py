from sympy import isprime
from math import log


def compute_valid_primes(N):
    """Returns all primes s.t. p-1 is Hamming. Log is used to determine
    an upper bound for the respective powers."""
    valid = []
    for i in range(int(log(N, 2)+1)):
        for j in range(int(log(N, 3)+1)):
            for k in range(int(log(N, 5)+1)):
                p = 2**i*3**j*5**k + 1
                if p <= N and isprime(p):
                    valid.append(p)
    return sorted(valid, reverse=True)


def p516(N):
    """Compute the sum of numbers n <= N such that phi(n) is Hamming."""
    total = 1
    P = compute_valid_primes(N)
    max_idx = len(P)

    def recursion(i, partial_sum, M):
        """Compute all possible numbers n % M such that phi(n) is Hamming."""
        nonlocal total  # Needed to reference the total variable

        # Stop once we have iterated over all valid primes in P
        if i == max_idx:
            pass

        else:
            power = 0
            x = partial_sum * P[i]**power
            while x <= N:
                # If power was nonzero, a unique new partial sum is obtained
                if power != 0:
                    total = (total + x) % M

                # Move to the next recursion step in which we multiply with
                # prime i^power
                recursion(i+1, x, M)

                # Add power and construct new unique prime factorization
                power += 1
                x = partial_sum * P[i]**power

                # Stop recursing the current prime has power larger than 1
                if P[i] not in [2, 3, 5] and power >= 2:
                    break

    # Start recursion
    recursion(0, 1, 2**32)

    return total


if __name__ == "__main__":
    print(p516(10**12))
