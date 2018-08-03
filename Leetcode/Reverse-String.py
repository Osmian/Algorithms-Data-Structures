#Problem: 344
#Using slicing, this is a really interesting python caveat by making the step
# size -1 we go in the reverse direction
class Solution(object):
    def reverseString(self, s):
        return s[::-1]
