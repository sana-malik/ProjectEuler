from math import pow

def triple1000():
	for a in range(1, 999):
		for b in range(a+1, 999):
			c = 1000 - a - b
			if a*a + b*b == c*c and a+b+c==1000:
				return a*b*c
	return None
	
print triple1000()