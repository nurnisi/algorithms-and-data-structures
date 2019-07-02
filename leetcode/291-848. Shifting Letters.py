# 848. Shifting Letters
class Solution:
    def shiftingLetters(self, S: str, shifts) -> str:
        i = len(S)-2
        
        shifts[-1] %= 26
        while i >= 0:
            shifts[i] = (shifts[i] + shifts[i+1]) % 26
            i -= 1
        
        ans = []
        for i, ch in enumerate(S):
            ans.append(chr((ord(ch) - ord('a') + shifts[i]) % 26 + ord('a')))
        
        return ''.join(ans)

print(Solution().shiftingLetters("bad", [10,20,30]))
print(Solution().shiftingLetters("ruu", [26,9,17]))