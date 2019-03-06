def reverseq():
	global it
	it += 1
	
	if it >= len(s):
		return ""
	if s[it] == 'b' or s[it] == 'w':
		return s[it]
		
	upperLeft = reverseq()
	upperRight = reverseq()
	lowerLeft = reverseq()
	lowerRight = reverseq()
	
	return "x" + lowerLeft + lowerRight + upperLeft + upperRight

for _ in xrange (input()):
	s  = raw_input()
	it = -1
	print reverseq()