# 647. Palindromic Substrings
class Solution:
    def countSubstrings2(self, s: str) -> int:
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

    def countSubstrings(self, s: str) -> int:
        count, n = 0, len(s)
        for k in range(n):
            i = 0
            while k - i >= 0 and k + i < n and s[k - i] == s[k + i]:
                count += 1
                i += 1
                
            i = 0
            while k - i >= 0 and k + i + 1 < n and s[k - i] == s[k + i + 1]:
                count += 1
                i += 1
        
        return count
            
        
print(Solution().countSubstrings2("abbaa"))    
print(Solution().countSubstrings("abbaa"))