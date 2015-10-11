# Project Euler 28
# Number spiral diagonals
# Solution 669171001


size = 1001

# First circle a special case with only 1 number on the diagonal
# Allother circles have four
def sumCornerCircles(width):
	if width is 1:
		return 1
	return 4*width**2 - 6*(width-1)

print("sum: ", sum([sumCornerCircles(x) for x in range(1, size+1, 2)] ))