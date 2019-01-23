# 394. Decode String
class Solution:
    def decodeString(self, s):
        stack = []
        for c in s:
            if c == "]":
                cur = ""
                while stack and stack[-1] != "[":
                    cur = stack.pop() + cur
                stack.pop()
                stack.append(cur * int(stack.pop()))
            elif c.isnumeric() and stack and stack[-1].isnumeric():
                stack[-1] += c
            else: stack.append(c)
        return ''.join(stack)
            


sol = Solution()
print(sol.decodeString("3[a]2[bc]"))
print(sol.decodeString("3[a2[c]]"))
print(sol.decodeString("2[abc]3[cd]ef"))

        