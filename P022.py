#! /usr/bin/python

def score(name):
	return sum(map(lambda n : ord(n)-ord('A')+1, name))

file = open('names.txt')
names = sorted(file.read().replace('"','').split(','))
file.close()

totalScore = 0
for i, name in enumerate(names):
	totalScore += (i+1)*score(name)
	
print totalScore
print 938*score('COLIN')