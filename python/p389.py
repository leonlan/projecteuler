from collections import defaultdict
import numpy as np


def compute_mean(X):
    """Computes the mean given the probability mass function."""
    mu = 0
    for x, p in X.items():
        mu += x*p
    return mu


def compute_variance(X):
    """Computes the variance given the probability mass function."""
    mu = compute_mean(X)
    var = 0
    for x, p in X.items():
        var += p*(x-mu)**2
    return var


def p389():
    """Computes the variance of I in 4 decimals."""
    T = defaultdict(int, {1: 0.25, 2: 0.25, 3: 0.25, 4: 0.25})
    C, O, D, I = (defaultdict(int) for i in range(4))
    die_size = [6, 8, 12, 20]
    rvs = [T, C, O, D, I]

    # Compute the pmf of the Uniform distirbutions
    for i, X in enumerate(rvs[:-1]):
        Xmax = max(X.keys())
        D = die_size[i]
        U = np.zeros((Xmax + 1, D*Xmax + 1))
        for n in range(1, Xmax + 1):
            print(i, n, Xmax)
            for x in range(1, D*n + 1):
                if n == 1:
                    U[n][x] = 1/D
                else:
                    for d in range(1, D+1):
                        U[n][x] += U[n-1][x-d]*(1/D)

        # Compute the pmf of the next random variable
        Y = rvs[i+1]
        for x in range(1, Xmax*D+1):
            for t in range(1, Xmax+1):
                Y[x] += U[t][x] * X[t]

    var = compute_variance(I)
    return np.round(var, 4)


if __name__ == "__main__":
    print(p389())
