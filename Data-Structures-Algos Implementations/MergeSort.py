#Implementing Merge Sort in python

def mergeSort(unsortedList):
	if(len(unsortedList)<=1):
		return unsortedList
	mid = len(unsortedList)//2
	left = unsortedList[:mid]
	right = unsortedList[mid:]


	left = mergeSort(left)
	right = mergeSort(right)
	return list(merge(left,right))

def merge(left,right):
	retList = []
	while(len(left)!=0 and len(right)!= 0):
		if(left[0] < right[0]):
			retList.append(left[0])
			del left[0]
		else:
			retList.append(right[0])
			del right[0]
	if len(left)==0:
		retList = retList+right
	else:
		retList = retList+left
	return retList

print(mergeSort([5,32,1,43,8,4,7645,7,45232,5332,35643,322]))
