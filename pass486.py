TM = 10000000
factors = [0] * (TM + 1)

def getFactorsBrute():
	for div in xrange (1, TM + 1):
		for multiple in xrange (div, TM + 1, div):
			factors[multiple] += 1

getFactorsBrute()
for _ in xrange (input()):
	n, lo, hi = map(int, raw_input().split())
	ans = 0
	for i in xrange(lo, hi + 1):
		ans += factors[i] == n
	print ans