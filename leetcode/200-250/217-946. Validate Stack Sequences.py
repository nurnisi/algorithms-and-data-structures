# 946. Validate Stack Sequences
class Solution:
    def validateStackSequences2(self, pushed, popped):
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

    def validateStackSequences(self, pushed, popped):
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)

sol = Solution()
print(sol.validateStackSequences([1,2,3,4,5], [4,5,3,1,2]))
print(sol.validateStackSequences([1], [1]))
print(sol.validateStackSequences([], []))
        