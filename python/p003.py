from euler import isprime


def p003(N):
    """Finds all prime factors of N."""
    largest = 0

    for i in range(2, int(N**0.5+1)):
        # Divide N by its prime factors
        while N % i == 0:
            N /= i
            largest = i

        # Stop loop if N is factored-out
        if N == 1:
            break

    return largest


if __name__ == "__main__":
    print(p003(600851475143))
