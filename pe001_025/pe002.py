"""
Problem:
By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

Solution:
Note that the parity of even and odd terms is periodic:
	(1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...)
	(odd, even, odd, odd, even, odd, odd, even, odd, odd)

Which follows from the fact that
	odd + even = odd
	even + odd = odd
	odd + odd = even

Hence, to find a solution to this problem, we only need to consider every 
3rd elements in the Fibonnaci sequence.

"""

def sum_evenfibonnaci(n):
	"""Finds the sum of all even terms in the Fibonnaci sequence up to n."""
	i = [1,2]
	j = 0
	total = 2
	while i[1] < n:
		i[1] = i[0]+i[1] 
		i[0] = i[1]-i[0]
		j += 1
		if j % 3 == 0:
			total += i[1]
	return(total)


def alternative(n):
	"""Finds the sum of all even terms in the Fibonnaci sequence up to n."""
	i=[1,2]
	j=1
	total = 2
	while i[j] < n:
		j += 1
		i.append(i[j-1]+i[j-2])
		if (j-1) % 3 == 0:
			total += i[j]
	return(total)


print(sum_evenfibonnaci(4e6))
