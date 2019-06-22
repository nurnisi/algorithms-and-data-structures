# 1018. Binary Prefix Divisible By 5
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = []
        cur = 0
        for i in A:
            cur = cur * 2 + i
            ans.append(True if cur % 5 == 0 else False)
        return ans