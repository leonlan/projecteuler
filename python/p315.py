from sympy import sieve

normal_costs = [6, 2, 5, 5, 4, 5, 6, 4, 7, 6]
reduced_costs = {
    0: {0: 0, 1: 4, 2: 3, 3: 3, 4: 4, 5: 3, 6: 2, 7: 2, 8: 1, 9: 2},
    1: {0: 4, 1: 0, 2: 5, 3: 3, 4: 2, 5: 5, 6: 6, 7: 2, 8: 5, 9: 4},
    2: {0: 3, 1: 5, 2: 0, 3: 2, 4: 5, 5: 4, 6: 3, 7: 5, 8: 2, 9: 3},
    3: {0: 3, 1: 3, 2: 2, 3: 0, 4: 3, 5: 2, 6: 3, 7: 3, 8: 2, 9: 1},
    4: {0: 4, 1: 2, 2: 5, 3: 3, 4: 0, 5: 3, 6: 4, 7: 2, 8: 3, 9: 2},
    5: {0: 3, 1: 5, 2: 4, 3: 2, 4: 3, 5: 0, 6: 1, 7: 3, 8: 2, 9: 1},
    6: {0: 2, 1: 6, 2: 3, 3: 3, 4: 4, 5: 1, 6: 0, 7: 4, 8: 1, 9: 2},
    7: {0: 2, 1: 2, 2: 5, 3: 3, 4: 2, 5: 3, 6: 4, 7: 0, 8: 3, 9: 2},
    8: {0: 1, 1: 5, 2: 2, 3: 2, 4: 3, 5: 2, 6: 1, 7: 3, 8: 0, 9: 1},
    9: {0: 2, 1: 4, 2: 3, 3: 1, 4: 2, 5: 1, 6: 2, 7: 2, 8: 1, 9: 0},
}


def digital_root_sequence(n):
    """Computes the digital root sequences for a number n. """

    def digital_root(n):
        """Computes the digital root of n."""
        return sum([int(d) for d in str(n)])

    l = [n]
    while n >= 10:
        n = digital_root(n)
        l.append(n)
    return l


def Sam(drs):
    """Calculates the number of transitions needed by Sam's clock
    for the digital root sequence of n."""
    total = 0
    for n in drs:
        for d in str(n):
            total += normal_costs[int(d)] * 2
    return total


def Max(drs):
    """Calculates the number of transitions needed by Max's clock
    for the digital root sequence of n."""
    total = 0
    for idx, n in enumerate(drs):
        if idx == 0:
            for d in str(n):
                # Add the initial turning on
                total += normal_costs[int(d)]
        else:
            # Calculate the transitions for each change of digit
            previous = str(drs[idx - 1])
            new = str(drs[idx])
            for i in range(1, len(previous) + 1):
                prev_digit = int(previous[-i])
                # For digits corresponding indices, there will be reduced
                # costs using Max's clock
                try:
                    new_digit = int(new[-i])
                    total += reduced_costs[prev_digit][new_digit]
                # For all other digits, use the
                # normal costs to calculate the transition cost (for turning off)
                except IndexError:
                    total += normal_costs[prev_digit]

    # Add the final turning off numbers
    for d in str(n):
        total += normal_costs[int(d)]
    return total


def p315(A, B):
    """Finds the difference between the total number needed by Sam's clock
    and that needed by Max's one for all prime numbers between A and B."""

    # Calculate the differences for each number
    total_diff = 0
    for p in sieve.primerange(A, B):
        drs = digital_root_sequence(p)
        total_diff += Sam(drs) - Max(drs)
    return total_diff


if __name__ == "__main__":
    print(p315(10 ** 7, 2 * 10 ** 7))
