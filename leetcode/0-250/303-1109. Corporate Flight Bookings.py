# 1109. Corporate Flight Bookings
class Solution:
    def corpFlightBookings(self, bookings, n: int):
        res = [0] * (n + 1)
        for i, j, k in bookings:
            res[i-1] += k
            res[j] -= k
        for i in range(1, n):
            res[i] += res[i-1]
        return res[:-1]

print(Solution().corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], n = 5))