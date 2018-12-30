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

    def sortColors2(self, nums):
        zero, two, cur = 0, len(nums)-1, 0
        while zero < two and cur <= two:
            if cur < zero: cur = zero
            if nums[cur] == 0: nums[zero], nums[cur] = nums[cur], nums[zero]
            if nums[cur] == 2: nums[two], nums[cur] = nums[cur], nums[two]
            if nums[cur] == 1: cur += 1
            if nums[zero] == 0: zero += 1
            if nums[two] == 2: two -= 1

        print(nums)

sol = Solution()
sol.sortColors2([2,0,2,1,1,0])
sol.sortColors2([0,0,1,1,1,2])
sol.sortColors2([0,1,2,0,1,2,0,1])
sol.sortColors2([1,0])
sol.sortColors2([0,0])
sol.sortColors2([0])
sol.sortColors2([0,2])
sol.sortColors2([0,2,0])

