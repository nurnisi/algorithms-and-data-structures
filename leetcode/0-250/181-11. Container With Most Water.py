# 11. Container With Most Water
import collections
class Solution:
    # TLE: brute force
    def maxArea2(self, height):
        ans, n = 0, len(height)
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, (j-i) * min(height[i], height[j]))
        return ans

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
print(sol.maxArea2([1,8,6,2,5,4,8,3,7]))