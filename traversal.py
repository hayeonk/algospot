def print_post_order(preorder, inorder):
	n = len(preorder)
	
	if n == 0:
		return []
	
	root = preorder[0]
	L = inorder.index(root)
	
	left = print_post_order(preorder[1:L+1], inorder[:L])
	right = print_post_order(preorder[L+1:], inorder[L+1:])

	return left + right + [root]

for i in range (input()):
	n = input()
	preorder = map(int, raw_input().split())
	inorder = map(int, raw_input().split())
	print " ".join(map(str, print_post_order(preorder, inorder)))