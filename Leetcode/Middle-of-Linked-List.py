#Problem 876, O(n)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#The method here is to have to iterators over the linked List
#One increments at twice the rate of the other and we return the
#Slower one
class Solution(object):
    def middleNode(self, head):
        curr = head
        while(curr and curr.next):
            head = head.next
            curr = curr.next.next
        return head
