def largest_palindrome3():
	largest_so_far = 0
	for n1 in range(999,99,-1):
		for n2 in range(n1, 99, -1):
			if isPalindrome(str(n1*n2)) and n1*n2 > largest_so_far:
				largest_so_far = n1*n2
				break
	return largest_so_far

def largest_palindrome2():
	largest_so_far = 0
	for n1 in range(99,9,-1):
		for n2 in range(n1, 9, -1):
			if isPalindrome(str(n1*n2)) and n1*n2 > largest_so_far:
				largest_so_far = n1*n2
				break
	return largest_so_far

def isPalindrome(s):
	return s == s[::-1]

print largest_palindrome2()
print largest_palindrome3()