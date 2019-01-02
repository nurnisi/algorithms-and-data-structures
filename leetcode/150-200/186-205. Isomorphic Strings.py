# 205. Isomorphic Strings
class Solution:
    def isIsomorphic(self, s, t):
        ds, dt = {}, {}
        for i in range(len(s)):
            if s[i] in ds and ds[s[i]] != t[i]: return False
            else: ds[s[i]] = t[i]

            if t[i] in dt and dt[t[i]] != s[i]: return False
            else: dt[t[i]] = s[i]

        return True

sol = Solution()
print(sol.isIsomorphic("egg", "add"))
print(sol.isIsomorphic("foo", "bar"))
print(sol.isIsomorphic("paper", "title"))
print(sol.isIsomorphic("aa", "ab"))


        