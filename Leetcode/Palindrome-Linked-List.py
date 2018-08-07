#Problem: 234
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
    
# Solution 1
        s1 = []
        s2 = []
        curr = head
        prev = None
        nxt = head
        while(head):
            nxt = head.next
            s1.append(head.val)
            head.next = prev
            prev = head
            head = nxt
        head = prev
        while(head):
            s2.append(head.val)
            head = head.next
        return s1==s2

# Solution 2 (More Optimized)
# Finding middle node and reversing then comparing
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
