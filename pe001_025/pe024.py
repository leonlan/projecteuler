from math import factorial

def lexicographic_permutation(n,i):
    """Finds the i-th lexicographic permutation of all digits 0, ..., n."""

    digits = list(range(n+1))
    remainder = i-1
    num = ''
    k = len(digits)

    while k != 0:
        idx = (remainder//factorial(k-1)) 
        num = num + str(digits.pop(idx))
        remainder = remainder - idx*factorial(k-1)
        k -= 1
    return(num)

if __name__ == "__main__":
    print(lexicographic_permutation(9, 1000000))
