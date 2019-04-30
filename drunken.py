import sys
rl = lambda: sys.stdin.readline().split()
INF = sys.maxint

V, E = map(int, rl())
D = map(int, rl())
graph = [[INF] * V for _ in xrange(V)]
W = [[INF] * V for _ in xrange(V)]
for _ in xrange(E):
	a, b, c = map(int, rl())
	graph[a-1][b-1] = c
	graph[b-1][a-1] = c

def solve():
	global D
	D = [(D[i], i) for i in xrange(V)]
	D.sort()
	
	for i in xrange(V):
		for j in xrange(V):
			if i == j:
				W[i][j] = 0
			else:
				W[i][j] = graph[i][j]
	
	for k in xrange(V):
		d, w = D[k]
		for i in xrange(V):
			for j in xrange(V):
				graph[i][j] = min(graph[i][j], graph[i][w] + graph[w][j])
				W[i][j] = min(W[i][j], graph[i][w] + d + graph[w][j])

solve()
for _ in range(input()):
	s, t = map(int, rl())
	print W[s-1][t-1]