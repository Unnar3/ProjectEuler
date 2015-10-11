
wordsw = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelfe", "thirteen", "fourteen", "fifteen", "sixteen", 
	"seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "and"]
words = [len(word) for word in wordsw]
dividorsw = ["hundred", "thousand"]
dividors = [len(word) for word in dividorsw]

def round_down(num, divisor):
    return num - (num%divisor)

count = 0
wordsl = []
c = 190
# for maxNumber in range(c, c+1):
for maxNumber in range(1, 1001):
	# divide by thousund
	isand = True
	if maxNumber >= 1000:
		isand = False
		a = round_down(maxNumber, 1000)
		count += words[a/1000-1] + dividors[1] 
		# wordsl.append(wordsw[a/1000-1])
		wordsl.append(dividorsw[1])
		maxNumber -= a

	if maxNumber >= 100:
		isand = False
		a = round_down(maxNumber, 100)
		count += words[a/100-1] + dividors[0] 
		# wordsl.append(wordsw[a/100-1])
		wordsl.append(dividorsw[0])
		maxNumber -= a
	if maxNumber >= 20:
		if not isand:
			count += words[-1]
			# wordsl.append(wordsw[-1])
			isand = True
		a = round_down(maxNumber, 10)
		count += words[a/10+20-3] 
		# wordsl.append(wordsw[a/10+20-3])
		if a >= 20:
			maxNumber -= a
		else:
			maxNumber = 0
	if maxNumber > 0:
		if not isand:
			count += words[-1]
			# wordsl.append(wordsw[-1])
			isand = True
		count += words[maxNumber-1]
		# wordsl.append(wordsw[maxNumber-1])
		maxNumber = 0

print "count: ", count