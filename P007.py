from math import sqrt

def nth_prime(n):
	primes = []
	p = 2
	while (len(primes) < n):
		if is_prime(p):
			primes.append(p)
		p += 1
	return p-1
	
def is_prime(n):
	for i in range(2, int(sqrt(n)+1)):
		if n % i == 0:
			return False
	return True
		
print nth_prime(6)
print nth_prime(10001)