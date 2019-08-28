# 53. Maximum Subarray
class Solution:
    def maxSubArray2(self, nums: List[int]) -> int:
        cum, ans, mn = 0, float('-inf'), 0
        for x in nums:
            cum += x
            ans = max(ans, cum-mn)
            mn = min(mn, cum)
        
        return ans

    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = nums[0]
        for x in nums[1:]:
            cur_sum = max(x, cur_sum+x)
            max_sum = max(max_sum, cur_sum)
        return max_sum