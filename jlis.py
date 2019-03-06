import sys

MIN = -3000000000

def jlis():
	for ai in reversed(xrange(-1, n)):
		for bi in reversed(xrange(-1, m)):
			a = MIN if ai == -1 else A[ai]
			b = MIN if bi == -1 else B[bi]
			maxVal = max(a, b)
			
			ret = 0
			for i in xrange(ai+1, n):
				if maxVal < A[i]:
					val = M[i+1][bi+1] + 1
					ret = max(ret, val)
			for i in xrange(bi+1, m):
				if maxVal < B[i]:
					val = M[ai+1][i+1] + 1
					ret = max(ret, val)
			M[ai+1][bi+1] = ret
	return M[0][0]

rl = lambda: sys.stdin.readline()

for _ in xrange (input()):
	n, m = map(int, rl().split())
	A = map(int, rl().split())
	B = map(int, rl().split())
	M = [[0] * (m+1) for _ in xrange (n+1)]
	
	print jlis()