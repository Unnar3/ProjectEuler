# Project Euler 21
# Amicable numbers
# Answer: 31626

max = 10000

# naive and bad way to calculate this
def proper_divisors_sum(number):
	if(number%2==0):
		return sum([x for x in range(1, number // 2 + 1) if number % x == 0])
	else:
		return sum([x for x in range(1, number // 3 + 1) if number % x == 0])

vec = [0]*10000
amicable_sum = 0
for i in range(3,len(vec)):
	if(vec[i] == 0):
		n = proper_divisors_sum(i)
		if(i == proper_divisors_sum(n) and i!=n):
			# Have a amicable pair, add to sum if in range
			vec[i] = 1
			amicable_sum += i
			print("i: ", i)
			if(n < 10000):
				vec[n] = 1
				amicable_sum += n
				print("n: ", n)	


print("sum: ", amicable_sum)