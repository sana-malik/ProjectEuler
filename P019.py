#!/usr/bin/python
from math import floor

def isLeapYear(year):
	if str(year)[-2:]== '00':
		return year % 400 == 0
	return year % 4 == 0
	
def daysInYear(year):
	if isLeapYear(year):
		return 366
	return 365

def daysInMonth(month, year):
	if month in [4, 6, 9, 11]:
		return 30
	elif month in [1, 3, 5, 7, 8, 10, 12]:
		return 31
	elif isLeapYear(year):
		return 29
	else:
		return 28

def dayOfYear(month, day, year):
	days = 0
	for m in range(1, month):
		days += daysInMonth(m, year)
	return days + day

def daysSince1900(month, day, year):
	days = 0
	for y in range(1900, year):
		days += daysInYear(y)
	return days + dayOfYear(month, day, year)
	
def isSunday(month, day, year):
	days = daysSince1900(month, day, year)
	return days % 7 == 0

def numSundays(year):
	count = 0
	for m in range(1, 13):
		if isSunday(m, 1, year):
			count += 1
	return count
	
def sundaysInCentury(year):
	count = 0
	for y in range(1901, year+1):
		count += numSundays(y)
	return count
	
print sundaysInCentury(2000)