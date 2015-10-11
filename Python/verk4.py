# Verkefni 4 í project EULER

count = int(raw_input('Chose the digit count'));
a = 10**count-1;
b = 10**count-1;
max = 1;

while (a*b > max and a>=10**(count-1)):
	while (a*b > max and b>=10**(count-1)):
		tala  = str( a * b );       
		talab = int( tala[::-1] ); 
		if( int(tala) == talab and talab > max):
			max = talab;
			break
		b = b-1;
	a=a-1; b=a;
	
print "%-5s %4d" % ("max=",max)