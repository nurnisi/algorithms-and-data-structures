# 11. Container With Most Water
import collections
class Solution:
    # two pointers
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, ans = 0, len(height)-1, 0
        while left < right:
            ans = max(ans, (right-left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return ans

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))