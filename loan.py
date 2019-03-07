def balance(amount, d, r, c):
	left = amount
	for i in xrange (d):
		left *= (1.0 + (r / 12.0) / 100.0)
		left -= c
	return left
	
def payment(amount, d, r):
	lo = 0
	hi = amount * (1.0 + (r / 12.0) / 100.0)
	for it in xrange (100):
		mid = (lo + hi) / 2.0
		if balance(amount, d, r, mid) <= 0:
			hi = mid
		else:
			lo = mid
	return hi

for _ in xrange (input()):
	n, m, p = map(float, raw_input().split())
	print payment(n, int(m), p)