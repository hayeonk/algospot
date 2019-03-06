def jump(y, x):
	if y >= n or x >= n:
		return 0
	if y == n-1 and x == n-1:
		return 1
	ret = cache[y][x]
	if ret != -1:
		return ret
	jumpSize = board[y][x]
	cache[y][x] = jump(y + jumpSize, x) or jump(y, x + jumpSize)
	return cache[y][x]

for _ in xrange (input()):
	n = input()
	board = []
	cache = [[-1] * n for i in xrange (n)]
	for i in xrange (n):
		row = map(int, raw_input().split())
		board.append(row)
	print "YES" if jump(0, 0) else "NO"