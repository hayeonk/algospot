def decision(cameras, gap):
	limit = -1
	installed = 0
	for i in xrange (m):
		if limit <= location[i]:
			installed += 1
			limit = location[i] + gap
	return installed >= cameras

def optimize(cameras):
	lo = 0
	hi = 241
	for it in xrange (100):
		mid = (lo + hi) / 2.0
		if decision(cameras, mid):
			lo = mid
		else:
			hi = mid
	return lo
	
for _ in xrange (input()):
	n, m = map(int, raw_input().split())
	location = map(float, raw_input().split())
	print "%.2f" % optimize(n)