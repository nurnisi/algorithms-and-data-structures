# 678. Valid Parenthesis String
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == ')':
                i = len(stack) - 1
                while i >= 0 and stack[i] != '(':
                    i -= 1
                if i >= 0: stack.pop(i)
                elif stack: stack.pop()
                else: return False
            else:
                stack.append(x)
        
        stack2 = []
        for x in stack:
            if x == '*':
                if stack2: stack2.pop()
            else: stack2.append('(')
                
        return not stack2
            
        