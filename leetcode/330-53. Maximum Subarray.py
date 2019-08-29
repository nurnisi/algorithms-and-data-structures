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

# Divide and conquer
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.rec(nums, 0, len(nums)-1)
    
    def rec(self, nums, l, r):
        if l == r: return nums[l]
        mid = (l+r)//2
        
        return max(self.rec(nums, l, mid),
                  self.rec(nums, mid+1, r),
                  self.crossSum(nums, l, r, mid))

    def crossSum(self, nums, l, r, mid):
        lsum, lmax = 0, float('-inf')
        for i in range(mid, l-1, -1):
            lsum += nums[i]
            lmax = max(lmax, lsum)
            
        rsum, rmax = 0, float('-inf')
        for i in range(mid+1, r+1):
            rsum += nums[i]
            rmax = max(rmax, rsum)
            
        return lmax + rmax