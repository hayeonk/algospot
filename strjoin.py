import heapq

for _ in xrange(input()):
	n = input()
	pq = map(int, raw_input().split())
	heapq.heapify(pq)
	ret = 0
	
	while len(pq) > 1:
		min1 = heapq.heappop(pq)
		min2 = heapq.heappop(pq)
		heapq.heappush(pq, min1 + min2)
		ret += min1 + min2
	print ret