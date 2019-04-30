import sys
from itertools import combinations
rl = lambda: sys.stdin.readline().split()

for _ in range(input()):
	n, m = map(int, rl())
	X = map(int, rl())
	Y = map(int, rl())
	graph = [[0] * n for _ in xrange(n)]
	
	for i, j in combinations(range(n), 2):
		graph[i][j] = graph[j][i] = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
	
	for i in range(m):
		a, b = map(int, rl())
		graph[a][b] = graph[b][a] = 0.0
	
	added = [False] * n
	minWeight = [1e10] * n
	ret = minWeight[0] = 0.0
	
	for it in range(n):
		u = -1
		for v in range(n):
			if not added[v] and (u == -1 or minWeight[u] > minWeight[v]):
				u = v
		ret += minWeight[u] ** 0.5
		added[u] = True
		
		for v in range(n):
			if not added[v] and minWeight[v] > graph[u][v]:
				minWeight[v] = graph[u][v]
	print ret