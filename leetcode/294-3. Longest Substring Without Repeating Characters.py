# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx, i = 0, 0
        sset = set()
        for ch in s:
            if ch in sset:
                while s[i] != ch:
                    sset.remove(s[i])
                    i += 1
                i += 1
            sset.add(ch)
            mx = max(mx, len(sset))
            
        return mx

print(Solution().lengthOfLongestSubstring("abcabcbb"))