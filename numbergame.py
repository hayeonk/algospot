EMPTY = -987654321

def play(l, r):
	if l > r:
		return 0
		
	if m[l][r] != EMPTY:
		return m[l][r]

	ret = max(board[l] - play(l + 1, r), board[r] - play(l, r - 1))
	if r - l >= 1:
		ret = max(ret, -play(l + 2, r))
		ret = max(ret, -play(l, r - 2))
	m[l][r] = ret
	
	return ret 
	
for _ in xrange (input()):
	n = input()
	board = map(int, raw_input().split())
	m = [[EMPTY] * n for _ in xrange (n)]
	
	print play(0, n-1)