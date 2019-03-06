import heapq
import sys

def dijkstra(src):
	dist[src] = 1.0
	pq = []
	heapq.heappush(pq, (1.0, src))
	
	while pq:
		cost, here = heapq.heappop(pq)
		
		for there, c in adj[here]:
			nextDist = cost * c
			if dist[there] > nextDist:
				dist[there] = nextDist
				heapq.heappush(pq, (nextDist, there))

rl = lambda: sys.stdin.readline()

for _ in xrange (int(rl())):
	V, E = map(int, rl().split())
	adj = [[] for i in xrange (V)]
	for i in xrange (E):
		input = rl().split()
		u, v, w = int(input[0]), int(input[1]), float(input[2])
		adj[u].append((v, w))
		adj[v].append((u, w))
		
	dist = [1e200] * V
	dijkstra(0)
	print dist[-1]
	