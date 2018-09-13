# Problem 70
# Time Complexity O(n)
# Solution builds the answer from the bottom up,
class Solution:
    def climbStairs(self, n):
        if n==1:
            return 1
        retList = [0 for x in range(n)]
        retList[0]=1
        retList[1]=2
        for i in range(2,n):
            retList[i] = retList[i-1]+retList[i-2]
        return retList[-1]
