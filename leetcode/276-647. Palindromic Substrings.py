# 647. Palindromic Substrings
class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        n = len(s)

        def rec(i, j):
            if i < 0 or j >= n or s[i] != s[j]: return
            self.count += 1
            rec(i-1, j+1)

        for i in range(n):
            rec(i, i)
            rec(i, i+1)

        return self.count
    
print(Solution().countSubstrings("abbaa"))