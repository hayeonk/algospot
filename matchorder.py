import bisect

for _ in xrange (input()):
	n = input()
	russian = map(int, raw_input().split())
	korean = sorted(map(int, raw_input().split()))
	wins = 0
	
	for rus in russian:
		if rus > korean[-1]:
			korean.pop(0)
		else:
			idx = bisect.bisect_left(korean, rus)
			korean.pop(idx)
			wins += 1
	print wins