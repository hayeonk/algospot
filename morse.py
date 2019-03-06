def kth(n, m, skip):
	if n == 0:
		return "o" * m
	if skip < bino[n+m-1][n-1]:
		return "-" + kth(n-1, m, skip)
	return "o" + kth(n, m-1, skip - bino[n+m-1][n-1])

def calcBino():
	for i in range (200):
		bino[i][0] = bino[i][i] = 1
		for j in range (1, i):
			bino[i][j] = min(M, bino[i-1][j-1] + bino[i-1][j])

M = 1000000000 + 100
bino = [[0] * 201 for _ in xrange (201)]
calcBino()
for _ in xrange (input()):
	n, m, k = map(int, raw_input().split())
	print kth(n, m, k-1)