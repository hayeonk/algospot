import sys
from collections import defaultdict
rl = lambda: sys.stdin.readline().split()
INF = sys.maxint

def bellman(src, target, graph):
	dist = [INF] * G
	dist[src] = 0
	for t in xrange(G-1):
		for u in xrange(G):
			for v, cost in graph[u]:
				dist[v] = min(dist[v], dist[u] + cost)
	
	for u in xrange(G):
		for v, cost in graph[u]:
			if dist[u] + cost < dist[v]:
				if reachable[src][u] and reachable[u][target]:
					return -INF
	return dist[target]
	
def reach():
	for k in xrange(G):
		for i in xrange(G):
			for j in xrange(G):
				reachable[i][j] |= (reachable[i][k] and reachable[k][j])
				
for _ in xrange(input()):
	G, W = map(int, rl())
	graph1 = defaultdict(list)
	graph2 = defaultdict(list)
	reachable = [[0] * G for _ in xrange(G)]
	
	for i in xrange(W):
		a, b, d = map(int, rl())
		graph1[a].append((b, d))
		graph2[a].append((b, -d))
		reachable[a][b] = 1
	
	reach()
	if not reachable[0][1]:
		print "UNREACHABLE"
	else:
		v1 = bellman(0, 1, graph1)
		v2 = bellman(0, 1, graph2)	
		v1 = str(v1) if v1 != -INF else "INFINITY"
		v2 = str(-v2) if v2 != -INF else "INFINITY"
		print v1, v2