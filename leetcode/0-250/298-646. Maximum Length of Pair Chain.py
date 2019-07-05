# 646. Maximum Length of Pair Chain
class Solution:
    def findLongestChain2(self, pairs: List[List[int]]) -> int:
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

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, res = float('-inf'), 0
        for p in sorted(pairs, key=lambda x: x[1]):
            if cur < p[0]:
                cur = p[1]
                res += 1
        return res