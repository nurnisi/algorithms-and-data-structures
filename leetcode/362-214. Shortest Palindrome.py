# 214. Shortest Palindrome
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        for i in range(len(s), -1, -1):
            if s[:i] == s[:i][::-1]:
                return s[i:][::-1] + s