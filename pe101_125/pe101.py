"""
Problem 101: Optimum polynomial
https://projecteuler.net/problem=101

Solution:
Let N be the length of the sequence. For i = 1, ..., N,
fit a polynomial to the sequence up to the i-th term. 
This can be done by solving a corresponding linear system. 
"""
import numpy as np


def pe101(func, N):
	"""Computes the sum of the FITs for the BOPs."""
	FITs = []
	seq = [func(n) for n in range(N+1)]
	
	# Compute the sequence
	for i in range(1, N):
		A = []
		b = []
		for n in range(1, i+1): # n-th equation
			a = [n**k for k in range(0, i)] # Coefficient matrix
			A.append(a)
			b.append(seq[n])
		x = np.linalg.solve(A, b) # Find the coefficients
		FIT = x.T@[(n+1)**p for p in range(i)]
		if FIT != seq[n+1]:
			FITs.append(FIT) # Remark: FITs always exist
	return int(sum(FITs))


if __name__ == "__main__":
	# def test(n):
	# 	return n**3
	# print(pe101(test, 4))
	def f(n):
		return 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
	print(pe101(f, 11))