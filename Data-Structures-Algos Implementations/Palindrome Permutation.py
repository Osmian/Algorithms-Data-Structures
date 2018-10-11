#Palindrome Permutation:
# Given a string write a function to check if it is a permutation of a palindrome


#My solution based on the length of the input
def paliperm(a):
	a = ''.join(a.split()).lower()
	a = list(a)

	if(len(a)%2==0):
		for elem in set(a):
			if(a.count(elem)%2!=0):
				return False
		return True
	else:
		thresh = 0
		for elem in set(a):
			if(a.count(elem)%2!=0):
				thresh +=1
				if(thresh>1):
					return False
		return True

#Solution 2: Using a character frequency dictionary 
# Iterate over the values for each key and if there is an even number of odd occurences return false
def paliperm2(a):
	#Modifying the original input so we can parse
	a = ''.join(a.split()).lower()
	charFrequencies = {}
	#Filling up the dictionary
	for elem in set(a):
		charFrequencies[elem] = a.count(elem)

	#Our variable for detecting occurences
	foundOdd = False
	#Iterating through the dictionary items
	for k,v in charFrequencies.items():
		if v%2!=0:
			#Odd Occurences = True
			#Even Occurences = False
			foundOdd = not foundOdd

	return(foundOdd)

#Most Efficeint Solution
def paliperm3(a):
	a = ''.join(a.split()).lower()
	bitvec = [True for x in range(26)]


print(paliperm2('Tact Ccoa'))

