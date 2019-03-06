def decision(d):
	visited = [True] + [False] * (n - 1)
	q = [ 0 ]
	seen = 0
	while q:
		here = q.pop(0)
		seen += 1
		for there in xrange (n):
			if not visited[there] and dist[here][there] <= d:
				visited[there] = True
				q.append(there)
	return seen == n
	
def optimize():
	lo, hi = 0.0, 1416.0
	for it in xrange (100):
		mid = (lo + hi) / 2
		if decision(mid):
			hi = mid
		else:
			lo = mid
	return hi
	
def getDist(i, j):
	x1, y1 = points[i]
	x2, y2 = points[j]
	return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def calcDist():
	for i in xrange (n):
		for j in xrange (i + 1, n):
			dist[i][j] = getDist(i, j)
			dist[j][i] = dist[i][j]

for _ in xrange (input()):
	n = input()
	points = []
	for _ in xrange (n):
		x, y = map(float, raw_input().split())
		points.append((x, y))
	dist = [[0] * n for _ in xrange (n)]
	calcDist()
	print "%.2f" % optimize()
	