def count(y, x):
	if y == n-1:
		return 1
	if m[y][x] != -1:
		return m[y][x]
	ret = 0
	if triangle[y+1][x+1] >= triangle[y+1][x]:
		ret += count(y+1, x+1)
	if triangle[y+1][x+1] <= triangle[y+1][x]:
		ret += count(y+1, x)
	m[y][x] = ret
	return ret

for _ in xrange (input()):
	n = input()
	triangle = [map(int, raw_input().split()) for _ in xrange (n)]
	for i in reversed(xrange(n-1)):
		for j in xrange(i+1):
			triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
	m = [[-1] * n for _ in xrange (n)]
	print count(0, 0)