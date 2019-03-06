INF = 987654321

def minError(lo, hi):
	sum = pSum[hi] - 0 if lo == 0 else pSum[hi] - pSum[lo-1]
	sqSum = pSqSum[hi] - 0 if lo == 0 else pSqSum[hi] - pSqSum[lo-1]
	m = int(float(sum) / (hi - lo + 1) + 0.5)
	ret = sqSum - 2 * m * sum + m * m * (hi - lo + 1)
	return ret

def quantize(fr, parts):
	if fr == n:
		return 0
	if parts == 0:
		return INF
	if cache[fr][parts] != -1:
		return cache[fr][parts]
	ret = INF
	for partSize in xrange (1, n - fr + 1):
		ret = min(ret, minError(fr, fr + partSize - 1) + quantize(fr + partSize, parts - 1))
	cache[fr][parts] = ret
	return ret
	
for _ in xrange (input()):
	n, s = map(int, raw_input().split())
	A = map(int, raw_input().split())
	A.sort()
	
	pSum = [A[0]]
	pSqSum = [A[0] * A[0]]
	for i in xrange (1, n):
		pSum.append(pSum[i-1] + A[i])
		pSqSum.append(pSqSum[i-1] + A[i] * A[i])
	
	cache = [[-1] * 11 for i in xrange(101)]
	print quantize(0, s)
	