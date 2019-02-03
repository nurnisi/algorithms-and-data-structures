# 680. Valid Palindrome II
import collections
class Solution:
    def validPalindrome2(self, s):
        n = len(s)
        stack = list(s[:n//2])
        print(stack)
        for i in range(n//2+n%2, n):
            if stack[-1] == s[i]: stack.pop()
            else: return False
        return True

    def validPalindrome3(self, s):
        i, j, flag = 0, len(s)-1, False
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif flag:
                return False
            else:
                if s[i] == s[j-1] and s[i+1] == s[j-2]: j -= 1
                elif s[i+1] == s[j] and s[i+2] == s[j-1]: i += 1
                else: return False
                flag = True
        return True

    def validPalindrome(self, s):
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

sol = Solution()
print(sol.validPalindrome("ebcbbececabbacecbbcbe"))
print(sol.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
        

        