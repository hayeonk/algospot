def gcd(a, b):
	return a if b == 0 else gcd(b, a%b)

def ceil(a, b):
	return (a + b - 1) / b

def solve():
	b = recipe[0]
	for i in xrange(1, n):
		b = gcd(b, recipe[i])
	a = b
	for i in xrange(n):
		a = max(a, ceil(put[i] * b, recipe[i]))
		
	ret = [r * a / b - p for r, p in zip(recipe, put)]
	return ret
	
for _ in xrange (input()):
	n = input()
	recipe = map(int, raw_input().split())
	put = map(int, raw_input().split())
	print " ".join(map(str, solve()))