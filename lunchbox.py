for _ in xrange (input()):
	n = input()
	m = map(int, raw_input().split())
	e = map(int, raw_input().split())
	order = []
	for i in xrange(n):
		order.append((e[i], m[i]))
	order.sort(reverse=True)
	
	ret = 0
	beginEat = 0
	for e, m in order:
		beginEat += m
		ret = max(ret, beginEat + e)
	print ret