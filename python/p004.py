def is_palindrome(n):
    """Checks if n is a palindromic number."""
    s = str(n)
    return s == s[::-1]


def p004(N):
    """Finds the largest palindrome made from the product
    of two N-digit numbers."""
    Ndigits = list(range(10**N-1, 10**(N-1), -1))
    max_palindrome = 0
    for i in Ndigits:
        for j in Ndigits:
            if is_palindrome(i*j):
                max_palindrome = max(max_palindrome, i*j)
    return max_palindrome


if __name__ == "__main__":
    print(p004(3))
