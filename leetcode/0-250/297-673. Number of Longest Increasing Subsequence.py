# 673. Number of Longest Increasing Subsequence
class Solution:
    def findNumberOfLIS(self, nums) -> int:
        if not nums: return 0
        
        dp = []
        for x in nums:
            mx, cnt = 0, 1
            for i, (d, c) in enumerate(dp):
                if nums[i] < x:
                    if mx == d:
                        cnt += c
                    elif mx < d:
                        mx = d
                        cnt = c        
            dp.append((mx+1, cnt))
        
        mx = max(dp)[0]
        return sum(x[1] for x in dp if mx == x[0])

print(Solution().findNumberOfLIS([1,2,4,3,5,4,7,2]))