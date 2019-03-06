import sys

def search(here, days):
	if days == 0:
		return 1.0 if here == p else 0.0
	if m[here][days] != -1:
		return m[here][days]
	ret = 0.0
	for there in range(n):
		if connected[here][there]:
			ret += search(there, days-1) / connected[there].count(1)
	m[here][days] = ret
	return ret

rl = lambda: sys.stdin.readline()
for _ in xrange (input()):
	n, d, p = map(int, rl().split())
	connected = [map(int, rl().split()) for _ in xrange (n)]
	t = int(rl())
	qList = map(int, rl().split())
	m = [[-1] * (d+1) for _ in xrange (n)]
	
	result = []
	for q in qList:
		result.append(search(q, d))
	print " ".join(map(str, result))