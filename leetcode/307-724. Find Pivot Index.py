# 724. Find Pivot Index
class Solution:
    def pivotIndex2(self, nums: List[int]) -> int:
        left = [0] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1] + nums[i-1]
        
        right = [0] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] + nums[i+1]
        
        for i in range(len(nums)):
            if left[i] == right[i]:
                return i
            
        return -1

    def pivotIndex(self, nums: List[int]) -> int:
        sm = [0]
        for i in nums:
            sm.append(sm[-1] + i)
        
        for i in range(1, len(sm)):
            if sm[i-1] == sm[-1] - sm[i]:
                return i-1
        
        return -1
        
        