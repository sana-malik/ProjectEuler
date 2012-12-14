#! /usr/bin/python

from math import floor

def toWords(n):
	words = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 
			10: "ten", 11: "eleven", 12 : "twelve", 13 : "thirteen", 14: "fourteen", 15: "fifteen", 18: "eighteen",
			20: "twenty", 30 : "thirty", 40: "forty", 50: "fifty", 80: "eighty"}
	
	if n <= 15 or n == 18:
		return words[n]
	elif n < 20:
		return words[n % 10] + "teen"
	elif n < 60 or floor(n/10)==8:
		return words[n-(n%10)] + words[n%10]
	elif n < 100:
		return words[floor(n/10)] + "ty" + words[n%10]
	elif n < 1000:
		out = words[floor(n/100)] + "hundred"
		if n % 100:
			out += "and" + toWords(n%100)
		return out
	elif n==1000:
		return "onethousand"
	else:
		return 'number is too large.'

print len(toWords(342))
print len(toWords(115))
print sum(map(lambda n: len(toWords(n)),range(1,1001)))