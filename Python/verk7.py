# Verkefni 5 í project EULER
import time

limit = int( raw_input('Choose Prime Number'));
s = time.time()
def isprime(n):
	# Athugum hvort talan n sé prime
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

i = 3;
n = 1;
while n!=limit :
	if( isprime(i) ):
		n=n+1;
	i=i+2;
print i-2
print time.time() -s 