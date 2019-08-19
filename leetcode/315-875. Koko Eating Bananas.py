# 875. Koko Eating Bananas
import math
class Solution:
    def minEatingSpeed(self, piles, H: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            res = 0
            for p in piles:
                if mid == 0: 
                    print(lo, hi)
                res += math.ceil(p / mid)
            if res <= H:
                hi = mid
            else:
                lo = mid + 1
        return lo

print(Solution().minEatingSpeed([312884470], 968709470))