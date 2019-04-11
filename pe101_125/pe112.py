"""
Problem 112: Bouncy numbers
https://projecteuler.net/problem=112

Solution:
"""
def pe112(P):
    """Find the least number for which the proportion of
    bouncy numbers is exactly P%."""
    def is_bouncy(n):
        s = str(n)
        D = False
        I = False
        for i in range(len(s)-1):
            if s[i] < s[i+1]:
                break
        else:
            D = True
        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                break
        else:
            I = True
        return(not(D or I))

    n = 100
    bouncy = 0
    while bouncy/n != P/100:
        n += 1
        bouncy += is_bouncy(n)
    return(n)


if __name__ == "__main__":
    print(pe112(99))
