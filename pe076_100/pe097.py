"""
Problem 97: Large non-Mersenne prime
https://projecteuler.net/problem=97

Solution:
The last 10 digits of a number can be calculated by using module 10**10.
Moreover, (k mod 10) * (p mod 10) = (k*p) mod 10. Using this identity
we can easily reduce the exponential of 2.
"""
def large_non_mersenne_prime():
    """Computes the last 10 digits of the prime number 28433*2**7830457."""
    def mod(n):
        return(n % 10**10)
    rem = 28433
    powers = 7830457
    while powers > 34:
        powers -= 34
        rem = mod(2**34*rem)
    return(mod(rem*2**powers+1))


if __name__ == "__main__":
    print(large_non_mersenne_prime())
