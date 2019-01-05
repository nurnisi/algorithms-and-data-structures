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

    # cumulative sum
    def findMaxAverage2(self, nums, k):
        sums = nums.copy()
        for i in range(1, len(sums)): sums[i] += sums[i-1]
        maximum = sums[k - 1]
        for i in range(k, len(sums)):
            maximum = max(maximum, sums[i] - sums[i - k])
        return maximum / k

sol = Solution()
print(sol.findMaxAverage2([1,12,-5,-6,50,3], 5))
print(sol.findMaxAverage2([0,4,0,3,2], 1))

        