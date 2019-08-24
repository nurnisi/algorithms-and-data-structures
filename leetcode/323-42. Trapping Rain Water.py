# 42. Trapping Rain Water
# TLE
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        bars = []
        
        for i, h in enumerate(height):
            if h > 0:
                j, l = 0, len(bars)
                while j < h:
                    if j < l: 
                        ans += i - bars[j] - 1
                        bars[j] = i
                    else:
                        bars.append(i)
                    j += 1
        
        return ans
        