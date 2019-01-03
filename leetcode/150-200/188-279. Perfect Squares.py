# 279. Perfect Squares
from math import sqrt
class Solution:
    # TLE
    def numSquares(self, n):
        # generate all perfect squares up to n
        ps = [i*i for i in range(1, int(sqrt(n))+1)]

        # dp
        dp = [0] + [float('inf')]*(n)
        for i in range(1, n+1):
            for j in ps:
                if  j <= i:
                    dp[i] = min(dp[i-j]+1, dp[i])
        print(ps, dp)
        return dp[n]

sol = Solution()
print(sol.numSquares(8285))
print(sol.numSquares(6730))
print(sol.numSquares(1103))