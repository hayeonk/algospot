def path(y, x):
	if y == n-1:
		return triangle[y][x]
	ret = m[y][x]
	if ret != -1:
		return ret
	m[y][x] = max(path(y+1, x), path(y+1, x+1)) + triangle[y][x]
	return m[y][x]

for _ in xrange (input()):
	n = input()
	triangle = [map(int, raw_input().split()) for i in xrange (n)]
	m = [[-1] * 100 for i in xrange (100)]
	print path(0, 0)