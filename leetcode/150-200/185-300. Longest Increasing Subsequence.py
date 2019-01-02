# 300. Longest Increasing Subsequence
import collections
class Solution:
    # TLE: 24/24 test
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = collections.defaultdict(int)
        def helper(cur):
            curMax = 0
            for i in range(cur+1, len(nums)):
                if cur == -1 or nums[cur] < nums[i]:
                    if i in d:
                        curMax = max(curMax, d[i])
                    else:
                        imax = helper(i)
                        d[i] = max(d[i], imax)
                        curMax = max(curMax, d[i])
            
            return 1 + curMax

        return helper(-1) - 1

    # dp
    def lengthOfLIS2(self, nums):
        if not nums: return 0
        dp = [0] * len(nums)
        for i in range(len(nums)):
            curMax = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    curMax = max(curMax, dp[j])
            dp[i] = curMax + 1
        
        return max(dp)

sol = Solution()
print(sol.lengthOfLIS2([10,9,2,5,3,7,101,18]))
print(sol.lengthOfLIS2([0,1,2,4,6,7,16,18]))