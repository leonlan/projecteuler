"""
Problem 95: Amicable chains
https://projecteuler.net/problem=95

Solution:
Similar to problem 92, we use a cache to store intermediate results. However,
this problem is not as straight-forward as the previous chain exercises.
- Calculate all proper divisors for n < 10**7
- ...
"""
import sys
sys.path.append("..")
from helperfunctions import properdivisors, prime_sieve


def amicable_chains(N):
    """Finds the smallest number of the longest amicable chain with no
    element exceeding N."""
    max_chain_length = 1
    longest_chain = []
    cache = {1: 0}

    # Calculate all the proper divisors for each number up to N
    amicable_dict = {}
    for i in range(2, N):
        amicable_dict[i] = sum(properdivisors(i))

    for key, value in amicable_dict.items():
        chain = []
        chain.append(key)
        head = value
        chain_length = 1
        while head in amicable_dict:
            if head in chain:
                # If the new head is the same as the starting key, then
                # it is an amicable chain. Store if it exceeds the max length.
                if chain.index(head) == 0 and chain_length > max_chain_length:
                    max_chain_length = chain_length
                    longest_chain = chain

                # If the new head is not the same, then there is a subchain
                # that is amicable.
                elif head in cache:
                    for elt in chain:
                        cache[elt] = chain_length

                cache[head] = chain_length
                break
            else:
                chain.append(head)
                chain_length += 1
                head = amicable_dict[head]
    return(longest_chain)


if __name__ == "__main__":
    min(amicable_chains(1000000))
