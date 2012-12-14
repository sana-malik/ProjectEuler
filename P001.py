sum = 0
fibb = 1
fib = 2

while (fib < 4000000):
	if fib%2==0:
		sum += fib
	fib += fibb
	fibb = fib - fibb
	

print sum;