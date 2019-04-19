INF = 987654321

def bitCount(n):
	return bin(n).count("1")

def graduate(semester, taken):
	if bitCount(taken) >= k:
		return 0
	if semester == m:
		return INF
	if cache[semester][taken] != -1:
		return cache[semester][taken]
	
	ret = INF
	canTake = classes[semester] & ~taken
	for i in xrange(n):
		if canTake & (1 << i) and taken & prerequisite[i] != prerequisite[i]:
			canTake &= ~(1 << i)
	
	take = canTake
	while take:
		if bitCount(take) > l:
			take = (take - 1) & canTake
			continue
		ret = min(ret, graduate(semester + 1, taken | take) + 1)
		take = (take - 1) & canTake
	
	ret = min(ret, graduate(semester + 1, taken))
	cache[semester][taken] = ret
	return ret

for _ in xrange(input()):
	n, k, m, l = map(int, raw_input().split())
	prerequisite = [0] * n
	classes = [0] * m
	cache = [[-1] * (1 << n) for _ in xrange(m)]
	for i in xrange(n):
		for c in map(int, raw_input().split())[1:]:
			prerequisite[i] |= (1 << c)
	for i in xrange(m):
		for c in map(int, raw_input().split())[1:]:
			classes[i] |= (1 << c)
	
	ret = graduate(0, 0)
	if ret == INF:
		print "IMPOSSIBLE"
	else:
		print ret