# Project Euler 31
# Coin sums
# Solution 73682

def combinations(coins, number, idxMax):
	sum = 0
	if coins[idxMax] == 2:
		return sum + number//2 + 1
	elif coins[idxMax] > number:
		return sum + combinations(coins,number,idxMax-1)
	elif coins[idxMax] == number:
		return sum + 1 + combinations(coins,number,idxMax-1)
	else:
		idx = 1
		while number > 0:
			if number == coins[idxMax-1]:
				idxMax -= 1
			sum += combinations(coins, number, idxMax-1)
			number -= coins[idxMax]
			idx +=1
	return sum + 1

coins = [1,2,5,10,20,50,100,200]
print("sum: ", combinations(coins,200,7)) 


