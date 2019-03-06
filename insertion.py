for _ in range (input()):
	n = input()
	shifted = map(int, raw_input().split())
	candidates = range (1, n+1)
	original = []
	
	for i in reversed(range(n)):
		larger = shifted[i]
		original.append(candidates[i - larger])
		del candidates[i - larger]
	original.reverse()
	print " ".join(map(str, original))