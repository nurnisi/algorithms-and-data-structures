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

    def scoreOfParentheses3(self, S):
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
    
    # leetcode stack
    def scoreOfParentheses4(self, S):
        stack = [0]
        for p in S:
            if p == '(': stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
        return stack.pop()

    # leetcode balance
    def scoreOfParentheses(self, S):
        bal = ans = 0
        for i, p in enumerate(S):
            if p == '(': bal += 1
            else:
                bal -= 1
                if S[i-1] == '(':
                    ans += 2 ** bal
        return ans

sol = Solution()
print(sol.scoreOfParentheses("()()"))
print(sol.scoreOfParentheses("(())"))
print(sol.scoreOfParentheses("((()))"))
print(sol.scoreOfParentheses("((()()))"))
print(sol.scoreOfParentheses("(()(()))"))


        