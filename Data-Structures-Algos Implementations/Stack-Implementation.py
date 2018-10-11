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

