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

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))