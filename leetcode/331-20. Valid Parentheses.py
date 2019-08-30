# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')':'(', '}':'{', ']':'['}
        for b in s:
            if b in d.values():
                stack.append(b)
            else:
                if not stack or stack[-1] != d[b]:
                    return False
                stack.pop()
        return not stack

    def isValid(self, s: str) -> bool:
        stack = []
        d = {')':'(', '}':'{', ']':'['}
        for b in s:
            if b in d.values():
                stack.append(b)
            elif not stack or stack.pop() != d[b]:
                return False
        return not stack