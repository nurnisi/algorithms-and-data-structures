# 442. Find All Duplicates in an Array
import collections
class Solution:
    def findDuplicates2(self, nums):
        return [k for k, v in collections.Counter(nums).items() if v > 1]

    def findDuplicates3(self, nums):
        ans = set()
        i = 0
        while i < len(nums):
            while nums[i] != i + 1:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                if nums[nums[i] - 1] == nums[i]: 
                    ans.add(nums[i])
                    break            
            i += 1
        return list(ans)

    def findDuplicates(self, nums):
        ans = []
        for i in nums:
            if nums[abs(i) - 1] < 0: ans.append(abs(i))
            else: nums[abs(i) - 1] *= -1
        return ans

sol = Solution()
print(sol.findDuplicates([4,3,2,7,8,2,3,1]))
        