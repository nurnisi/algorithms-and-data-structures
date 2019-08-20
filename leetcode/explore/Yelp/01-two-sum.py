class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {nums[i]: i for i in range(len(nums))}
        
        for i in range(len(nums)):
            j = target - nums[i]
            if j in d and d[j] != i:
                return [i, d[j]]