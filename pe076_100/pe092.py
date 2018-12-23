"""
Problem 92: Square digit chains
https://projecteuler.net/problem=92

Solution:
Similar to problem 74, use a cache to store intermediate results.
Using dictionay lookup in constant time, many excess computations can
be avoided.

Possible improvement: we can find an upper bound to reduce the number
of times that we need to store the numbers. The upper bound is
# digits * 9^2. In this case, since we consider at most 7 digit numbers,
we have 7*81 = 567 as upper bound.

"""


def square_digit(n):
    """Returns the sum of the digits squared."""
    return(sum([int(d)**2 for d in str(n)]))


def square_digit_chains(N):
    """Returns the number of integers below N that arrive at 89."""
    count = 0
    chains = {1: 1, 89: 89}  # Cache

    for n in range(1, N):
        curr_chain = [n]
        num = n
        while True:
            # Check if the num is in the cache
            try:
                if chains[num] == 89:
                    count += 1

                # Store the numbers in the chain since we know the values
                if n <= 567:
                    for i in range(len(curr_chain)):
                        chains[curr_chain[i]] = chains[num]
                break

            # Otherwise continue looping
            except KeyError:
                num = square_digit(num)
                curr_chain.append(num)
    return(count)


if __name__ == "__main__":
    print(square_digit_chains(10**7))
