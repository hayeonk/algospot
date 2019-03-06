import sys

def pack(c, i):
	if i == n:
		return 0
		
	if m[c][i] != -1:
		return m[c][i]
		
	ret = pack(c, i + 1)
	if c >= volume[i]:
		ret = max(ret, pack(c - volume[i], i + 1) + need[i])
	m[c][i] = ret
	return ret

def reconstruct(c, i):
	if i == n:
		return
	if pack(c, i) == pack(c, i + 1):
		reconstruct(c, i + 1)
	else:
		picked.append(names[i])
		reconstruct(c - volume[i], i + 1)

rl = lambda: sys.stdin.readline()
for _ in xrange (input()):
	n, c = map(int, rl().split())
	names = []
	volume = []
	need = []
	m = [[-1] * (n + 1) for _ in xrange (c + 1)]
	for _ in xrange (n):
		name, v, ne = rl().split()
		names.append(name)
		volume.append(int(v))
		need.append(int(ne))
	picked = []	
	maxVal = pack(c, 0)
	reconstruct(c, 0)
	print maxVal, len(picked)
	for item in picked:
		print item