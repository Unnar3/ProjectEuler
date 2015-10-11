
# Project Euler number 14
# Longest Collatz sequence
# answer: 837799

print "started"
def iseven(n):
    return n % 2 == 0
    

calculated = [0]*1000001
calculated[0] = 1
calculated[1] = 1
length = [0]*1000001
i = 1000000
while i > 0:
	if calculated[i] is 1:
		i = i - 1
		continue
	j = i
	count = 0
	while j is not 1: 
		if iseven(j):
			j = j/2
		else:
			j = 3*j + 1

		count = count + 1
		if j <= 1000000:
			calculated[j] = 1
	calculated[i] = 1
	length[i] = count
	i = i - 1
	# print i
m = max(length)
print [i for i, j in enumerate(length) if j == m]
