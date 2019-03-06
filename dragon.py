MAX = 1000000000 + 1

def precalc():
	for i in xrange (1, 51):
		length.append(min(MAX, length[i-1] * 2 + 2))
		
def expand(dragonCurve, generations, skip):
	if generations == 0:
		return dragonCurve[skip]
	
	for i in xrange(len(dragonCurve)):
		if dragonCurve[i] == "X" or dragonCurve[i] == "Y":
			if skip >= length[generations]:
				skip -= length[generations]
			elif dragonCurve[i] == "X":
				return expand(EXPAND_X, generations - 1, skip)
			else:
				return expand(EXPAND_Y, generations - 1, skip)
		elif skip > 0:
			skip -= 1
		else:
			return dragonCurve[i]

length = [1]
EXPAND_X = "X+YF"
EXPAND_Y = "FX-Y"
precalc()
for _ in xrange (input()):
	n, p, l = map(int, raw_input().split())
	s = ""
	for i in xrange (p - 1, p + l - 1):
		s += expand("FX", n, i)
	print s