# 565. Array Nesting
class Solution:
    def arrayNesting2(self, nums):
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

    def arrayNesting3(self, nums):
        seen, ans = set(), 0
        for i in range(len(nums)):
            if nums[i] not in seen:
                s, j, cnt = set(), i, 0
                while nums[j] not in s:
                    seen.add(nums[j])
                    s.add(nums[j])
                    j = nums[j]
                ans = max(ans, len(s))
        return ans

    def arrayNesting4(self, nums):
        seen, ans = [False] * len(nums), 0
        for i in range(len(nums)):
            if not seen[i]:
                j, cnt = nums[i], 1
                while nums[j] != nums[i]:
                    seen[j] = True
                    cnt += 1
                    j = nums[j]
                ans = max(ans, cnt)
        return ans

    def arrayNesting(self, nums):
        ans = 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                j, cnt = nums[i], 1
                while nums[j] != nums[i]:
                    cnt += 1
                    tmp = j
                    j = nums[j]
                    nums[tmp] = -1
            ans = max(ans, cnt)
        return ans

sol = Solution()
print(sol.arrayNesting([5,4,0,3,1,6,2]))