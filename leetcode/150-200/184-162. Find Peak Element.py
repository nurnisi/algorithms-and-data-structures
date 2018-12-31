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

    # binary search
    def findPeakElement2(self, nums):
        l, r = 1, len(nums)
        nums = [float('-inf')] + nums + [float('-inf')]
        while l < r:
            mid = (l + r) // 2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]: return mid-1
            if nums[mid-1] < nums[mid] and nums[mid] < nums[mid+1]: l = mid + 1
            else: r = mid

        return l-1

    # leetcode linear solution
    def findPeakElement3(self, nums):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums)-1

sol = Solution()
print(sol.findPeakElement2([1,2,1]))
print(sol.findPeakElement2([1,2,3,1]))
print(sol.findPeakElement2([1,2,1,3,5,6,4]))
print(sol.findPeakElement2([1]))
print(sol.findPeakElement2([1,2]))
