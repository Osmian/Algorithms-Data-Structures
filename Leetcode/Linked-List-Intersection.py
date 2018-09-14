# Really interesting solution because the only valid way to exit
# the loop is if they are equal

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        pointA = headA
        pointB = headB

        while pointA is not pointB:
            pointA = headB if pointA is None else pointA.next
            pointB = headA if pointB is None else pointB.next
        return pointA
