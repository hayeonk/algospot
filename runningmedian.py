import heapq

class RNG(object):
	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.seed = 1983
		
	def getNext(self):
		ret = self.seed
		self.seed = ((ret * self.a) + self.b) % 20090711
		return ret
		
for _ in xrange (input()):
	n, a, b = map(int, raw_input().split())
	rng = RNG(a, b)
	ret = 0
	minheap = []
	maxheap = []
	
	for i in range (n):
		if len(maxheap) == len(minheap):
			heapq.heappush(maxheap, -rng.getNext())
		else:
			heapq.heappush(minheap, rng.getNext())
		
		if maxheap and minheap and minheap[0] < -maxheap[0]:
			a = heapq.heappop(minheap)
			b = -heapq.heappop(maxheap)
			
			heapq.heappush(maxheap, -a)
			heapq.heappush(minheap, b)
			
		ret = (ret - maxheap[0]) % 20090711
	
	print ret