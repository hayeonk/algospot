from bisect import bisect
import sys

rl = lambda: sys.stdin.readline()
for _ in xrange(input()):
	n = input()
	cnt = 0
	keys = []
	datas = []
	for _ in xrange(n):
		x, y = map(int, rl().split())
		y = -y
		i = bisect(keys, x)
		if i == len(keys) or datas[i] > y:
			keys.insert(i, x)
			datas.insert(i, y)
		j = bisect(datas, y, 0, i)
		del keys[j:i]
		del datas[j:i]
		cnt += len(keys)
	print cnt