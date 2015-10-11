# Project Euler number 19
# Counting Sundays
# answer: 171


months =  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print sum(months)

firstSunday1990 = 7

months[0] = 31 - firstSunday1990 + 1

startYear = 1901
endYear = 2001
knownYear = 1900

def isLeapYear(year):
	if year%4 != 0:
		return False
	elif year%100 != 0:
		return True
	elif year%400 != 0:
		return False
	return True

month = 1
count = 0
year = knownYear
# for year in range(knownYear,endYear):
if isLeapYear(year):
	months[1] = 29
else:
	months[1] = 28

while year < endYear:
	print "Year: ", year
	if isLeapYear(year):
		months[1] = 29
	else:
		months[1] = 28

	while month < 13:
		if month is not 12:
			if sum(months[0:month])%7 == 0:
				print "MonDAY, month -", month+1
				if year >= startYear and year < endYear:
					count += 1
		else:
			a = sum(months)%7
			if a is 0:
				print "MonDAY, month -", month+1
				months[0] = 31
				if year >= startYear and year < endYear:
					if year != endYear - 1 and month != 13:
						count += 1
			else:
				months[0] = 31+a
		month += 1

	month = 1
	year += 1

print "count: ", count

