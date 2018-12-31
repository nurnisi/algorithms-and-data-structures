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

    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = collections.defaultdict(int)
        arr = [float('inf')] * len(nums)
        def helper(cur):
            curMax = 0
            for i in range(cur+1, len(nums)):
                if cur == -1 or (nums[cur] <= arr[i] and nums[cur] < nums[i]):
                    if i in d:
                        curMax = max(curMax, d[i])
                    else:
                        imax = helper(i)
                        d[i] = max(d[i], imax)
                        curMax = max(curMax, d[i])
                    if cur != -1:
                        arr[i] = nums[cur]
            
            return 1 + curMax

        return helper(-1) - 1

sol = Solution()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(sol.lengthOfLIS([0,1,2,4,6,7,16,18]))
            

