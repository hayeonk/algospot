class TrieNode(object):
	def __init__(self, chr):
		self.chr = chr
		self.first = -1
		self.terminal = -1
		self.children = [None for i in range (26)]
	
	def insert(self, key, id):
		if self.first == -1:
			self.first = id
		if key == "":
			self.terminal = id
		else:
			next = ord(key[0]) - ord('A')
			if self.children[next] == None:
				self.children[next] = TrieNode(key[0])
			self.children[next].insert(key[1:], id)
	
	def find(self, key):
		if key == "":
			return self
		next = ord(key[0]) - ord('A')
		if self.children[next] == None:
			return None
		return self.children[next].find(key[1:])
	
	def type(self, key, id):
		if key == "":
			return 0
		if self.first == id:
			return 1
		next = ord(key[0]) - ord('A')
		return 1 + self.children[next].type(key[1:], id)
		
def countKeys(trie, word):
	node = trie.find(word)
	if node == None or node.terminal == -1:
		return len(word)
	return trie.type(word, node.terminal)
	
def readInput(n):
	input = []
	for _ in xrange(n):
		s, freq = raw_input().split()
		freq = int(freq)
		input.append((-freq, s))
	input.sort()
	
	trie = TrieNode("")
	for i in xrange(n):
		trie.insert(input[i][1], i)
	trie.first = -1
	return trie

for _ in xrange (input()):
	n, m = map(int, raw_input().split())
	trie = readInput(n)
	words = raw_input().split()
	ret = 0
	for i in xrange (m):
		ret += countKeys(trie, words[i])
	print ret + m - 1