# Verkefni 2 í project EULER

sum = 2;
n   = [1, 2];
i   = 0;
while i < 4000000:
	i = n[0]+n[1];
	if ( i%2==0):
		sum = sum+i;
	n[0]=n[1]; n[1]=i;
print sum
