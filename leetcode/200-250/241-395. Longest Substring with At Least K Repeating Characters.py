# 395. Longest Substring with At Least K Repeating Characters
import collections
class Solution:
    def longestSubstring(self, s, k):
        count, n = [], len(s)
        i = j = 0
        while i < n:
            while j < n and s[i] == s[j]: j += 1
            count.append((s[i], j - i))
            i = j
        
        ans = 0
        dct = collections.defaultdict(int)
        tot1 = 0
        for i in range(len(count)):
            ch, cnt = count[i]
            dct[ch] += cnt
            dct_copy = {key: v for key, v in dct.items()}
            tot1 = tot2 = tot1 + cnt
            for j in range(i + 1):
                if all(v == 0 or v >= k for key, v in dct_copy.items()):
                    ans = max(ans, tot2)
                    break
                ch, cnt = count[j]
                dct_copy[ch] -= cnt
                tot2 -= cnt
                if tot2 < ans: break
        return ans

sol = Solution()
print(sol.longestSubstring("aaabbc", 2))
print(sol.longestSubstring("bbaaacbd", 3))

        