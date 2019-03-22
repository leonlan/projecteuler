"""
Problem 72: Counting fractions
https://projecteuler.net/problem=72

Solution:
The number of reduced proper fractions for d <= D is equal to
the sum of all phi(d) for 2 <= d <= D. Totient sieve function
is copied from problem 70.
"""
def totient_sieve(N):
    N = N+1
    totients = [1]*(N)
    for p in range(2, N):
        # Sieve for each prime number p
        if totients[p] == 1:
            powers = set()
            k = 2

            # Calculate each power of the prime number
            while p**k < N:
                powers.add(p**k)
                k += 1

            # Multiply with phi(p) = p-1 for every number divisible by p
            for i in range(p, N, p):
                totients[i] *= p-1

            # Multiply with p to count for multiplicity
            for power in powers:
                for j in range(power, N, power):
                    totients[j] *= p
    return(totients[2:])


def counting_fractions(D):
    """Returns the number of elements contained in the set of reduced
    proper fractions for d <= D."""
    return(sum(totient_sieve(D)))


if __name__ == "__main__":
    print(counting_fractions(10**6))
