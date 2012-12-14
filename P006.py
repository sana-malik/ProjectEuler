from math import pow

def diff(n):
	square_of_sum = pow(n*(n+1)/2, 2)
	sum_of_squares = sum([pow(i, 2) for i in range(1, n+1)])
	return int(square_of_sum - sum_of_squares)

#### closed-er form
def closed(n):
	square_of_sum = pow(n*(n+1)/2, 2)
	sum_of_squares = n*(n+1)*(2*n+1)/6
	return int(square_of_sum - sum_of_squares)
	
print diff(10)
print diff(100)
print closed(10)
print closed(100)