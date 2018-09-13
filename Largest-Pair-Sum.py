# Given an unsorted of distinct integers, find the largest pair sum in it.
# Time complexity = O(n) because it is done in one-pass



l = [1,20,2,4353,231,214,411,12,4001,5,6,7,223,8,3,33]
l2=[1000,2,3,401,234,123,2000]

def find_largest_sum(arr):

    #Bounds check
    if(len(arr)<2):
        return 0

    #Setting up our initial conditions
    first_largest = max(arr[0],arr[1])
    second_largest = min(arr[0],arr[1])


    for num in arr[2:]:
        if num>first_largest:
            second_largest = first_largest
            first_largest = num

        elif num<first_largest and num>second_largest:
            second_largest = num
    return(first_largest+second_largest)

print(find_largest_sum(l2))
