def differentiate(poly):
	ret = []
	n = len(poly) - 1
	for i in xrange(n):
		ret.append(poly[i] * (n - i))
	return ret

def solveNaive(poly):
	if len(poly) == 2:
		return [ -poly[1]/poly[0] ]
	a, b, c = poly
	r = b**2 - 4*a*c
	if r < 0:
		return []
	elif r == 0:
		return [ -b/(2.0 * a) ]
	else:
		return [ (-b - r**0.5)/(2.0 * a), (-b + r**0.5)/(2.0 * a)]
	
def evaluate(poly, x0):
	ret = 0
	n = len(poly)
	for i in xrange(n):
		ret += poly[i] * (x0 ** (n-i-1))
	return ret
		
def solve(poly):
	n = len(poly) - 1
	if n <= 2:
		return solveNaive(poly)
	derivative = differentiate(poly)
	sols = solve(derivative)
	sols = [-L-1] + sols + [L+1]

	ret = []
	for i in xrange (len(sols)-1):
		x1, x2 = sols[i], sols[i+1]
		y1, y2 = evaluate(poly, x1), evaluate(poly, x2)
		if y1 * y2 > 0: continue
		if y1 > y2:
			y1, y2 = y2, y1
			x1, x2 = x2, x1
		for it in xrange (100):
			mx = (x1 + x2) / 2
			my = evaluate(poly, mx)
			if y1 * my > 0:
				x1, y1 = mx, my
			else:
				x2, y2 = mx, my
		ret.append((x1 + x2) / 2)

	ret.sort()
	return ret

L = 25.0
for _ in xrange (input()):
	n = input()
	poly = map(float, raw_input().split())
	ret = map(str, solve(poly))
	print " ".join(ret)