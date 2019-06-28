# 1081. Smallest Subsequence of Distinct Characters
class Solution:
    def smallestSubsequence(self, text: str) -> str:
        last = {c: i for i, c in enumerate(text)}
        stack = []
        for i, c in enumerate(text):
            if c in stack: continue
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
        return "".join(stack)