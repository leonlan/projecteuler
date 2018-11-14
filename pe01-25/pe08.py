import numpy as np

"""
Problem:
https://projecteuler.net/problem=8

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

The four adjacent digits in the 1000-digit number that have the greatest 
product are 9 × 9 × 8 × 9 = 5832. Find the thirteen adjacent digits in the 
1000-digit number that have the greatest product. What is the value of this product?

Solution:
Consider all the 13-length numbers in the series. Note that we can optimise
the search if we find a 0 in the number (because the product will be 0). 
In this case, we skip to the index of the found 0.

"""
# Make an array of integers from the text file.
L = open("pe8.txt", "r").readlines()
series = np.array([int(x) for x in ''.join(line.strip() for line in L)], dtype='int64')

def product_series(L, n):
    """Finds the n adjacent digits in the series with the greatest product."""    
    maxprod = 0
    numlength = n
    serieslength = len(L)
    i = 0
    while i < (serieslength - numlength + 1):
        num = L[i:i+numlength]
        # If there is a zero in the number, move to the index of the zero.
        if 0 in num:
            i += max(np.where(num==0)[0]) + 1
        # Else calculate the product of the digits in the number.
        else:
            newprod = np.multiply.reduce(num)
            if maxprod < newprod:
                maxprod = newprod
            i += 1
    return(maxprod)

print("The largest product of four adjacent digits are:", 
    product_series(series, 4))
print("The largest product of thirteen adjacent digits are:", 
    product_series(series, 13))