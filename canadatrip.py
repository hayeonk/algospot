import sys

def decision(dist):
	ret = 0
	for l, m, g in lmg:
		if dist >= l - m:
			ret += (min(dist, l) - (l - m)) / g + 1
	return ret >= k

def optimize():
	lo, hi = -1, 80300001
	while lo + 1 < hi:
		mid = (lo + hi) / 2
		if decision(mid):
			hi = mid
		else:
			lo = mid
	return hi
	
rl = lambda: sys.stdin.readline()
for _ in xrange (input()):
	n, k = map(int, rl().split())
	lmg = []
	for _ in xrange (n):
		lmg.append(map(int, rl().split()))
	print optimize()