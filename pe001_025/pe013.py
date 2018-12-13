"""
Problem:
https://projecteuler.net/problem=13

Work out the first ten digits of the sum of the following one-hundred 50-digit 
numbers (see link).

Solution:
Consider a summation of 100 12-digit numbers of 1 followed by only 9s. First, we
consider adding 10 12-digit nines (199 999 999 999), which results in 

    1 999 999 999 990

The first ten digits of this number are not influenced by the 11th or 12th
digit. Clearly, adding another 12 digit nine gives us

    2 199 999 999 989

So by adding 11 of such numbers, we see that the first ten digits are
influenced by the 11th digits. It follows that adding 101+ of such numbers,
the first ten digits are influenced by the 11th and 12th digits. 

Hence, for the actual problem we only need to take the first 11 digits of each 
number to correctly find the first 10 digits of the sum.

"""
L = open('pe13.txt','r').readlines()
numbers = [int(line.strip()[0:11]) for line in L]
sum = 0
for number in numbers:
    sum += number
print(str(sum)[0:10])