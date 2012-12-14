#! /usr/bin/python

from math import sqrt

def factors(n):
	yield 1
	i = 2
	while i < sqrt(n):
		if n % i == 0:
			yield i
			yield n/i
		i += 1
	if sqrt(n) % 1 == 0:
		yield int(sqrt(n))
		
def d(n):
	return sum(factors(n))

def amicablePairs(n):
	sum = 0
	for a in range(1, n):
		b = d(a)
		if b!= a and b < n and a == d(b):
			sum += a
	return sum
	
print amicablePairs(10000)