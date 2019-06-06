# 1002. Find Common Characters
from collections import Counter

class Solution:
    def commonChars(self, A):
        cnt_tot = Counter(A[0])
        
        for s in A[1:]:
            cnt_cur = Counter(s)
            cnt_tot &= cnt_cur

        ans = []
        for k, v in cnt_tot.items():
            ans += [k] * v
        return ans

print(Solution().commonChars(["bella","label","roller"]))