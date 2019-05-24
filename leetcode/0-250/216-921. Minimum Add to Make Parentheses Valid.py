# 921. Minimum Add to Make Parentheses Valid
class Solution:
    def minAddToMakeValid(self, S):
        stack = []
        for c in S:
            if c == ')' and stack and stack[-1] == '(': stack.pop()
            else: stack.append(c)
        return len(stack)

sol = Solution()
print(sol.minAddToMakeValid("((())))"))

        