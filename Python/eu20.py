# Project Euler number 16
# Factorial digit sum
# answer: 648


import math

def range_factorial(low,high):
    if low+1 < high:
        mid = (high+low)//2
        return range_factorial(low,mid) * range_factorial(mid+1,high)
    if low == high:
        return low
    return low*high

def factorial(n):
    if n < 2:
        return 1
    return range_factorial(1,n)

n = 100

fac = factorial(n)
sum = 0
for i in str(fac):
	sum += int(i)

print "sum of digits: ", sum