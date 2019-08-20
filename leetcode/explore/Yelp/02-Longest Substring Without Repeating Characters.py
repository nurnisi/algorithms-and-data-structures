# Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring2(self, s: str) -> int:
        mx = l = r = 0
        while r < len(s):
            if len(set(s[l:r+1])) == r-l+1:
                mx = max(mx, r-l+1)
                r += 1
            else:
                l += 1
                
        return mx

    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = l = 0
        st = set()
        for c in s:
            while st and c in st:
                st.remove(s[l])
                l += 1
            st.add(c)
            mx = max(mx, len(st))
        return mx

