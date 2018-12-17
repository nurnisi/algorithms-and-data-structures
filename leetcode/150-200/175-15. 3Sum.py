# 15. 3Sum
from collections import defaultdict
class Solution:
    # TLE at test # 311
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
        
sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum([0,0,0]))