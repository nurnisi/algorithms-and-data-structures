# 1106. Parsing A Boolean Expression
class Solution:
    def parseBoolExpr(self, expr: str) -> bool:
        stack = []
        for i, e in enumerate(expr):
            if e in ['!', '|', '&']:
                stack.append(e)
            elif e in ['f', 't']:
                stack.append(True if e == 't' else False)
            elif e == ')':
                arr = []
                while stack[-1] not in ['!', '|', '&']:
                    arr.append(stack.pop())
                ecur = stack.pop()
                if ecur == '!': stack.append(not arr[0])
                elif ecur == '|': stack.append(any(arr))
                else: stack.append(all(arr))
                    
        return stack[0]
            
print(Solution().parseBoolExpr("!(f)"))