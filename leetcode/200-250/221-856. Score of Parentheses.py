# 856. Score of Parentheses
class Solution:

    def scoreOfParentheses2(self, S):
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

    def scoreOfParentheses(self, S):
        stack, count, ans = [], 0, 0
        for p in S:
            if p == '(':
                if count: ans += 2 ** (len(stack) + count - 1)
                count = 0
                stack.append(p)
            else:
                stack.pop()
                count += 1
        return ans + 2 ** (count - 1)  

sol = Solution()
print(sol.scoreOfParentheses("()()"))
print(sol.scoreOfParentheses("(())"))
print(sol.scoreOfParentheses("((()))"))
print(sol.scoreOfParentheses("((()()))"))
print(sol.scoreOfParentheses("(()(()))"))


        