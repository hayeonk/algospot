import sys
from itertools import combinations
rl = lambda: sys.stdin.readline().split()

for t in xrange(input()):
	n, m = map(int, rl())
	X = map(int, rl())
	Y = map(int, rl())
	graph = [[0] * n for _ in xrange(n)]
	
	for i, j in combinations(range(n), 2):
		graph[i][j] = graph[j][i] = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
	
	for _ in xrange(m):
		a, b = map(int, rl())
		graph[a][b] = graph[b][a] = 0
	
	added = [False] * n
	minWeight = [1e10] * n
	ret = minWeight[0] = 0.0
	
	for _ in xrange(n):
		u = -1
		for v in xrange(n):
			if not added[v] and (u == -1 or minWeight[u] > minWeight[v]):
				u = v
		added[u] = True
		ret += minWeight[u] ** 0.5
		
		for v in xrange(n):
			if not added[v] and minWeight[v] > graph[u][v]:
				minWeight[v] = graph[u][v]
	print ret