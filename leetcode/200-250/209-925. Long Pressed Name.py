# 925. Long Pressed Name
class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = j = 0
        n, t = len(name), len(typed)
        while i < n nad j < t:
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

sol = Solution()
print(sol.isLongPressedName(name = "alex", typed = "aaleex"))
print(sol.isLongPressedName(name = "leelee", typed = "lleeelee"))
print(sol.isLongPressedName(name = "saeed", typed = "ssaaedd"))
print(sol.isLongPressedName(name = "laiden", typed = "laiden"))
            
        