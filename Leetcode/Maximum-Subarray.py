'''
Problem: 53
Using Kadanes Algorithm we only need to keep track of the maximum sum for
Each ending index through the array and return the maximum
'''

class Solution(object):
    def maxSubArray(self, nums):

        if not nums:
            return 0

        currMax = totalMax = nums[0]
        for x in nums[1:]:
            currMax = max(x,currMax + x)
            totalMax = max(currMax,totalMax)
        return totalMax
