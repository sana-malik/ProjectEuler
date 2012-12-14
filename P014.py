#! /usr/bin/python

def seq(n):
	yield n
	
	while (n != 1):
		if n%2 == 0:
			n = n/2
		else:
			n = 3*n+1
		yield n

def longest_chain(n):
	m = 0
	ans = -1
	for i in range(1,n+1):
		print i
		s = [k for k in seq(i)]
		if len(s) > m:
			m = len(s)
			ans = i
	print m
	return ans

print longest_chain(1000000)