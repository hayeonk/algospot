def get_partial_match(s):
	m = len(s)
	pi = [0 for i in range (m)]
	
	begin, matched = 1, 0
	while begin + matched < m:
		if s[begin + matched] == s[matched]:
			matched += 1
			pi[begin+matched-1] = matched
		else:
			if matched == 0:
				begin += 1
			else:
				begin += matched - pi[matched-1]
				matched = pi[matched-1]
	
	return pi

def max_overlap(a, b):
	n = len(a)
	pi = get_partial_match(b)
	begin, matched = 0, 0
	
	while begin < n:
		if matched < n and a[begin + matched] == b[matched]:
			matched += 1
			if begin + matched == n:
				return matched
		else:
			if matched == 0:
				begin += 1
			else:
				begin += matched - pi[matched-1]
				matched = pi[matched-1]
	return 0
	
for i in range (input()):
	s = raw_input()
	print 2 * len(s) - max_overlap(s, s[::-1])