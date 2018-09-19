import sys
A = [1,4,100,212,-1,2]


def find_max_diff(nums):
    maxi = -sys.maxsize-1
    mini = sys.maxsize
    
    for i in nums:
        if i> maxi:
            maxi = i
        if i<mini:
            mini = i
    print(maxi,mini)

find_max_diff(A)
