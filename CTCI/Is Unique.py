#CTCI:1.1 
#Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures


#Solution 1 with a set
def isUnique(a):
	#I am making the assumption that lowercase and uppercase are the same char
	a = ''.join(a.split()).lower()
	uniques = set(a)
	return(len(uniques)==len(a))

#Solution 2 by iterating through and setting the index of each char in the set to True
#As soon as we run into a false we know that it contains duplicates
def isUnique2(a):
	letters = {}
	for char in a:
		if(char in letters):
			return False
		else:
			letters[char]=True
		return True

print(isUnique2('Hhelo'))