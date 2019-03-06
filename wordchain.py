def makeGraph(words):
	for i in range (n):
		a = ord(words[i][0]) - ord('a')
		b = ord(words[i][-1]) - ord('a')
		graph[a][b].append(words[i])
		adj[a][b] += 1
		outdegree[a] += 1
		indegree[b] += 1
	
def checkEuler():
	plus1, minus1 = 0, 0
	for i in range (26):
		delta = outdegree[i] - indegree[i]
		if delta < -1 or delta > 1:	
			return False
		if delta == 1:
			plus1 += 1
		if delta == -1:
			minus1 += 1
	return (plus1 == 1 and minus1 == 1) or (plus1 == 0 and minus1 == 0)

def getEulerCircuit(here):
	for there in range (26):
		while adj[here][there] > 0:
			adj[here][there] -= 1
			outdegree[here] -= 1
			getEulerCircuit(there)
	circuit.append(here)
	
def getEulerTrailOrCircuit():
	for i in range (26):
		if outdegree[i] == indegree[i] + 1:
			getEulerCircuit(i)
			return
			
	for i in range (26):
		if outdegree[i]:
			getEulerCircuit(i)

for _ in xrange (input()):
	n = input()
	words = []
	for i in xrange (n):
		words.append(raw_input())
	
	adj = [[0 for i in range (26)] for j in range (26)]
	graph = [[[] for i in range (26)] for j in range (26)]
	indegree = [0 for i in range (26)]
	outdegree = [0 for j in range (26)]
	
	makeGraph(words)
	if not checkEuler():
		print "IMPOSSIBLE"
		continue
		
	circuit = []
	getEulerTrailOrCircuit()
	if len(circuit) != n + 1:
		print circuit
		continue
		
	circuit.reverse()
	ret = []
	for i in range (1, n+1):
		a = circuit[i-1]
		b = circuit[i]
		ret.append(graph[a][b].pop())
	print " ".join(ret)
	