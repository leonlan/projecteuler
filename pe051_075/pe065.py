"""
Problem 65: Convergents of e
https://projecteuler.net/problem=65

Solution:
Start with the last number in the continued fraction and work your way up.
"""


def continued_fraction_e(n):
    """Returns the array of the continued fraction of e."""
    seq = [1, 2]
    i = 2
    k = 2
    while i < n:
        if (i-1) % 3 == 0:
            k += 2
            seq.append(k)
        else:
            seq.append(1)
        i += 1
    return(seq)


def convergents_of_e(n):
    """Finds the sum of digits in the numerator of the nth convergent
    of the continued fraction of e."""
    seq = continued_fraction_e(n-1)
    N = len(seq) - 1
    frac = [1, seq[N]]
    for i in range(N, 0, -1):
        frac[0] += seq[i-1]*frac[1]
        frac = frac[::-1] # 1 divide by fraction <=> reverse fraction
    frac[0] += 2*frac[1]
    return(sum([int(d) for d in str(frac[0])]))


if __name__ == "__main__":
    print(convergents_of_e(100))
