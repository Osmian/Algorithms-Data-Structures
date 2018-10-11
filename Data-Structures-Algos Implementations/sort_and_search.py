# Implementing Merge Sort and Binary Search in python to sort a list and find the value in the list
# Merge Sort has a time complexity of O(nlogn)
# Binary Search has a time complexity of O(log n)
# Combining these two in one program to find an element in an unsorted array is O(nlogn)



def mergeSort(unsorted):
	if(len(unsorted)>1):
		mid = len(unsorted)//2
		left = unsorted[:mid]
		right = unsorted[mid:]


		mergeSort(left)
		mergeSort(right)

		i = 0
		j = 0
		k = 0

		while i<len(left) and j<len(right):
			if(left[i]<right[j]):
				unsorted[k] = left[i]
				i+=1
			else:
				unsorted[k] = right[j]
				j+=1
			k+=1
		while i<len(left):
			unsorted[k] = left[i]
			i+=1
			k+=1
		while j<len(right):
			unsorted[k] = right[j]
			j+=1
			k+=1
	return unsorted


def binSearch(alist,target):
	
	first = 0
	last = len(alist)-1
	found = False

	while first<=last and not found:
		midpoint = (first+last)//2
		if alist[midpoint]==target:
			found = True
		else:
			if target<alist[midpoint]:
				last = midpoint-1
			else:
				first = midpoint+1
	return found

orig_list = [54,26,93,17,77,31,44,55,20]
new_list = mergeSort(orig_list)
print(binSearch(new_list,17))



