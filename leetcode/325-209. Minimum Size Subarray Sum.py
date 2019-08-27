# 209. Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        i, j = 0, -1
        ans, cur_sum = float('inf'), 0
        
        while j < len(nums) - 1:
            if i == j or cur_sum < s:
                j += 1
                cur_sum += nums[j]
            else:
                ans = min(ans, j-i)
                cur_sum -= nums[i]
                i += 1
        
        return ans

print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))