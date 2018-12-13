"""
Problem 42: Coded triangle numbers
https://projecteuler.net/problem=42

Solution:
Compute all only the triangle numbers up to the maximum score
of the given names.
"""


def word_score(s):
    return(sum([(ord(c) - ord('A') + 1) for c in s]))


def coded_triangle_num(words):
    """Returns the number of triangle words in a list of words."""
    scores = list(map(word_score, words))
    trianglenums = []
    trianglenum = 0
    n = 1
    while trianglenum < max(scores):
        trianglenum = n*(n+1)//2
        trianglenums.append(trianglenum)
        n += 1
    return(sum([1 for s in scores if s in trianglenums]))


if __name__ == "__main__":
    with open("pe42.txt", 'r') as f:
        names = [s.strip("\"") for s in f.read().split(",")]
    print(coded_triangle_num(names))
