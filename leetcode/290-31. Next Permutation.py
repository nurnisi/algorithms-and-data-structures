# 31. Next Permutation
class Solution:
    def nextPermutation(self, nums) -> None:
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i == -1:
            nums.reverse()
            return
        
        j = len(nums)-1
        while nums[i] >= nums[j]:
            j -= 1
            
        nums[i], nums[j] = nums[j], nums[i]
        j = len(nums)-1
        i += 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

print(Solution().nextPermutation([1,5,1]))