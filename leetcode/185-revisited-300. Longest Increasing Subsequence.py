# 300. Longest Increasing Subsequence
class Solution:
    def lengthOfLIS2(self, nums) -> int:
        dp = []
        for x in nums:
            mx = 0
            for i, d in enumerate(dp):
                if nums[i] < x and mx < d:
                    mx = d
            dp.append(mx + 1)
        
        return max(dp) if dp else 0

    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))