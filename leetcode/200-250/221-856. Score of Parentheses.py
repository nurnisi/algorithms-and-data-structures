# 856. Score of Parentheses
class Solution:

    def scoreOfParentheses(self, S):
        stack = []
        ans, i, cur = 0, 0, 0
        while i < len(S):
            if S[i] == '(':
                ans += cur * (2 ** len(stack))
                cur = 0
                stack.append(S[i])
            else:
                stack.pop()
                if not cur: cur = 1
                else: cur *= 2
            i += 1
        return ans + cur

sol = Solution()
print(sol.scoreOfParentheses("()()"))
print(sol.scoreOfParentheses("(())"))
print(sol.scoreOfParentheses("((()))"))
print(sol.scoreOfParentheses("((()()))"))
print(sol.scoreOfParentheses("(()(()))"))


        