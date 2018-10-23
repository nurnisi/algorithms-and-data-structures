# 191. Number of 1 Bits
def hammingDistance(n):
    count = 0
    while n:
        count += (n & 1)
        n >>= 1
    return count

print(hammingDistance(8))
            