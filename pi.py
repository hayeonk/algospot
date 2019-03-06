import sys

def classify(a, b):
	M = N[a:b]
	if len(set(M)) == 1:
		return 1
	
	progressive = True
	for i in range(len(M)-1):
		if M[i+1] - M[i] != M[1] - M[0]:
			progressive = False
	if progressive and abs(M[1] - M[0]) == 1:
		return 2
	
	alternating = True
	for i in range(len(M)):
		if M[i] != M[i%2]:
			alternating = False
	if alternating: return 4
	if progressive: return 5
	return 10

def memorize():
	n = len(N)
	cache[2] = classify(0, 3)
	cache[3] = classify(0, 4)
	cache[4] = classify(0, 5)
	
	for i in xrange(3, n):
		for j in xrange(3, 6):
			if i - j >= 0:
				cache[i] = min(classify(i-j+1, i+1) + cache[i-j], cache[i])
	return cache[-1]

rl = lambda: sys.stdin.readline().strip()
for _ in xrange (input()):
	N = map(int, list(rl()))
	cache = [987654321] * len(N)
	print memorize()
	