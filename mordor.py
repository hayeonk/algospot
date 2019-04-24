import sys
import gc
from math import log
rl = lambda: sys.stdin.readline().split()
INT_MAX = 987654321

class RMQ(object):
	def __init__(self, A):
		self.n = len(A)
		nn = 2**(int(log(self.n, 2))+2)
		self.rangeMin = [INT_MAX] * nn
		self.rangeMax = [-INT_MAX] * nn
		self.init(A, 0, self.n-1, 1)
		gc.collect()
		
	def init(self, A, left, right, node):
		if left == right:
			self.rangeMin[node] = A[left]
			self.rangeMax[node] = A[left]
			
		else:
			mid = (left + right) / 2
			leftMin, leftMax = self.init(A, left, mid, node * 2)
			rightMin, rightMax = self.init(A, mid + 1, right, node * 2 + 1)
			self.rangeMin[node] = min(leftMin, rightMin)
			self.rangeMax[node] = max(leftMax, rightMax)
		return self.rangeMin[node], self.rangeMax[node]

	def query(self, left, right, node, nodeLeft, nodeRight):
		if right < nodeLeft or nodeRight < left:
			return INT_MAX, -INT_MAX
		if left <= nodeLeft and nodeRight <= right:
			return self.rangeMin[node], self.rangeMax[node]
		
		mid = (nodeLeft + nodeRight) / 2
		leftMin, leftMax = self.query(left, right, 2*node, nodeLeft, mid)
		rightMin, rightMax = self.query(left, right, 2*node+1, mid+1, nodeRight)
		return min(leftMin, rightMin), max(leftMax, rightMax)
	
for _ in xrange(input()):
	n, q = map(int, rl())
	A = map(int, rl())
	R = RMQ(A)
	for _ in xrange(q):
		i, j = map(int, rl())
		minVal, maxVal = R.query(i, j, 1, 0, n-1)
		print maxVal - minVal