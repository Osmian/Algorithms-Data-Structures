# Zero Matrix: Write an algorithm such that if an element 
# in an MxN matrix is 0, its entire row and column are set to zero 

def zeroMatrix(matrix):
	for row in matrix:
		print(row)
	print('\n')
	row = [False for x in range(len(matrix))]
	col = [False for x in range(len(matrix[0]))]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if(matrix[i][j]==0):
				row[i]=True
				col[j]=True

	for i in range(len(row)):
		if(row[i]):
			nullifyRow(matrix,i)


	for i in range(len(col)):
		if(col[i]):
			nullifyCol(matrix,i)

	return matrix

def nullifyRow(matrix,row):
	for j in range(len(matrix[0])):
		matrix[row][j]=0

def nullifyCol(matrix,col):
	for i in range(len(matrix)):
		matrix[i][col] = 0



	
				


new_matrix = zeroMatrix([[0,2,3],[4,5,6],[7,8,9]])
for row in new_matrix:
	print(row)