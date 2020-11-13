from math import floor, pow


def f(x):
    return floor(pow(2, 30.403243784 - pow(x, 2))) * pow(10, -9)


def p197(iterations=100000):
    a = -1
    b = f(a)
    for i in range(iterations):
        a = b
        b = f(a)
    return round(a + b, 9)


if __name__ == "__main__":
    print(p197())
