"""
Problem 346: Strong Repunits
https://projecteuler.net/problem=346

Solution:
Let n>0 be an integer. Then n is a repunit in base n-1 (verify this).
Next, n can be a repunit in some base b if:

b^0 + ... + b^k for k >= 2

This shows that we can simply iterate over all bases >= 2 for all
powers of k >= 2.
"""
def pe346(N):
    """Finds the sum of all strong rep units below N."""
    strong_repunits = set([1])
    for n in range(2, int(N**0.5)+1):
        total = 1 + n + n**2
        power = 2
        while total < N:
            strong_repunits.add(total)
            power += 1
            total += n**power
    return(sum(strong_repunits))


if __name__ == "__main__":
    print(pe346(10**12))
