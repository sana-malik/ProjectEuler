#! /usr/bin/python

from math import sqrt

def tri(n):
	return (n+1)*(n)/2
	

def factors(n):
	facts = []
	for i in range(1,int(sqrt(n))):
		if n % i == 0:
			facts.append(i)
			facts.append(n/i)
	if sqrt(n) % 1 == 0:
		facts.append(sqrt(n))
	return facts

def first_with(n):
	facts = []
	i = 1
	while len(facts) < n:
		facts = factors(tri(i))
		i += 1
	return tri(i-1)
	
print first_with(5)
print first_with(500)