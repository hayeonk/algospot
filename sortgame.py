import Queue

def precalc(n):
	perm = "01234567"[:n]
	q = Queue.Queue()
	q.put(perm)
	toSort[perm] = 0
	while not q.empty():
		here = q.get()
		cost = toSort[here]
		for i in range (n):
			for j in range (i+1, n+1):
				here = here[:i] + here[i:j][::-1] + here[j:]
				if here not in toSort:
					toSort[here] = cost + 1
					q.put(here)
				here = here[:i] + here[i:j][::-1] + here[j:]
	
def convertListToString(perm):
	sorted_list = [x for x in perm]
	ret = []
	sorted_list.sort()
	
	for i in perm:
		ret.append(sorted_list.index(i))
	return "".join(map(str, ret))
	
fixed_list = []
precalc_set = set()
for _ in xrange (input()):
	n = input()
	perm = map(int, raw_input().split())
	fixed = convertListToString(perm)
	fixed_list.append(fixed)
	precalc_set.add(len(fixed))

toSort = {}
for i in precalc_set:
	precalc(i)

for fixed in fixed_list:
	print toSort[fixed]