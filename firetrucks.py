import sys
from collections import defaultdict
from heapq import *

def shortestPath(src):
	dist[src] = 0
	pq = [(0, src)]
	
	while pq:
		d, u = heappop(pq)
		for v in graph[u]:
			nextDist = d + graph[u][v] 
			if dist[v] > nextDist:
				dist[v] = nextDist
				heappush(pq, (nextDist, v))
				
rl = lambda: sys.stdin.readline().split()
for _ in xrange(input()):
	V, E, n, m = map(int, rl())
	graph = defaultdict(dict)
	for i in xrange(E):
		a, b, t = map(int, rl())
		graph[a][b] = t
		graph[b][a] = t
	fire = map(int, rl())
	for b in map(int, rl()):
		graph[0][b] = 0
	
	dist = [1e200] * (V + 1)
	shortestPath(0)
	print sum([dist[f] for f in fire])