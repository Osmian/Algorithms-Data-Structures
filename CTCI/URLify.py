#URLify: Replace all whitespaces with %20


#Solution 1 using the replace method ~ O(n)
def urlify(a):
	a = a.replace(' ','%20')


#Solution 2 by converting to list and replacing indices ' ' with '%20' then joining back
def urlify2(a):
	a = list(a)
	for x in a:
		if(x==' '):
			a[a.index(x)] = '%20'
	a = ''.join(a)

urlify2('  ')