# 643. Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maximum = cursum = sum(nums[:k])
        for i in range(k, len(nums)):
            cursum += nums[i] - nums[i-k]
            maximum = max(maximum, cursum)
        return maximum / k

sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 5))
print(sol.findMaxAverage([0,4,0,3,2], 1))

        