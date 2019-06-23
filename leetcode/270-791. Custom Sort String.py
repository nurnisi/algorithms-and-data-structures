# 791. Custom Sort String
from collections import Counter
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        cnt = Counter(T)
        ans = []
        for c in S:
            n = cnt.pop(c, None)
            if n: ans.append(c * n)
        
        for k, v in cnt.items():
            ans.append(k * v)
        
        return ''.join(ans)
            
        