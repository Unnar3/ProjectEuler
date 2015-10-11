# Verkefni 9 í project EULER

lim = 1000;
a = 1;
b = 1;
c = lim-b-a; 
while True:
	c = lim-b-a;
	sum = a+b+c;
	if( lim == sum and a*a+b*b==c*c ):
		break
	if( a == b ):
		b = b+1;
		a = 1;
	if( a < b ):
		a = a+1;

print "%-5s %4d" % ("a=",a)
print "%-5s %4d" % ("b=",b)
print "%-5s %4d" % ("c=",c)
print "%-5s %4d" % ("product=",a*b*c)