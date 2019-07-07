# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        c = 0
        ans = [0] * len(seq)
        for i, br in enumerate(seq):
            if br == '(':
                c += 1
                ans[i] = c % 2
            else:
                ans[i] = c % 2
                c -= 1

        return ans