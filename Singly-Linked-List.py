'''
The listnode class used to create a pointer to the head of a linked list
and from there afer we create the dependent nodes (singly-linked)
'''
class ListNode():
	def __init__(self,num):
		self.data = num   # Data Item
		self.next = None  # Point to successor