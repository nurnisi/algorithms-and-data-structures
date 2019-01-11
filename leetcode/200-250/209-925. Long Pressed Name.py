# 925. Long Pressed Name
import itertools
class Solution:
    def isLongPressedName2(self, name, typed):
        i = j = 0
        n, t = len(name), len(typed)
        while i < n and j < t:
            curn = name[i]
            cn = 0
            while i < n and curn == name[i]:
                cn += 1
                i += 1
            curt = typed[j]
            ct = 0
            while j < t and curt == typed[j]:
                ct += 1
                j += 1
            if cn > ct or curn != curt: return False
        
        if i != n or j != t: return False
        return True

    def isLongPressedName(self, name, typed):
        gn = [(k, len(list(g))) for k, g in itertools.groupby(name)]
        gt = [(k, len(list(g))) for k, g in itertools.groupby(typed)]
        if len(gn) != len(gt): return False
        return all(kn == kt and vn <= vt for (kn, vn), (kt, vt) in zip(gn, gt))

sol = Solution()
print(sol.isLongPressedName(name = "alex", typed = "aaleex"))
print(sol.isLongPressedName(name = "leelee", typed = "lleeelee"))
print(sol.isLongPressedName(name = "saeed", typed = "ssaaedd"))
print(sol.isLongPressedName(name = "laiden", typed = "laiden"))
            
        