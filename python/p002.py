def p002(N):
    """Finds the the value of all even-valued Fibonnaci terms whose
    values does not exceed N."""
    total = 0
    F = [1, 1]
    i = 2
    while F[-1] <= N:
        # Make the new F[i] term
        F.append(F[i-2] + F[i-1])

        # Sum each even numbers
        if F[i] % 2 == 0:
            total += F[i]
        i += 1

    return total


if __name__ == "__main__":
    print(p002(4*10**6))
