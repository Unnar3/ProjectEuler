import math
import numpy as np

f = open('eu18.txt', 'r')
# f.readline()

# add txt to list of lists
tri = [[int(x) for x in line.split()] for line in f]

for t in tri:
	print t

tri_sum = [[0 for x in i] for i in tri]



for i in range(0, len(tri)):
	for j in range(0, len(tri[i])):
		if i is 0:
			tri_sum[i][j] = tri[i][j]
		elif j is 0:
			tri_sum[i][j] = tri[i][j] + tri_sum[i-1][j]
		elif j is i: 
			tri_sum[i][j] = tri[i][j] + tri_sum[i-1][j-1]
		else:
			tri_sum[i][j] = tri[i][j] + max(tri_sum[i-1][j-1], tri_sum[i-1][j])


print "max: ", max(tri_sum[-1])