MOD = 1000000007

def tiling(width):
	if width <= 1:
		return 1
		
	if m[width] != -1:
		return m[width]
	m[width] = (tiling(width-2) + tiling(width-1)) % MOD
	return m[width]

m = [-1] * 101
for _ in xrange (input()):
	print tiling(input())