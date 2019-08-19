# 1011. Capacity To Ship Packages Within D Days
class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            tot, res = 0, 1
            for wt in weights:
                if tot + wt > mid:
                    res += 1
                    tot = wt
                else:
                    tot += wt
            if res <= D:
                hi = mid
            else:
                lo = mid + 1

        return lo

print(Solution().shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))