# 198. House Robber
class Solution(object):
    def rob(self, nums):
        l = len(nums)
        robs = [0] * (l + 2)
        for i in range(l):
            robs[i + 2] = max(robs[i] + nums[i], robs[i + 1])
        return robs[l + 1]

        
        