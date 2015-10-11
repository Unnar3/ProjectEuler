# Verkefni 3 í project EULER
import math

def isprime(n):
	# Athugum hvort talan n sé prime
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

tala = raw_input('Choose Number')
tala = int(tala)
i = 1;
while( i != tala/2 ):
	if( tala%i==0): 
		if( isprime(tala/i) ):
			print(tala/i);
			break;
	i=i+1;