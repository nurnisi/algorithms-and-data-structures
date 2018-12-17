# 15. 3Sum
from collections import defaultdict
class Solution:
    # TLE at test # 311 out of 313
    def threeSum(self, nums):
        n = len(nums)
        dic = defaultdict(set)
        d = {}
        for i in range(n):
            dic[nums[i]].add(i)
            # d.setdefault(nums[i], []).append(i)
        ans = []
        table = set()
        for i in range(n):
            for j in range(i+1, n):
                k = -nums[i]-nums[j]
                if k in dic:
                    s = dic.get(k).copy()
                    s.add(i)
                    s.add(j)
                    arr = [k, nums[i], nums[j]]
                    arr.sort()
                    key = ''.join(map(str, arr))
                    if len(s) >= 3 and key not in table:
                        ans.append(arr)
                        table.add(key)
        return ans

    def threeSum2(self, nums):
        ans, n = [], len(nums)
        nums.sort()
        for i in range(n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                    
        return ans
        
sol = Solution()
print(sol.threeSum2([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum2([0,0,0]))