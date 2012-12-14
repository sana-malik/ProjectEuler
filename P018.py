#!/usr/bin/python

from collections import defaultdict

data = [[75],
	[95,64],
	[17,47,82],
	[18,35,87,10],
	[20,4,82,47,65],
	[19,1,23,75,3,34],
	[88,2,77,73,7,63,67],
	[99,65,4,28,6,16,70,92],
	[41,41,26,56,83,40,80,70,33],
	[41,48,72,33,47,32,37,16,94,29],
	[53,71,44,65,25,43,91,52,97,51,14],
	[70,11,33,28,77,73,17,78,39,68,17,57],
	[91,71,52,38,17,14,91,43,58,50,27,29,48],
	[63,66,4,68,89,53,67,30,73,16,69,87,40,31],
	[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]
	
babyTriangle = [[3],
	[7,4],
	[2, 4, 6],
	[8, 5, 9, 3]]
	
secondTriangle = [[75],
	[95,64],
	[17,47,82],
	[18,35,87,10]]
	
def makeNode(data, left, right):
	return {'data' : (row, col, data), 'left' : left, 'right' : right}

def adjacency(size):
	nodes = [(i, j) for i in range(0, size) for j in range(0,i+1)]
	graph = {}
	for row, col  in nodes[:-1]:
		graph[(row, col)] = [(row+1, col), (row+1, col+1)]
	
	for col in range(0,size):
		graph[(size-1, col)] = []
	
	return graph
	
def heuristic(row, size):
	return (size - row-1);

def aStar(data):
	adj = adjacency(len(data))
	currentPrev = None
	current = (0,0)
	paths = defaultdict(lambda : {'value' : 0})
	paths[current] = {'hist' : [current], 'value' : data[0][0] + heuristic(0, len(data)), 'actual' : data[0][0]}
	while current != currentPrev:
		neighbors = adj[current]
		for neighbor in neighbors:
			if paths[neighbor]['value'] < data[neighbor[0]][neighbor[1]] + paths[current]['actual'] + heuristic(neighbor[0], len(data)):
				pathy = []
				pathy.extend(paths[current]['hist'])
				pathy.append(neighbor)
				paths[neighbor] = {'hist' : pathy, 'value' : paths[current]['actual'] + data[neighbor[0]][neighbor[1]] + heuristic(neighbor[0], len(data)), 'actual' : paths[current]['actual'] + data[neighbor[0]][neighbor[1]]}

		currentPrev = current
		current = max(paths, key=lambda path : paths[path]['value'])
	
	return paths[current]
	
def bruteForce(data, path):
	if not data: 
		return path
	pathy = []
	pathy.extend(path)
	pathy.append(data[0][0])
	paths = [bruteForce(map(lambda l : l[:-1], data[1:]), pathy),
		bruteForce(map(lambda l : l[1:], data[1:]), pathy)]
	return max(paths, key=sum)
	
		
print bruteForce(babyTriangle, []), sum(bruteForce(babyTriangle, []))
print bruteForce(data, []), sum(bruteForce(data, []))
		