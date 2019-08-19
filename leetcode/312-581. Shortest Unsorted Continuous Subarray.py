# 581. Shortest Unsorted Continuous Subarray
class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        nums_sorted = sorted(nums)
        n = len(nums)
        i, j = -1, n
        while i < n-1 and nums[i+1] == nums_sorted[i+1]:
            i += 1
        while j > 0 and nums[j-1] == nums_sorted[j-1]:
            j -= 1
        return 0 if i == n-1 else j-i-1

print(Solution().findUnsortedSubarray([1,3,2,4,5]))