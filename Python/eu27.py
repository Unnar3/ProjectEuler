# Project Euler 27
# Quadratic primes
# Solution: -59231

# Check if n is prime
def isPrime(n):
	if n > 4:
		if n % 2 is 0 or n % 3 is 0:
			return False
		for x in range(5, int(n**0.5)+1, 6):
			if n % x == 0 or n%(x+2) is 0:
				return False
		return True
	elif n < 4 and n > 1:
		return True
	else:
		return False

# Define the formula n^2 + a*n + b
def quadraticPrime(n,a,b):
	return n*n + a*n + b
def quadraticPrimeMinA(n,b):
	return (2-n*n-b)/n

# Precompute a set of primes upto atleast n=100, a = b = 999
primes = [2,3]
k = 1
while 6*k-1 < quadraticPrime(100,999,999):
	if isPrime(6*k-1):
		primes.append(6*k-1)
	if isPrime(6*k+1):
		primes.append(6*k+1)
	k += 1
primesSet = set(primes)
setMax = primes[-1]

# We know that it starts in n=0, thus b needs to be a prime, thus we loop through
# all the primes in the set smaller than 1000.
# The conditions for a come from n = 1 => 2 = 1*1 + 1*a + b
maxCount = 2
maxA = 0
maxB = 0
for b in primes:
	if b < 1000:
		aList = [x - 1 - b for x in primes if abs(x - 1 - b) < 1000] 
		for a in aList:
			count = 2
			for n in range(2,len(primes)):
				if(isPrime(quadraticPrime(n,a,b))):
					count += 1
				else: 
					break
			if count > maxCount:
				maxCount = count
				maxA = a
				maxB = b

print("count:", maxCount)
print("a:", maxA)
print("b:", maxB)
print("soution", maxA*maxB)
