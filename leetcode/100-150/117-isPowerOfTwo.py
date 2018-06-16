def isPowerOfTwo(self, n):
    return n >= 0 and list(bin(n))[2:].count('1') == 1