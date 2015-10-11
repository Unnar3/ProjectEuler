# Project Euler 22
# Names Scores
# Answer: 871198282

import re
from string import ascii_uppercase as al

def wordSum(word, dict):
	summ = 0
	for i in range(0, len(word)):
		summ += dict[word[i]]
	return summ

f = open('eu22.txt', 'r')
tri = re.findall(r"[\w']+", f.read())
tri = sorted(tri)
dic = {x:i for i, x in enumerate(al, 1)}

totalSum = 0
for i in range(0, len(tri)):
	totalSum += wordSum(tri[i], dic)*(i+1)

print("totalSum: ", totalSum)