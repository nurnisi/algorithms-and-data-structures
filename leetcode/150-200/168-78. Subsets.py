# 78. Subsets
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans, stack, n = [[]], [], len(nums)
        def helper(cur):
            for i in range(cur, n):
                stack.append(nums[i])
                ans.append(stack.copy())
                helper(i + 1)
                stack.pop()
        helper(0)
        return ans
                