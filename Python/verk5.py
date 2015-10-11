# Verkefni 5 í project EULER

bil = int(raw_input('Choose highest number'));
mid = bil/2;
jump = bil*(bil-1);
pruf = jump;
i=2;
while( i<mid ): 
	if( pruf%(bil-i)!=0):
		pruf = pruf+jump;
		i=2;
	else :
		i=i+1;
print pruf
		