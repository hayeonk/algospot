def lis(start):
	if m[start] != -1:
		return m[start]
		
	ret = 1
	for next in xrange (start+1, n):
		if S[start] < S[next]:
			ret = max(ret, lis(next) + 1)
	m[start] = ret
	return ret

for _ in xrange (input()):
	n = input()
	S = map(int, raw_input().split())
	m = [-1] * n
	
	maxLen = 0
	for begin in xrange (n):
		maxLen = max(maxLen, lis(begin))
	print maxLen