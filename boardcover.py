def setXY(y, x, type, delta):
	ok = True
	for i in range (3):
		ny = y + coverType[type][i][0]
		nx = x + coverType[type][i][1]
		if ny < 0 or ny >= n or nx < 0 or nx >= m:
			ok = False
		else: 
			board[ny][nx] += delta
			if board[ny][nx] > 1:
				ok = False
	return ok

def cover():
	y, x = -1, -1
	for i in range (n):
		for j in range (m):
			if board[i][j] == 0:
				y, x = i, j
				break
		if y != -1:
			break
	
	if y == -1:
		return 1
		
	ret = 0
	for type in range (4):
		if setXY(y, x, type, 1):
			ret += cover()
		setXY(y, x, type, -1)
	return ret

coverType = [
	[ [0, 0], [1, 0], [0, 1] ],
	[ [0, 0], [0, 1], [1, 1] ],
	[ [0, 0], [1, 0], [1, 1] ],
	[ [0, 0], [1, 0], [1, -1] ]
]

for _ in xrange (input()):
	n, m = map(int, raw_input().split())
	board = [[0] * m for _ in range (n)] 
	
	for i in xrange (n):
		row = raw_input()
		for j in range (m):
			if row[j] == "#":
				board[i][j] = 1

	print cover()
	