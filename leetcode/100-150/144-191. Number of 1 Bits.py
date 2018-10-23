# 191. Number of 1 Bits
def hammingWeight(n):
    count = 0
    while n:
        count += (n & 1)
        n >>= 1
    return count

def hammingWeight2(self, n):
	count = 0
	while n:
		count += 1
		n &= (n-1)
	return count


print(hammingDistance(8))
            