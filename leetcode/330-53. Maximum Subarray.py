# 53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cum, ans, mn = 0, float('-inf'), 0
        for x in nums:
            cum += x
            ans = max(ans, cum-mn)
            mn = min(mn, cum)
        
        return ans