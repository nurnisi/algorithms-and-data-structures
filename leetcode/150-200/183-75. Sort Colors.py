# 75. Sort Colors
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros, ones = 0, 0
        for i in nums:
            if i == 0: zeros += 1
            elif i == 1: ones += 1

        nums[:zeros:1] = [0] * zeros
        nums[zeros:zeros+ones:1] = [1] * ones 
        nums[zeros+ones::1] = [2] * (len(nums)-zeros-ones)
        
        print(nums)

sol = Solution()
sol.sortColors([2,0,2,1,1,0])