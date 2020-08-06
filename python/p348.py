from math import sqrt


def palindrome_number_generator():
    yield 0
    lower = 1
    while True:
        higher = lower*10
        for i in range(lower, higher):
            s = str(i)
            yield int(s+s[-2::-1])
        for i in range(lower, higher):
            s = str(i)
            yield int(s+s[::-1])
        lower = higher


def is_perfect_square(n):
    """Checks if n is a perfect square."""
    return (sqrt(n) - int(sqrt(n))) == 0


def is_4_square_cube_sum(n):
    """Checks if n can be expressed as the sum of a square and a cube
    in exactly four different ways."""
    total = 0
    for cube in range(1, int(n**(1/3))+1):
        remainder = n - cube**3
        if is_perfect_square(remainder):
            total += 1
            if total > 4:
                return False
    return total == 4


def p348():
    """Finds the sum of the five smallest palindromic numbers
    that can be expressed in exactly 4 different square-cube sum ways."""
    candidate = []
    for p in palindrome_number_generator():
        if is_4_square_cube_sum(p):
            candidate.append(p)
            if len(candidate) == 5:
                return sum(candidate)


if __name__ == "__main__":
    print(p348())
