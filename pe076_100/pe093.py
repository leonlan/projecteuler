'''
Problem 93: Arithmetic expressions
https://projecteuler.net/problem=93

Comment: I might be calculating redundant expressions.
'''
from itertools import combinations, permutations


def pos_and_int(n):
    return(n >= 0 and int(n) == n)


def arith2(a, b):
    def safe_div(x, y):
        if y == 0:
            return 0
        return(x / y)
    return(set([a+b, b-a, a-b, safe_div(a, b), safe_div(b, a), a*b]))


def arith3(a, b, c):
    targetnums = []
    abc = list(permutations([a, b, c], 3))
    for triple in abc:
        x, y, z = triple
        for n in arith2(x, y):
            targetnums.extend(arith2(n, z))
    return(set(targetnums))


def arith4(a, b, c, d):
    """Calculates all possible target numbers with a, b, c and d."""
    targetnums = []
    abcd = list(permutations([a, b, c, d], 4))
    for quadruple in abcd:
        w, x, y, z = quadruple

        # (a+b+c)+d
        for n in arith3(w, x, y):
            targetnums.extend(arith2(n, z))

        # a+(b+c)+d
        for i in arith2(x, y):
            for j in arith2(w, i):
                targetnums.extend(arith2(j, z))

        # a+b+(c+d)
        for i in arith2(y, z):
            for j in arith2(x, i):
                targetnums.extend(arith2(w, j))

        # (a+b)+(c+d)
        for i in arith2(w, z):
            for j in arith2(x, y):
                targetnums.extend(arith2(i, j))

        # a+b+c+d
        for i in arith2(w, x):
            for j in arith2(i, y):
                targetnums.extend(arith2(j, z))
    return(set(filter(pos_and_int, targetnums)))


def consecutive(li):
    n = 0
    while True:
        n += 1
        if n not in li:
            break
    return(n)


def arithmetic_expression(n):
    result = ''
    max_consec = 0
    for abcd in list(combinations(range(1, n), 4)):
        a, b, c, d = abcd
        new = consecutive(arith4(a, b, c, d))
        if new > max_consec:
            max_consec = new
            result = str(a)+str(b)+str(c)+str(d)
    return(result)


if __name__ == "__main__":
    print(arithmetic_expression(10))
