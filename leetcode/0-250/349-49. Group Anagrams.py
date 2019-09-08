# 49. Group Anagrams
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [(''.join(sorted(w)), w) for w in strs]
        d = collections.defaultdict(list)
        for sorted_w, w in sorted_strs:
            d[sorted_w].append(w)
        
        return d.values()