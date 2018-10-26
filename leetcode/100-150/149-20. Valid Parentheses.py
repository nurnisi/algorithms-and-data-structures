# 20. Valid Parentheses
def isValid(s):
    stack = []
    for c in s:
        if any(c == p for p in ['(', '{', '[']):
            stack.append(c)
        elif stack:
            if (c == ')' and stack[-1] == '(') \
                or (c == '}' and stack[-1] == '{') \
                or (c == ']' and stack[-1] == '['):
                stack.pop()
            else: return False    
        else:
            return False		
    return True if not stack else False

def isValid1(self, s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if top != mapping[char]:
                return False
        else:
            stack.append(char)

    return not stack
