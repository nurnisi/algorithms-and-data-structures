# 290. Word Pattern
import collections
class Solution:
    def wordPattern2(self, pattern: str, s: str) -> bool:
        sSplit = s.split(' ')
        
        if len(pattern) != len(sSplit):
            return False
        
        dptr, dstr = collections.defaultdict(str), collections.defaultdict(str)
        for i in range(len(pattern)):
            if pattern[i] in dptr and dptr[pattern[i]] != sSplit[i] or sSplit[i] in dstr and dstr[sSplit[i]] != pattern[i]:
                return False
            dptr[pattern[i]] = sSplit[i]
            dstr[sSplit[i]] = pattern[i]
        
        return True

