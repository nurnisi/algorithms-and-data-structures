# 5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        mx = 0
        ans = ""
        n = len(s)
        
        # odd strings
        for i in range(n):
            j = 0
            while 0 <= i-j and i+j < n and s[i-j] == s[i+j]:
                j += 1
            if mx < 2*j-1:
                mx = 2*j-1
                ans = s[i-j+1:i+j]
        
        # even strings
        for i in range(n-1):
            j = 0
            while 0 <= i-j and i+j+1 < n and s[i-j] == s[i+j+1]:
                j += 1
            if mx < 2*j:
                mx = 2*j
                ans = s[i-j+1:i+j+1]
                
        return ans

print(Solution().longestPalindrome("cbba"))