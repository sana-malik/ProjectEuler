#! /usr/bin/python

from math import sqrt
from itertools import product, starmap, ifilter, takewhile
from operator import add

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
	
def abundantNumbers():
	i = 12
	yield 12
	
	while i <= 28123:
		if d(i) > i:
			yield i
		i += 1


print sum(set(range(1,28124)).difference(set(ifilter(lambda x : x<=28123, (starmap(add,product(abundantNumbers(), abundantNumbers())))))))
