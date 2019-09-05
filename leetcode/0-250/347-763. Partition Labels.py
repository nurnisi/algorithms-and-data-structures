# 763. Partition Labels
import collections
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        counts = collections.Counter(S)
        ans = []
        prev, i, rem = -1, 0, 0
        seen = set()
        
        while i < len(S):
            if S[i] not in seen:
                rem += counts[S[i]]-1
                seen.add(S[i])
            else:
                rem -= 1
            
            if rem == 0:
                ans.append(i-prev)
                prev = i
                seen = set()
                
            i += 1
            
        return ans