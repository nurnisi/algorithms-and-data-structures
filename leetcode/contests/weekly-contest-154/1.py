import collections
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = collections.Counter(text)
        ans = float('inf')
        for ch in 'ban':
            ans = min(ans, cnt.get(ch, 0))
        
        for ch in 'lo':
            ans = min(ans, cnt.get(ch, 0) // 2)
        
        return ans