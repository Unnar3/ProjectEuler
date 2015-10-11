# Project Euler 25
# 1000-digit Fibonacci number
# Solution 4782

digits = 1000
# print(len(str(i)))

fi = [1,1]
i = 2
while len(str(fi[-1])) < digits:
	fi.append(sum(fi))
	fi.pop(0)
	i += 1

print("iterations:", i)
