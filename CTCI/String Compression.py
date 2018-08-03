#String Compression:
# Use the counts of repeated characters to create a compressed string. 
# If the compressed string would not become smaller than the original string, return original

def compress(s):

	frequencies = {k:s.count(k) for k in set(s)}
	# print(frequencies)
	if(len(set(s))*2>len(s)):
		return s
	else:
		compString = list()
		for char in set(s):
			compString.append(char)
			compString.append(str(frequencies[char]))
		return(''.join(compString))
	

print(compress('akcc'))
