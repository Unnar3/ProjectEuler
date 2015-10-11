# Verkefni 10 í project EULER
import time
s = time.time()
def maxrow(matrix, lengthrow, lengthcol, lengthsum):
		i=0; j=0; rowm = 1; row = []; rowmax = [];
		while i!=lengthrow:
			while j<=lengthcol-lengthsum:
				rowm=(matrix[i][j]);
				for k in range(j,j+lengthsum-1):
					rowm=rowm*matrix[i][k];
				j = j+1;
				row.append(rowm)
			rowmax.append(max(row));
			i = i+1;
			j = 0
			rowm = 1;
		return max(rowmax);

def maxcol(matrix, lengthrow, lengthcol, lengthsum):
		i=0; j=0; colm = 1; col = []; colmax = [];
		while j!=lengthcol:
			while i<=lengthrow-lengthsum:
				colm=(matrix[i][j]);
				for k in range(i+1,i+lengthsum):
					colm=colm*matrix[k][j];
				i = i+1;
				col.append(colm)
			colmax.append(max(col));
			j = j+1;
			i = 0
			colm = 1;
		return max(colmax);
		
def maxdia(matrix, lengthrow, lengthcol, lengthsum):
		i=0; j=0; 
		rowm = 1; row = []; rowmax = [];
		colm = 1; col = []; colmax = [];
		while i!=lengthrow:
			while j!=lengthcol:
				rowm = matrix[i][j];
				rowc = matrix[i][j];
				if j<=lengthcol-lengthsum and i<=lengthrow-lengthsum:
					for k in range(1,lengthsum):
						rowm = rowm * matrix[i+k][j+k];
				if j>lengthsum-1 and i<=lengthrow-lengthsum:
					for k in range(1,lengthsum):
						rowc = rowc * matrix[i+k][j-k];
						print k
				j = j+1;
				row.append(rowm)
				col.append(rowc)
			rowmax.append(max(row));
			colmax.append(max(col));
			i = i+1;
			j = 0
			rowm = 1;
			rowc = 1;
		maxall = [max(rowmax),max(colmax)];
		print (max(rowmax),max(colmax))
		return max(maxall)
		
f = file("verk10.txt", "r")
data = [line.split() for line in f]
f.close()
x = [[int(column) for column in row] for row in data]
lrow = len(data[0][:]);
lcol = len(data[:][0]);
lsum=4;
t1 = maxrow(x,lrow,lcol,lsum);
t2 = maxcol(x,lrow,lcol,lsum);
t3 = maxdia(x,lrow,lcol,lsum);
t  = [t1,t2,t3];
print max(t)
print time.time() -s 