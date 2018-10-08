# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        nums = []
        self.inorder(root,nums)
        
        
        # Checking the constraints of a BST
        if(len(set(nums))==len(nums) and nums == sorted(nums)):
            return True
        else:
            return False
        
    

    # Doing a recursive in-order traversal of the tree    
    def inorder(self,root,nums):
        if not root:
            return
        else:
            self.inorder(root.left,nums)
            nums.append(root.val)
            self.inorder(root.right,nums)
        
        