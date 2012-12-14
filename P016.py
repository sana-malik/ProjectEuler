#! /usr/bin/python

def sum_of_dig(b, e):
	s = str(b**e);
	sum = 0
	for c in s:
		sum += int(c)
	return sum
	
print sum_of_dig(2, 15)
print sum_of_dig(2, 1000)