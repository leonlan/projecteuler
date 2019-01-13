"""
Problem 119: Digit power sum
https://projecteuler.net/problem=119

Solution:
Brute-force approach. I just took a very large number N and calculated
all the powers for every number up to the digit power sum of len(N)*9.
"""
def digit_sum(n):
    return(sum([int(c) for c in str(n)]))


def digit_power_sum(N, idx):
    upper_bound = int(len(N)*'9')
    seq = []
    for x in range(2, len(N)*9+1):
        n = 2
        D = x**n
        while D < N:
            if x == digit_sum(D):
                seq.append(D)
                print(x, n, D)
            n += 1
            D = x**n
    return(sorted(seq)[idx])


if __name__ == "__main__":
    print(digit_power_sum(99999999999999999))
