# Project Euler 29
# Distinct powers
# Solution 9183

size = 100
print("solution:", len(set([a**b for a in range(2,size+1) for b in range(2,size+1)])))

