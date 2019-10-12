# 45. Jump Game II
class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        if n == 1: return 0
        
        ans = 1
        r, next_r = nums[0], 0
        for i, j in enumerate(nums[:-1]):
            next_r = max(next_r, i+j)
            if i == r:
                ans += 1
                r = next_r
        
        return ans
        


print(Solution().jump([2,3,1,1,4]))
print(Solution().jump([4,1,1,3,1,1,1]))