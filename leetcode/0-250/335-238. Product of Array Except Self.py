# 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cur, n = 1, len(nums)
        out = [1]*n
        for i in range(1, n):
            cur *= nums[i-1]
            out[i] = cur
        
        cur = 1
        for i in range(n-2, -1, -1):
            cur *= nums[i+1]
            out[i] *= cur
        
        return out