# 875. Koko Eating Bananas
import math
class Solution:
    def minEatingSpeed2(self, piles, H: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            res = 0
            for p in piles:
                res += math.ceil(p / mid)
            if res <= H:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            m = (lo + hi) // 2
            if sum((p + m - 1) // m for p in piles) > H: lo = m + 1
            else: hi = m
        return lo

print(Solution().minEatingSpeed([312884470], 968709470))