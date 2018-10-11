#Given two strings, write a method to decide if one is a permutation of the other

#Permutations have the same letters just different orders
def checkPerm(a,b):

	if(len(a)!=len(b)):
		return False

	a = list(a)
	a.sort()
	b = list(b)
	b.sort()

	return(a==b)


def checkPerm2(a,b):
	if(len(a)!=len(b)):
		return False

	uniquesA = set(a)
	uniquesB = set(b)
	if(uniquesA!=uniquesB):
		return False

	for char in uniquesA:
		if(a.count(char) != b.count(char)):
			return False
	return True

print(checkPerm2('heskkkfx','heskkkdfx'))
