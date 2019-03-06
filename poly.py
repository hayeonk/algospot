MOD = 10000000

def poly(n, first):
	if n == first:
		return 1
	if m[n][first] != -1:
		return m[n][first]
	ret = 0
	for second in range (1, n - first + 1):
		ret = (ret + ((second + first - 1) * poly(n - first, second) % MOD)) % MOD
	m[n][first] = ret
	return ret

m = [[-1] * 101 for _ in xrange (101)]
for _ in xrange (input()):
	n = input()
	ret = 0
	for first in range (1, n+1):
		ret += poly(n, first)
	print ret % MOD 