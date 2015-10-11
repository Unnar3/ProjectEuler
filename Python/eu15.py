# Project Euler number 15
# Lattice paths
# answer: 137846528820

import numpy as np

matSize = 20
mat = np.zeros(shape=(matSize+1,matSize+1))

for i in range(0, matSize+1):
	for j in range(0, matSize+1):
		# Check if we are on the boundary
		if i is 0 and j is 0:
			mat[i][j] = 0
		elif i is 0:
			mat[i][j] = 1
		elif j is 0:
			mat[i][j] = 1
		else:
			mat[i][j] = mat[i-1][j] + mat[i][j-1]

print mat[matSize][matSize]