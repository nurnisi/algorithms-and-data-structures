# 279. Perfect Squares
from math import sqrt
class Solution:
    # dp
    def numSquares2(self, n):
        dp = [0] + [float('inf')]*(n)
        for i in range(1, n+1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i-j*j]+1, dp[i])
                j += 1

        return dp[n]

sol = Solution()
print(sol.numSquares2(12))
print(sol.numSquares(8285))
print(sol.numSquares(6730))
print(sol.numSquares2(1103))