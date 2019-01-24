"""
Problem 98: Anagramic squares
https://projecteuler.net/problem=98

Solution:
For every word length:
1. First we compute all anagramic word pairs from the given text file.
2. Then if there exists anagramic word pairs, we compute the anagramic number square pairs
3. Then for each anagramic word pair, we check if it coincides with an anagramic number pair
"""
import sys
sys.path.append("..")
from helperfunctions import prime_sieve
from math import ceil, floor, sqrt
from itertools import combinations


def find_anagramic_pairs(words):
    """Takes a list of words with fixed length and returns a list which contains
    all anagramic pairs as tuples."""
    anagramic_pairs = []
    prime_gen = prime_sieve(1000)
    primes = [next(prime_gen) for i in range(26)]

    # Calculate the prime factorization for each word.
    word_to_prime = []
    for word in words:
        prod = 1
        for c in word:
            prod *= primes[ord(c)-ord('A')]
        word_to_prime.append(prod)

    # Find the associated words for each prime factorization
    d = {}
    n = 0
    for prime_factor in word_to_prime:
        if prime_factor in d:
            d[prime_factor].append(words[n])
        else:
            d[prime_factor] = [words[n]]
        n += 1

    # Return all the anagramic pairs
    for k, v in d.items():
        if len(v) == 2:
            anagramic_pairs.append(v)
        # If we have a triple, quadruple, etc. then split it in doubles
        elif len(v) > 2:
            for x in combinations(v, 2):
                anagramic_pairs.append(x)
    return(anagramic_pairs)


def is_anagramic_square(word_pair, num_pair):
    word1, word2 = word_pair
    num1, num2 = num_pair
    for _ in range(2):
        letter_to_num = {}
        for i in range(len(word1)):
            letter = word1[i]
            digit = num1[i]
            # If the digit is different for the same letter, then stop
            if letter in letter_to_num and letter_to_num[letter] != digit:
                num2, num1 = num_pair
                break
            elif letter not in letter_to_num and digit in letter_to_num.values():
                num2, num1 = num_pair
                break
            else:
                letter_to_num[letter] = digit
        else:
            if num2 == "".join([letter_to_num[c] for c in word2]):
                return(True)
    return(False)


def anagramic_squares(words):
    """Returns the largest anagramic square in the list of words."""
    # First find the longest word in the word list to get an upper bound of n
    max_length = 0
    for word in words:
        max_length = max(len(word), max_length)

    # Compute the anagramic pairs and squares for every length n
    largest = 0
    for n in range(2, max_length+1):
        anagramic_words = find_anagramic_pairs([word for word in words if len(word) == n])
        if anagramic_words:
            anagramic_nums = find_anagramic_pairs([str(num**2)
                                                   for num in range(ceil(sqrt(10**(n-1))),
                                                                    floor(sqrt(10**n)))])
            for word in anagramic_words:
                for num in anagramic_nums:
                    if is_anagramic_square(word, num):
                        largest = max(largest, int(max(num)))
                        print(word, num, largest)
    return(largest)


if __name__ == "__main__":
    f = open("pe098.txt", "r").read().strip()
    all_words = [word.strip("\"") for word in f.split(",")]
    print(anagramic_squares(all_words))
