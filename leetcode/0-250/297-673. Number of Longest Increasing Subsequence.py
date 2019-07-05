# 673. Number of Longest Increasing Subsequence
class Solution:
    def findNumberOfLIS2(self, nums) -> int:
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

    # does not work
    def findNumberOfLIS(self, nums) -> int:
        if not nums: return 0
        
        tails = [[0, 1] for _ in range(len(nums))]
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m][0] < x: 
                    i = m + 1
                else: 
                    j = m

            if tails[i][0] == 0:
                tails[i][1] = 1 if i == 0 else tails[i-1][1]
            else: 
                tails[i][1] += 1

            tails[i][0] = x
            size = max(i+1, size)
            
        return tails[size-1][1]

print(Solution().findNumberOfLIS([1,3,5,4,7]))