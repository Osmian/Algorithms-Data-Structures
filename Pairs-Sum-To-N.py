# def find_pairs(nums,target):
    uniques = set(nums)
    pairs = []

    for i in nums:
        tmp = target-i
        if tmp in uniques:
            pairs.append([str(i),str(tmp)])

    print(pairs)
def find_missing_num(arr):
    








A = [1,2,3,4,5,7,8]
N = 6
find_pairs(A,N)
