# Project Euler number 16
# Power digit sum
# answer: 1366

def round_down(num, divisor):
    return num - (num%divisor)

a = 2**1000
i = 1

while i < a:
	i = i*10

sum = 0
tmp = 0
count = 0
while i > 0:
	tmp = round_down(a,i)
	print tmp/i
	sum = sum + tmp/i
	a = a - tmp
	i = i / 10
	count = count + 1
print "sum: ", sum 
