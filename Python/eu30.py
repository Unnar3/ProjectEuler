# Project Euler 30
# Digit fifth powers
# Slution: 443839


fifthPower = [x**5 for x in  range(0,10)]
def sumPowers(number):
	sum = 0
	while number:
		sum += fifthPower[number % 10]
		number //= 10
	return sum

i = 0
while 10**i-1 <= i*fifthPower[-1]:
	i += 1

# maximum number letters  then i-1
max = 10**(i)
number = 1634
count = 0
sumOfDigits = []
for i in range(10, max):
	if i == sumPowers(i):
		sumOfDigits.append(i)

print("list:", sumOfDigits)
print("sum: ",sum(sumOfDigits))