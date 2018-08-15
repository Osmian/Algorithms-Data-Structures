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

