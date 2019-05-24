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

    def isIsomorphic2(self, s, t):
        return len(set(zip(s,t))) == len(set(s)) and len(set(zip(t,s))) == len(set(t))

sol = Solution()
print(sol.isIsomorphic2("egg", "add"))
print(sol.isIsomorphic2("foo", "bar"))
print(sol.isIsomorphic2("paper", "title"))
print(sol.isIsomorphic2("aa", "ab"))


        