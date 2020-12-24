import numpy as np
from tqdm import tqdm


def p739(n, p):
    """Calculates f(n) [the summation of summations] mod p using the
    Lucas sequence."""
    total = 0

    # Create Lucas numbers
    lucas = np.zeros(n+3, dtype=np.int32)
    lucas[0], lucas[1] = (1, 3)
    for i in range(2, n+3):
        lucas[i] = (lucas[i-1] + lucas[i-2]) % p

    # Compute f(n) through iteratively computing Catalan numbers
    # using the recursive definition
    Cp = 1
    kp = 1
    Cm = 1
    km = 1
    for k in tqdm(range(n+2)):
        # Start computing the new Catalan numbers
        if k >= 1:
            Cp = (Cp * (n+k)) % p
            kp = (kp * pow(k, p-2, p)) % p
        if k >= 3:
            Cm = (Cm * (n+k)) % p
            km = (km * pow(k-2, p-2, p)) % p

        # Definition of Catalan numbers depending on k
        if k >= 2:
            C = (Cp * kp - Cm * km) % p
        else:
            C = (Cp * kp) % p
        total = (total + C * lucas[-(k+1)]) % p

    return total


if __name__ == "__main__":
    p = 10**9 + 7
    N = 10**8
    print("Note: this algorithm will take approx. 20 minutes to run.")
    print(p739(N-3, p))
