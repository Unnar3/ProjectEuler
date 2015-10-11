# Verkefni 5 í project EULER

squaresum = 0;
sum       = 0;
sumsquare = 0;

for i in range(1,101):
	sum       = sum+i;
	sumsquare = sumsquare+(i*i);

squaresum = sum*sum;

diff = squaresum-sumsquare;
print diff