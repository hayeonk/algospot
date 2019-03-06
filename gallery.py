def dfs(here):
	visited[here] = True
	children = [0, 0, 0]
	for i in range (len(adj[here])):
		there = adj[here][i]
		if not visited[there]:
			children[dfs(there)] += 1
	
	if children[UNWATCHED]:
		global installed
		installed += 1
		return INSTALLED
	
	if children[INSTALLED]:
		return WATCHED
	return UNWATCHED

for _ in xrange (input()):
	V, E = map(int, raw_input().split())
	adj = [[] for i in range (V)]
	visited = [False for i in range (V)]
	UNWATCHED = 0
	WATCHED = 1
	INSTALLED = 2
	installed = 0
	for i in range (E):
		u, v = map(int, raw_input().split())
		adj[u].append(v)
		adj[v].append(u)
	for u in range (V):
		if not visited[u] and dfs(u) == UNWATCHED:
			installed += 1
	print installed