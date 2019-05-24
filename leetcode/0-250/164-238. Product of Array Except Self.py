# 238. Product of Array Except Self
class Solution:
    # brute force
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product, ans, zeros, check = 1, [0 for i in nums], 0, False
        for i in nums: 
            if i: product *= i
            else: zeros += 1
                
        for i in range(len(nums)):
            if nums[i]: 
                if zeros: ans[i] = 0 
                else: ans[i] = product//nums[i]
            elif zeros < 2: ans[i] = product

        return ans
        