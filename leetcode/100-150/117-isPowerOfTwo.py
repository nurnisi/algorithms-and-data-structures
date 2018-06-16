def isPowerOfTwo(self, n):
    return n >= 0 and bin(n).count('1') == 1

def isPowerOfTwo2(self, n):
    return n>0 and (n&(n-1))==0