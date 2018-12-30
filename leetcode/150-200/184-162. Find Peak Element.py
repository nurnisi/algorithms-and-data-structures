# 162. Find Peak Element
import sys
class Solution:
    # linear solution
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Maximum values in Python
        # sys.maxsize
        # -sys.maxsize
        # float('inf')
        # float('inf')

        n = len(nums)
        if n == 1: return 0
        if nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return n-1
        for i in range(1, n-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i

sol = Solution()
print(sol.findPeakElement([1,2,1]))
print(sol.findPeakElement([1,2,3,1]))
print(sol.findPeakElement([1,2,1,3,5,6,4]))
