import numpy as np

"""
Problem:
https://projecteuler.net/problem=22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into 
alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a 
name score.

For example, when the list is sorted into alphabetical order, COLIN, which 
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

L = open("pe22.txt", "r").read().split(",")
L.sort()
names = [l.strip('"') for l in L]

def wordscore(s):
    """Computes the alphabetical value of the string s."""
    return(sum([(ord(c) - ord('A') + 1) for c in s]))

def total_namesscore(names):
    """Computes the total of name scores of a names list."""
    namesscore = np.array([wordscore(s) for s in names])
    return(np.inner(namesscore, np.arange(1,(len(names)+1))))    

print(total_namesscore(names))