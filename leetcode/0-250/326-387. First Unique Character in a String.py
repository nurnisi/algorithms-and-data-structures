# 387. First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = collections.Counter(s)
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1