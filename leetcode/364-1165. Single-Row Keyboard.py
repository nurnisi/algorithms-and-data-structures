# 1165. Single-Row Keyboard
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        ans = prev = 0
        d_kb = {k:i for i, k in enumerate(keyboard)}
        
        for ch in word:
            ans += max(prev, d_kb[ch]) - min(prev, d_kb[ch])
            prev = d_kb[ch]
            
        return ans