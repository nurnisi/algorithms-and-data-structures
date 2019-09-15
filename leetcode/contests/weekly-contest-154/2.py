class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        i = 0;
        while i < len(s):
            if s[i] == ')':
                cur = []
                while stack and stack[-1] != '(':
                    cur.append(stack.pop())
                stack.pop()
                stack.extend(cur)
            else:
                stack.append(s[i])
            i += 1
        
        return ''.join(stack)