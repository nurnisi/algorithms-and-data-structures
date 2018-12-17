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

    # counter
    def findDuplicate3(self, nums):
        count = collections.Counter(nums)
        for k, v in count.items():
            if v > 1:
                return k

sol = Solution()
print(sol.findDuplicate3([2,2,2,2,2]))