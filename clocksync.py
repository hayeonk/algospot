linked = [
	"xxx.............",
	"...x...x.x.x....",
	"....x.....x...xx",
	"x...xxxx........",
	"......xxx.x.x...",
	"x.x...........xx",
	"...x..........xx",
	"....xx.x......xx",
	".xxxxx..........",
	"...xxx...x...x.."
]

def areAligned():
	if len(set(clocks)) == 1 and clocks[0] == 12:
		return True
	return False

def push(swtch):
	for clock in range (16):
		if linked[swtch][clock] == "x":
			clocks[clock] += 3
			if clocks[clock] == 15:
				clocks[clock] = 3

def solve(swtch):
	if areAligned():
		return 0
	
	if swtch == 10:
		return 9999
	
	ret = 9999
	for cnt in range (4):
		ret = min(ret, cnt + solve(swtch + 1))
		push(swtch)
		
	return ret

for _ in xrange (input()):
	clocks = map(int, raw_input().split())
	
	ret = solve(0)
	print ret if ret != 9999 else -1