"""
Problem:
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

"..."

Although it has not been proved yet (Collatz Problem), it is thought 
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

Solution:
Brute-force approach. Try all numbers from 1-1000000, but keep track of each
number that appears in such sequence. We can then optimize the brute-force.
"""

def collatzseq(n):
    """Returns the number (smaller than n) with the longest Collatz seq."""
    seqlen = {1:1, 2:2}
    largestseqlen, largestseqnum = [1,1]
    for i in range(3, n+1):
        currentnum = i
        j = 1
        seq = []
        while currentnum != 1:
            seq.append(currentnum)            
            # If we know the series length of the current number, shortcut.
            if currentnum in seqlen:
                j += seqlen[currentnum]
                break

            # Even number
            elif currentnum % 2 == 0:
                currentnum = currentnum//2

            # Odd number
            else:
                currentnum = (3*currentnum)+1
            j += 1
        
        # For each new number in the sequence, add it to the list of seqlens.
        for k in range(0, len(seq)):
            seqlen[seq[k]] = j - k - 1

        if j > largestseqlen:
            largestseqlen = j
            largestseqnum = i

    return(largestseqnum)

print(collatzseq(1000000))
