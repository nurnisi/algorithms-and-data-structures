# 442. Find All Duplicates in an Array
import collections
class Solution:
    def findDuplicates(self, nums):
        return [k for k, v in collections.Counter(nums).items() if v > 1]

sol = Solution()
print(sol.findDuplicates([4,3,2,7,8,2,3,1]))
        