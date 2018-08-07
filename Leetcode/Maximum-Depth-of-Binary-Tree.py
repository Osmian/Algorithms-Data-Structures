# Problem 104
# Recursively adding one for each level traversed

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
