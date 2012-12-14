from math import sqrt

def is_prime(n):
	for i in range(2, int(sqrt(n)+1)):
		if n % i == 0:
			return False
	return True

def sum_of_primes(n):
	if n < 2:
		return 0
	sum = 2
	if n % 2 == 0:
		n = n - 1
	for i in range(3, n, 2):
		if is_prime(i):
			sum += i
	return sum

print sum_of_primes(10)
print sum_of_primes(2000000)