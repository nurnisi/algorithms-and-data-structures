# 42. Trapping Rain Water
# TLE
import heapq
class Solution:
    def trap2(self, height) -> int:
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

    def trap(self, height) -> int:
        ans = 0
        l, r = 0, len(height)-1
        lmax = rmax = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= lmax:
                    lmax = height[l]
                else:
                    ans += lmax - height[l]
                l += 1
            else:
                if height[r] >= rmax:
                    rmax = height[r]
                else:
                    ans += rmax - height[r]
                r -= 1
        return ans
        
print(Solution().trap([0,1,0,3,2,0,1,3,2,1,2,1]))