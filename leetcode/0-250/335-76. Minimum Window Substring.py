# 76. Minimum Window Substring
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = collections.Counter(t)
        fix_cnt = cnt.copy()
        n = rem = len(t)
        l = r = 0
        ans = None
        
        while r < len(s):
            while r < len(s) and rem > 0:
                if s[r] in cnt:
                    if cnt[s[r]] > 0:
                        rem -= 1
                    cnt[s[r]] -= 1
                r += 1
            while l < r and rem <= 0:
                if not ans or len(ans) > r-l:
                    ans = s[l:r]
                if s[l] in cnt:
                    if cnt[s[l]] >= 0 and cnt[s[l]] < fix_cnt[s[l]]:
                        rem += 1
                    cnt[s[l]] += 1
                l += 1
        
        return ans or ""

print(Solution().minWindow("ADOBECODEBANCA", "ABCA"))