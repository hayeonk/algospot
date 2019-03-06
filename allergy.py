import sys

def search(edible, chosen):
	global best
	if chosen >= best:
		return
	
	first = 0
	while first < n and edible[first]:
		first += 1
	if first == n:
		best = min(best, chosen)
		return
	
	for i in range (len(canEat[first])):
		food = canEat[first][i]
		for j in range (len(eaters[food])):
			edible[eaters[food][j]] += 1
		search(edible, chosen + 1)
		for j in range (len(eaters[food])):
			edible[eaters[food][j]] -= 1

rl = lambda: sys.stdin.readline()
for _ in xrange (input()):
	n, m = map(int, rl().split())
	friends = rl().split()
	eaters = [[friends.index(x) for x in rl().split()[1:]] for _ in xrange (m)]
	edible = [0] * n
	canEat = [[] for _ in xrange (n)]
	best = 987654321
	for i, friend in enumerate(eaters):
		for f in friend:
			canEat[f].append(i)
	search(edible, 0)
	print best