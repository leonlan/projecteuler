def Fibonacci(n):
    """Computes all Fibonacci numbers up to n (not including).
    Starts at 1, 2, etc."""
    L = []
    a, b = 1, 2
    while a < n:
        L.append(a)
        a, b = b, a + b
    return L


def p297(N):
    """Computes the sum of z(n) for all n = 1, ..., N-1."""
    # Compute all candidate fibonacci numbers
    F = Fibonacci(N)

    # Precompute values for S(n)
    S = {1: 1, 2: 2, 3: 3}
    for i, f in enumerate(F):
        if f not in S:
            S[F[i]] = (F[i] - F[i-1] - 1) + S[F[i-1]] + S[F[i-2]]

    # Define a function that does recursive computations of S(n)
    # Based on the recurrence relation below.
    def compute_S(n):
        """
        Calculates S(n) according to the rule
        n = maximal_f + rem
        S[n] = S[maximal_f] + compute_S(rem) + n - maximal_f

        where S[n] is the dictionary of all S values.

        If n is Fibonacci, the function reduces to a dictionary look up in S,
        that is, compute_S(n) returns S[n]
        """
        if n in F:
            return S[n]

        else:
            maximal_f = 1
            for f in F:
                if f <= n:
                    maximal_f = max(maximal_f, f)
            rem = n - maximal_f
            return S[maximal_f] + compute_S(rem) + n - maximal_f

    return(compute_S(N-1))


if __name__ == "__main__":
    print(p297(10**17))
