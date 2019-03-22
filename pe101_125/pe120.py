"""
Problem 120: Square remainders
https://projecteuler.net/problem=120

Solution:
(a-1)^n + (a+1)^n == r mod a^2

Using WolframAlpha there is a pattern if we expand for n:
n = 0 => 2 mod a^2
n = 1 => 2a mod a^2
n = 2 => 2 mod a^2
n = 3 => 6a mod a^2
n = 4 => 2 mod a^2
n = 5 => 10a mod a^2
n = 6 => 2 mod a^2
n = 7 => 14a mod a^2
etc.

So for n uneven we have
r = 2*n*a mod a^2.

This means that r is maximized if 2*n*a == a^2-i, where i > 0 is
as minimum as possible. So we check if there is some integer n
s.t.

n == (a^2 - 1)/(2a),
n == (a^2 - 2)/(2a),
n == (a^2 - 3)/(2a),
etc.

"""
def square_remainders(A):
    """Returns \sum(r_max) for 3 <= a <= A."""
    def is_int(n):
        """Checks if n is integer."""
        return(int(n) == n)

    sumrmax = 0
    for a in range(3, A+1):
        i = 1
        n = (a**2-i)/(2*a)
        while not is_int(n):
            i += 1
            n = (a**2-i)/(2*a)
        sumrmax += a**2-i
    return(sumrmax)


if __name__ == "__main__":
    print(square_remainders(1000))
