import sys
import gc
rl = lambda: sys.stdin.readline().split()

class fenwick(object):
	def __init__(self, size):
		self.tree = [0] * size
	
	def add(self, pos, val):
		pos += 1
		while pos < len(self.tree):
			self.tree[pos] += val
			pos += (pos & -pos)

	def sum(self, pos):
		pos += 1
		ret = 0
		while pos:
			ret += self.tree[pos]
			pos &= pos - 1
		return ret

for _ in xrange(input()):
	gc.collect()
	n = input()
	A = map(int, rl())
	tree = fenwick(1000001)
	ret = 0
	for i in xrange(n):
		ret += tree.sum(999999) - tree.sum(A[i])
		tree.add(A[i], 1)
	print ret