'''
Data structure supporting fast search and flexible update. A rooted binary tree is 
recursively defined as either being empty, or consisting of a node called the root 
with left and right subtrees.

left-subtree <=root
right-suntree >=root

Basic Operations Supported, searching, traversal, insertion, deletion
'''
class TreeNode():
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None 

#Pre-Order traversale printing
def print_tree(root):
	if not root:
		return 
	print(root.data)
	print_tree(root.left)
	print_tree(root.right)


def search_tree(root,target):
	if(not root):
		return None
	if(root.data == target):
		return root.data
	if(root.data<target):
		search_tree(root.right,target)
	else:
		search_tree(root.left,target)

root = TreeNode(10)
root.left = TreeNode(23)
root.right = TreeNode(100)
print(search_tree(root,23))
