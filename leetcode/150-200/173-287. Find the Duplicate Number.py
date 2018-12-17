# 287. Find the Duplicate Number
import collections
class Solution:
    # bit manipulation
    def findDuplicate(self, nums):
        a = 1 << (len(nums))
        for i in nums:
            if a & 1 << i:
                return i
            a = a | 1 << i

    # sorting: does not satisfy the conditions
    def findDuplicate2(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]

    # counter: does not satisfy the conditions
    def findDuplicate3(self, nums):
        count = collections.Counter(nums)
        for k, v in count.items():
            if v > 1:
                return k

    # set: does not satisfy the conditions
    def findDuplicate5(self, nums):
        seen = set()
        for i in nums:
            if i in seen:
                return i
            seen.add(i)

    # cycle detection
    def findDuplicate4(self, nums):
        tor, rab = 0, 0
    
        while True:
            tor = nums[tor]
            rab = nums[nums[rab]]
            if tor == rab:
                break
        
        tor = 0
        while tor != rab:
            tor = nums[tor]
            rab = nums[rab]
        
        return tor
    

sol = Solution()
print(sol.findDuplicate4([2,2,2,2,2]))