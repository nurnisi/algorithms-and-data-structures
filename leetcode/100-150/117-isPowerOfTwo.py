def isPowerOfTwo(self, n):
    return n >= 0 and bin(n).count('1') == 1

def isPowerOfTwo2(self, n):
    return n>0 and (n&(n-1))==0

def isPowerOfTwo3(self, n):
    while n!=0 and n%2==0: n/=2
    return n==1