"""
Problem 74: Digit factorial chains
https://projecteuler.net/problem=74

Solution:
To reduce computations, we implement a cache (named chains) which
keeps track of known chain lengths.

Note that the program is not very well scalable for large N. It takes
about ~2 seconds to solve for N = 10^6, and about ~20 seconds for N = 10^7.
Since it is proven that every chain will get stuck in a loop eventually,
the solution is indeed average O(n) complexity.
"""
from math import factorial


def digit_factorial(n):
    """Returns the sum of all digits factorial in n."""
    return(sum([factorial(int(d)) for d in str(n)]))


def digit_factorial_chains(N, L):
    """Returns how many numbers 1 <= n < N have exactly a digit factorial
    chain of length L."""
    count = 0
    chains = {}
    for n in range(1, N):
        curr_chain = [n]
        curr_chain_count = 1
        num = n
        while True:
            # Check if the chain length of num is already known
            try:
                curr_chain_count += chains[num]-1
                if curr_chain_count == L:
                    count += 1
                break
            # Otherwise compute the next digit factorial
            except KeyError:
                num = digit_factorial(num)
                # Stop if there are repeating terms
                if num in curr_chain:
                    break
                else:
                    curr_chain_count += 1
                    curr_chain.append(num)

        # Store all numbers and their corresponding chain length
        for i in range(len(curr_chain)):
            chains[curr_chain[i]] = curr_chain_count-i
    return(count)


if __name__ == "__main__":
    print(digit_factorial_chains(10**6, 60))
