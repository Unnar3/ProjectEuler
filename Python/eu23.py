
def sumOfProperDivisors(n):
	sub = n
	sum = 1
	p = 2
	while p*p<=n and n>1:
		if n%p == 0:
			j = p*p
			n = n/p
			while n%p == 0:
				j = j*p
				n = n/p
			sum = sum*(j-1)
			sum = sum/(p-1)
		if p==2:
			p = 3
		else:
			p = p+2
	if n>1:
		sum = sum*(n+1)
	return sum - sub


# Find all abundant numbers
s = 28123 
abundant = [0]*s
for i in range(1, s):
	if sumOfProperDivisors(i) > i:
		abundant[i] = 1

sums = []
for i in range(0,len(abundant)):
	if abundant[i] == 1:
		for j in range(i,len(abundant)):
			if abundant[j] == 1:
				sums.append(i+j)

sum = 0
idx = 0
sums = list(set(sums))
for i in range(0, s):
	if(i != sums[idx]):
		sum += i
	else:
		idx += 1

print(abundant)
print(sums)
print(sum)