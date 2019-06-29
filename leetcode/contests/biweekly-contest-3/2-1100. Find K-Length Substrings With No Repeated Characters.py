# 1100. Find K-Length Substrings With No Repeated Characters
import collections
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if K > len(S): return 0
        
        ans = 0
        for i in range(len(S)-K+1):
            cnt = collections.Counter(S[i:i+K])
            if all(v == 1 for k, v in cnt.items()): ans += 1
            
        return ans
            
print(Solution().numKLenSubstrNoRepeats("havefunonleetcode", 5))