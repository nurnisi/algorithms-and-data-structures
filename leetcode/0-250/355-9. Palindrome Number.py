# 9. Palindrome Number
class Solution:
    def isPalindrome2(self, x: int) -> bool:
        xs = str(x)
        i, j = 0, len(xs)-1
        
        while i < j:
            if xs[i] != xs[j]:
                return False
            i += 1
            j -= 1
        
        return True

    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        y = 1
        while x // (y*10) != 0:
            y *= 10
            
        z = 10
        while y >= z:
            a, b = x // y % 10, x % z
            if x // y % 10 != x % z:
                return False
            x //= z
            y //= 100
            
        return True

    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
    
        revert = 0
        while x > revert:
            revert = revert * 10 + x % 10
            x //= 10
        
        return x == revert or x == revert//10
            
print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(1001))
print(Solution().isPalindrome(10))