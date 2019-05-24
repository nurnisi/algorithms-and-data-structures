# 680. Valid Palindrome II
import collections
class Solution:
    def validPalindrome2(self, s):
        i, j = 0, 0
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        
        i1, j1 = i + 1, j
        while i1 < j1 and s[i1] == s[j1]:
            i1 += 1
            j1 -= 1
        
        i2, j2 = i, j - 1
        while i2 < j2 and s[i2] == s[j2]:
            i2 += 1
            j2 -= 1
        
        return i1 >= j1 or i2 >= j2

    def validPalindrome3(self, s):
        def is_pali(i, j):
            return all(s[k] == s[j-k+i] for k in range(i, j))
        
        for k in range(len(s)//2):
            if s[k] != s[~k]:
                j = len(s)-1-k
                return is_pali(k+1, j) or is_pali(k, j-1)
        return True

    def validPalindrome(self, s):
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                one, two = s[i:j], s[i+1:j+1]
                return one == one[::-1] or two == two[::-1]
            i, j = i+1, j-1
        return True

sol = Solution()
print(sol.validPalindrome("ebcbbececabbacecbbcbe"))
print(sol.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
        

        