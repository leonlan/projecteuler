def p001(N):
    """Finds the sum of all the multiples of 3 or 5 below N"""
    total = 0

    # Finds multiples of 3
    for i in range(3, N, 3):
        total += i

    # Finds multiples of 5
    for i in range(5, N, 5):
        # Multiples of 3 and 5 should only be counted once
        if i % 3 != 0:
            total += i

    return total


if __name__ == "__main__":
    print(p001(1000))
