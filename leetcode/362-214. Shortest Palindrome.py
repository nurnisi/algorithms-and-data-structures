# 214. Shortest Palindrome
class Solution:
    # Bruteforce
    def shortestPalindrome(self, s: str) -> str:
        for i in range(len(s), -1, -1):
            if s[:i] == s[:i][::-1]:
                return s[i:][::-1] + s

    # KMP
    def shortestPalindrome(self, s: str) -> str:
        i = self.KMP(s+'#'+s[::-1])[-1]
        return s[i:][::-1] + s
    
    def KMP(self, s):
        j, i, n = 0, 1, len(s)
        kmp = [0] * n
        
        while i < n:
            if s[i] == s[j]:
                kmp[i] = j+1
                j += 1
                i += 1
            else:
                if j != 0:
                    j = kmp[j-1]
                else:
                    kmp[i] = 0
                    i += 1
        
        return kmp