# 5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        mx = ""
        for i in range(n):
            j = 0
            while i-j >= 0 and i+j < n and s[i-j] == s[i+j]:
                if len(mx) < len(s[i-j:i+j+1]): mx = s[i-j:i+j+1]
                j += 1
                
        for i in range(n-1):
            j = 0
            while i-j >= 0 and i+j+1 < n and s[i-j] == s[i+j+1]:
                if len(mx) < len(s[i-j:i+j+2]): mx = s[i-j:i+j+2]
                j += 1
        
        return mx