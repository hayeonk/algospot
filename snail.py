import sys

def climb(n, m):
	if m >= n:
		return 1.0
	if m == 0:
		return 0
	if (n, m) in d:
		return d[(n, m)]
	d[(n, m)] = 0.75 * climb(n-2, m-1) + 0.25 * climb(n-1, m-1)
	return d[(n, m)]

rl = lambda: sys.stdin.readline()
d = {}
for _ in xrange (input()):
	n, m = map(int, rl().split())
	print climb(n, m)