'''
The listnode class used to create a pointer to the head of a linked list
and from there afer we create the dependent nodes (singly-linked)
'''
class ListNode():
	def __init__(self,num):
		self.data = num   # Data Item
		self.next = None  # Point to successor


'''
Stacks support retrieval by LIFO ordering. Use stacks when retireval order does
not matter at all such as when processing batch jobs. LIFO arises usually within
recursive algorithms
'''
class Stack():
	def __init__(self):
		self.nums = []

	def push(self,x):
		self.nums.append(x)

	def pop(self):
		val = self.nums[len(self.nums)-1]
		del self.nums[len(self.nums)-1]
		return val

	def isEmpty(self):
		if(len(self.nums)==0):
			return True
		else:
			return False

	def printStack(self):
		for x in reversed(self.nums):
			print(x)


'''
Queues support retrieveal in FIFO ordering. This is the best way to control waiting 
times. You want the container holding jobs to be processed in FIFO order to minimize
the maximum time spent waiting. Note that the average waiting time will be the same
regardless of whether a FIFO or LIFO structure is used. Usually used when
ordering is important
'''
class Queue():
	def __init__(self):
		self.nums = []
	def enqueue(self,x):
		self.nums.append(x)
	def dequeue(self,x):
		val = self.nums[0]
		del self.nums[0]
		return val
	def isEmpty(self):
		if(len(self.nums)==0):
			return True
		else:
			return False
	def printQueue(self):
		for x in self.nums:
			print(x)


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
