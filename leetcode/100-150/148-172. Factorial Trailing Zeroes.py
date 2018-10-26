# 172. Factorial Trailing Zeroes
#exceeds time limit
def trailingZeros(n):
	fact = 1
	for i in range(1, n+1):
		fact *= i
	
	zeros = 0
	while fact % 10 == 0:
		zeros += 1
		fact /= 10
	
	return zeros

# accepted
def trainlingZeros(n):
	five = 5
	zeros = 0
	while five <= n:
		zeros += (n / five)
		five *= 5
	return zeros


print(trailingZeros(10))
