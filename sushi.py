import sys

def sushi():
	mid = M - 4000
	for budget in range (1, mid):
		if budget >= price[effidx]:
			m[budget%201] = pref[effidx] + m[(budget - price[effidx])%201]
		
	for budget in range (mid, M + 1):
		for dish in range (n):
			if budget >= price[dish]:
				m[budget%201] = max(m[budget%201], m[(budget - price[dish])%201] + pref[dish])
		
	return m[M%201]

rl = lambda: sys.stdin. readline()
for _ in xrange (input()):
	n, M = map(int, rl().split())
	M /= 100
	price = []
	pref = []
	for _ in xrange (n):
		i = map(int, rl().split())
		price.append(i[0] / 100)
		pref.append(i[1])
	eff = [s / float(m) for m, s in zip(price, pref)]
	effidx = eff.index(max(eff))
	m = [0] * 201
	print sushi()