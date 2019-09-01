import collections
class Solution:
    # TLE
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        ans = []
        for q in queries:
            l, r, k = q[0], q[1], q[2]
            cnt = sum([v % 2 for v in collections.Counter(s[l:r+1]).values()])
            ans.append(cnt // 2 <= k)
        return ans