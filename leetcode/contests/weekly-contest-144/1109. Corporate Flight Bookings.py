# 1109. Corporate Flight Bookings
import collections
class Solution:
    def corpFlightBookings(self, bookings, n: int):
        ans = [0] * n
        cnt = {}
        for i, j, k in bookings:
            key = str.format("{}-{}", i, j)
            ii, jj, kk = cnt.get(key, (0, 0, 0))
            cnt[key] = (i, j, k + kk)

        for i, j, k in cnt.values():
            for l in range(i-1, j):
                ans[l] += k
                
        return ans

print(Solution().corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], n = 5))