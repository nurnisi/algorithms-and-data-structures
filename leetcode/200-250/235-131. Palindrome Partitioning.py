# 131. Palindrome Partitioning
class Solution:
    # backtracking
    def partition(self, s):
        ans, part = [], []
        def is_palindrome(s):
            return all(s[i] == s[~i] for i in range(len(s)//2))

        def helper(s):
            if not s:
                ans.append(part.copy())
                return

            for i in range(1, len(s) + 1):
                if is_palindrome(s[:i]):
                    part.append(s[:i])
                    helper(s[i:])
                    part.pop()
        helper(s)
        return ans

    # 1-liner
    def partition(self, s):
        return [[s[:i]] + rest for i in range(1, len(s)+1) if s[:i] == s[i-1::-1] for rest in self.partition(s[i:])] or [[]]

sol = Solution()
print(sol.partition("aabac"))