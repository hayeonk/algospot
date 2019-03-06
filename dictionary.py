def makeGraph(words):
	adj = [[0 for i in range (26)] for j in range (26)]
	for j in range (1, N):
		i = j - 1
		length = min(len(words[i]), len(words[j]))
		
		for k in range (length):
			if words[i][k] != words[j][k]:
				a = ord(words[i][k]) - ord('a')
				b = ord(words[j][k]) - ord('a')
				adj[a][b] = 1
				break
	return adj
	
def dfs(here):
	seen[here] = 1
	for there in range (26):
		if adj[here][there] and not seen[there]:
			dfs(there)
	order.append(here)

def topologicalSort():
	for i in range (26):
		if not seen[i]:
			dfs(i)
	order.reverse()
	for i in range (26):
		for j in range (i+1, 26):
			if adj[order[j]][order[i]]:
				return "INVALID HYPOTHESIS"
	return "".join(map(lambda x: chr(x + ord('a')), order))
	
for _ in xrange (input()):
	N = input()
	words = []
	for _ in xrange (N):
		words.append(raw_input())
	
	adj = makeGraph(words)
	seen = [0 for i in range (26)]
	order = []
	print topologicalSort()