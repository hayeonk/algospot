def calcOverlap():
	for i in range (k):
		for j in range (k):
			overlap[i][j] = is_overlap(words[i], words[j])

def is_overlap(a, b):
	cnt = 0
	for i in range(1, 1 + min(len(a), len(b))):
		if a[-i:] == b[:i]:
			cnt = i
	return cnt
	
def restore(last, used):
	if used == (1<<k)-1:
		return 0
	if m[last][used] != -1:
		return m[last][used]
	ret = 0
	for next in range (k):
		if (used & (1<<next)) == 0:
			cand = overlap[last][next] + restore(next, used + (1<<next))
			ret = max(ret, cand)
	m[last][used] = ret
	return ret
	
def reconstruct(last, used):
	if used == (1<<k)-1:
		return ""
	for next in range (k):
		if (used & (1<<next)):
			continue
		ifUsed = restore(next, used + (1<<next)) + overlap[last][next]
		if restore(last, used) == ifUsed:
			return words[next][overlap[last][next]:] + reconstruct(next, used + (1<<next))

for _ in xrange (input()):
	k = input()
	word = [raw_input().strip() for _ in xrange (k)]
	words = []
	
	for i in range (k):
		skip = False
		for j in range (k):
			if i != j and word[i] in word[j]:
				skip = True
		if not skip:
			words.append(word[i])
			
	k = len(words)
	overlap = [[0] * k for _ in xrange (k)]
	m = [[-1] * (1<<k) for _ in xrange (k)]
	calcOverlap()
	
	maxVal = 0
	first = 0
	for i in xrange (k):
		if restore(i, (1<<i)) > maxVal:
			maxVal = restore(i, (1<<i))
			first = i
	print words[first] + reconstruct(first, (1<<first))