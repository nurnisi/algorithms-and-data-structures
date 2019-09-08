# 5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        n = len(s)
        
        for i in range(n):
            j = 0
            while 0 <= i-j-1 and i+j+1 < n and s[i-j-1] == s[i+j+1]:
                j += 1
            if len(ans) < j+j+1:
                ans = s[i-j: i+j+1]
        
        for i in range(n-1):
            j = 0
            while 0 <= i-j and i+j+1 < n and s[i-j] == s[i+j+1]:
                j += 1
            if len(ans) < j+j:
                ans = s[i-j+1: i+j+1]
        
        return ans