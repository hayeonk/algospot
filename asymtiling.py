MOD = 1000000007

def tiling(n):
	if n <= 1:
		return 1
	if m[n] != -1:
		return m[n]
	m[n] = (tiling(n-1) + tiling(n-2)) % MOD
	return m[n]

def asymmetric(width):
	if (width % 2):
		return (tiling(width) - tiling(width/2) + MOD) % MOD
	
	ret = tiling(width)
	ret = (ret - tiling(width/2) + MOD) % MOD
	ret = (ret - tiling(width/2 - 1) + MOD) % MOD
	return ret

m = [-1] * 101
for _ in xrange(input()):
	print asymmetric(input())