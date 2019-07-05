# 646. Maximum Length of Pair Chain
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs: return 0
        pairs.sort()
        stack = [pairs[0]]
        for p in pairs:
            if p[0] > stack[-1][1]:
                stack.append(p)
            elif p[1] < stack[-1][1]:
                stack.pop()
                stack.append(p)
        return len(stack)