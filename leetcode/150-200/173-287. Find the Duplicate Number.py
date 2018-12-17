# 287. Find the Duplicate Number
class Solution:
    # bit manipulation
    def findDuplicate(self, nums):
        a = 1 << (len(nums))
        for i in nums:
            if a & 1 << i:
                return i
            a = a | 1 << i



sol = Solution()
print(sol.findDuplicate([2,2,2,2,2]))