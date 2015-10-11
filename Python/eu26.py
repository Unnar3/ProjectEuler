# Project Euler 26
# Reciprocal cycles
# Solution 983

import math
from time import sleep

# Uses long division and checks for repeating remainder
# if a repeating remainder is found the distance between them is return
# 0 is return ir the remainder becomes 0 since the numerator is 1
def repeating_digits(number):
	numbers = []
	digits = []
	numerator = 1
	while numerator < number:
		numerator *= 10

	while numerator not in digits:
		digits.append(numerator)
		numbers.append(numerator//number)
		numerator -= (numerator//number) * number

		if numerator is 0:
			break

		while numerator < number:
			numerator *= 10
	
	return 0 if numerator == 0 else len(digits)-digits.index(numerator)

length = 0
idx = 0
for i in range(2,1000):
	tmp = repeating_digits(i)
	if tmp > length:
		length = tmp
		idx = i 

print(idx)