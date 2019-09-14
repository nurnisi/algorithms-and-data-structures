# 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        lmax, rmax = height[l], height[r]
        ans = (r-l) * min(lmax, rmax)
        
        while l < r:
            if height[l] < height[r]: 
                l += 1
                lmax = max(lmax, height[l])
            else: 
                r -= 1
                rmax = max(rmax, height[r])
            ans = max(ans, (r-l) * min(lmax, rmax))
        
        return ans