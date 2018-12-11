"""
Problem 59: XOR decryption
https://projecteuler.net/problem=59

Solution:
This program tries to decrypt the cyphertext using every possible
3-lowercase letter key combination. It then checks whether there are
enough English words, after which can be manually verified whether
the key is correct. 

(Simply run the code in an Python interpreter.)

"""

from itertools import product
from pathlib import Path


# Top 1000 words in English dictionary
data_folder = Path("../resources")
en_dict = open(data_folder / "top1000words.txt", "r").read().splitlines()


# All possible key combinations
x = range(ord('a'), ord('z') + 1)
keys = product(x, x, x)


# List of all cyphertext values
cyphertext = [int(c) for c in  open('pe59.txt', 'r').read().rsplit(',')]
cypherslice = cyphertext[:100]


# Crack the code
def decrypt(key, cypher):
    """Applies a key cyclically to a cypertext."""
    text = ''
    for i in range(len(cypher)):
        text += chr(cypher[i] ^ key[i%3])
    return(text)


def words_in_wordlist(s, wordlist):
    """Returns all words in a string s that are also in a wordlist"""
    return([word for word in s.split(' ') if word in wordlist])

def find_key(keys):
    """Finds the correct key among all possible key combinations
    if the decrypted text contains enough English words."""
    for key in keys:
        decrypted = decrypt(key, cypherslice)
        english_words = words_in_wordlist(decrypted, en_dict)
        # Checks if the decrypted text contains 6 or more common English words
        if len(english_words) > 5:
            return(key) # [103, 111, 100]


# Convert the text to ASCII values
def str_to_num(s):
    sum = 0
    for c in s:
        sum += ord(c)
    return(sum)


if __name__ == "__main__":
    print("The total word score of this file is:",
        str_to_num(decrypt(find_key(keys), cyphertext)))
