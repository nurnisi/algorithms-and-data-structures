# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        xs = str(x)
        i, j = 0, len(xs)-1
        
        while i < j:
            if xs[i] != xs[j]:
                return False
            i += 1
            j -= 1
        
        return True
            
        
            