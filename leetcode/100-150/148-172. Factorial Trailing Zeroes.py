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
def trailingZeros1(n):
	five = 5
	zeros = 0
	while five <= n:
		zeros += (n / five)
		five *= 5
	return zeros

# leetcode solution
def trailingZeros2(n):
	return 0 if n == 0 else n / 5 + trailingZeros(n / 5)
