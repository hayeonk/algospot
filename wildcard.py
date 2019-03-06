def match(w, s):
	ret = m[w][s]
	if ret != -1:
		return ret
	
	if s < len(S) and w < len(W) and (W[w] == "?" or W[w] == S[s]):
		m[w][s] = match(w+1, s+1)
		return m[w][s]
	
	if w == len(W):
		m[w][s] = (s == len(S))
		return m[w][s]
		
	if W[w] == "*":
		if match(w+1, s) or (s < len(S) and match(w, s+1)):
			m[w][s] = 1
			return m[w][s]
	return 0

for _ in xrange (input()):
	W = raw_input()
	Slist = [raw_input() for i in xrange (input())]
	result = []
	for S in Slist:
		m = [[-1] * 101 for j in xrange (101)]
		if match(0, 0): 
			result.append(S)
	result.sort()
	for r in result:
		print r