from operator import itemgetter

class Node(object):
	def __init__(self, x, y, r):
		self.x, self.y, self.r = x, y, r
		self.child = []
	
	def contain(self, n):
		return (self.x - n.x) ** 2 + (self.y - n.y) ** 2 < (self.r - n.r) ** 2
		
	def addChild(self, n):
		for c in self.child:
			if c.contain(n):
				c.addChild(n)
				return
		self.child.append(n)
		
	def height(self):
		heights = []
		for i in self.child:
			heights.append(i.height())
			
		if not heights:
			return 0
			
		heights.sort(reverse=True)
		if len(heights) >= 2:
			global longest
			longest = max(longest, 2 + heights[0] + heights[1])
		
		return heights[0]+1
	

for i in xrange(input()):
	n = input()
	inputs = [map(int, raw_input().split()) for _ in xrange(n)]
	inputs.sort(key=itemgetter(2), reverse=True)
	
	nodes = [Node(i[0], i[1], i[2]) for i in inputs]
	root = nodes.pop(0)
	for node in nodes:
		root.addChild(node)
	longest = 0
	h = root.height()
	print max(longest, h)