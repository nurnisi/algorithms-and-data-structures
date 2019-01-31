# 565. Array Nesting
class Solution:
    def arrayNesting(self, nums):
        sets, l = [], [0] * len(nums)
        for i in range(len(nums)):
            for s in sets:
                if nums[i] in s:
                    l[i] = len(s)
                    break
            if not l[i]:
                s = set()
                j = i
                while nums[j] not in s:
                    s.add(nums[j])
                    j = nums[j]
                l[i] = len(s)
                if len(s) > 1: sets.append(s)
        return max(l)

sol = Solution()
print(sol.arrayNesting([5,4,0,3,1,6,2]))