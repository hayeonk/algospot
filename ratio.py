import math

def solve():
	r = int(m * 100 / n + 1)
	if r >= 100:	
		return -1
	ret = int(math.ceil((r * n - 100 * m) / (100 - r)))
	return ret if ret <= 2000000000 else -1
	
for _ in xrange (input()):
	n, m = map(float, raw_input().split())
	print solve()