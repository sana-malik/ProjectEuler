from collections import defaultdict
from operator import mul
from math import sqrt, log, pow

def prime_factors(n):
	if n < 2:
		return [n]
	p = 2
	factors = []
	while n > 1:
		if n % p == 0:
			factors.append(p)
			n = n/p
		else:
			p += 1
	return factors

def GCD(n):
	factors = []
	for i in range(n, 1, -1):
		nFact = prime_factors(i)
		if list_diff(nFact, factors):
			factors.extend(list_diff(nFact,factors))
	return factors

def list_diff(a,b):
	diff = []
	bNum = defaultdict(int)
	for elem in b:
		bNum[elem] += 1
	diff = []
	for elem in a:
		if bNum[elem] == 0:
			diff.append(elem)
		else:
			bNum[elem] -= 1
	return diff

print reduce(mul, GCD(10))
print reduce(mul, GCD(20))


###########################################
## another way

def get_primes_less_than(n):
	primes = []
	for i in range(2, n+1):
		if is_prime(i):
			primes.append(i)
	return primes
	
def is_prime(n):
	for i in range(2, int(sqrt(n)+1)):
		if n % i == 0:
			return False
	return True

def smallest_product(n):
	product = 1
	for prime in get_primes_less_than(n):
		product *= pow(prime,int(log(n, prime)))
	return int(product)

print smallest_product(10)
print smallest_product(20)