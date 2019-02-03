# 131. Palindrome Partitioning
class Solution:
    # brute force: accepted
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

sol = Solution()
print(sol.partition("aabac"))