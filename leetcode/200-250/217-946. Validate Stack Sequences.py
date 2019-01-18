# 946. Validate Stack Sequences
class Solution:
    def validateStackSequences(self, pushed, popped):
        i = j = 0
        stack, out = [], []
        while i < len(pushed) and j < len(popped):
            if not stack:
                stack.append(pushed[i])
                i += 1
            elif stack[-1] != popped[j]:
                stack.append(pushed[i])
                i += 1
            else:
                stack.pop()
                j += 1

        while j < len(popped) and stack:
            if stack.pop() != popped[j]:
                return False
            j += 1
        
        return True

sol = Solution()
print(sol.validateStackSequences([1,2,3,4,5], [4,5,3,1,2]))
print(sol.validateStackSequences([1], [1]))
        