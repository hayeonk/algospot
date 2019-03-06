def countPairings(taken):
	firstFree = -1
	
	for i in range (n):
		if not taken[i]:
			firstFree = i
			break
			
	if firstFree == -1:
		return 1
		
	ret = 0
	for pairWith in range (firstFree + 1, n):
		if not taken[pairWith] and areFriends[firstFree][pairWith]:
			taken[firstFree], taken[pairWith] = True, True
			ret += countPairings(taken)
			taken[firstFree], taken[pairWith] = False, False
	return ret

for _ in xrange (input()):
	n, m = map(int, raw_input().split())
	A = map(int, raw_input().split())
	areFriends = [[False for i in range (n)] for j in range (n)]
	
	for i in xrange (0, 2*m, 2):
		areFriends[A[i]][A[i+1]] = True
		areFriends[A[i+1]][A[i]] = True
	
	taken = [False] * n
	print countPairings(taken)