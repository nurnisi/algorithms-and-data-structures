def isPowerOfThree(self, n):
    while n>0 and n%3==0: n/=3
    return n==1

def isPowerOfThree2(self, n):
    return n>0 and (n==1 or (n%3==0 and self.isPowerOfThree(n/3)))

def isPowerOfThree3(self, n):
    return n>0 and 1162261467%n==0