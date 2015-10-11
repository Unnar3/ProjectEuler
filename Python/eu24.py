# Project Euler 24
# Lexicographic permutations
# Solution: 2783915604

iteration = 1000001

def swapList(L,a,b):
	tmp = L[a+b]
	L[a+1:a+b+1] = L[a:a+b]
	L[a] = tmp
	# L[a], L[b] = L[b], L[a]
	return L

l = [0,1,2,3,4,5,6,7,8,9]
cp = [1]*len(l)
for i in range(2,len(l)+1):
	cp[i-1] = i*cp[i-2]
print(cp)

# Find index of swappable
firstPart = []


goal = iteration-1
doMath = True
if goal > cp[-1]:
	print("not enough variables")
	doMath = False
	
if doMath:
	while goal > 0:
		if int(goal) is 1:
			# Special case
			l = swapList(l,len(l)-2,1)
			print("swapped", l)
			goal = 0

		else:
			swaIdx = next(x[0] for x in enumerate(cp) if x[1] > goal)
			# print("swaIdx:", swaIdx)
			swaVal = cp[swaIdx]

			# Find increment for each swap 
			inc = swaVal / len(l)
			swaNum = int(goal // inc)
			l = swapList(l,len(l)-swaIdx-1,int(swaNum))
			goal = goal - swaNum*inc
			firstPart.append(l[len(l)-swaIdx-1])
			l = l[len(l)-swaIdx:len(l)]

	firstPart.extend(l)
	print("solution:", ''.join([ "%d"%x for x in firstPart]))