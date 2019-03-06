def toInt():
	ret = 0
	for y in xrange (3):
		for x in xrange (3):
			ret *= 3
			if board[y][x] == "o": ret += 1
			elif board[y][x] == "x": ret += 2
	return ret

def nextTurn(turn):
	return "o" if turn == "x" else "x"
	
def isFinished(turn):
	for i in xrange (3):
		if board[0][i] == board[1][i] == board[2][i] == turn: return True
		if board[i][0] == board[i][1] == board[i][2] == turn: return True
	if board[0][0] == board[1][1] == board[2][2] == turn: return True
	if board[0][2] == board[1][1] == board[2][0] == turn: return True
	return False

def canWin(turn):
	if isFinished(nextTurn(turn)): 
		return -1
	if m[toInt()] != -2:
		return m[toInt()]
	minVal = 2
	for y in range (3):
		for x in range (3):
			if board[y][x] == ".":
				board[y][x] = turn
				minVal = min(minVal, canWin(nextTurn(turn)))
				board[y][x] = "."
	if minVal == 2 or minVal == 0:
		m[toInt()] = 0
	else:
		m[toInt()] = -minVal
	return m[toInt()]

def getTurn():
	xCnt = 0
	oCnt = 0
	for row in board:
		xCnt += row.count('x')
		oCnt += row.count('o')
	if xCnt > oCnt:
		return "o"
	return "x"

for _ in xrange (input()):
	board = [list(raw_input()) for _ in xrange (3)]
	m = [-2] * 19683
	
	ret = canWin(getTurn())
	if ret == 0:
		print "TIE"
	elif ret == 1:
		print getTurn()
	else:
		print nextTurn(getTurn())