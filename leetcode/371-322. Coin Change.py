# 322. Coin Change
class Solution:
    def coinChange2(self, coins: List[int], amount: int) -> int:
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        for i in range(amount+1): dp[0][i] = float('inf')
        
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if j - coins[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]] + 1)
                    
        return -1 if dp[-1][-1] == float('inf') else dp[-1][-1]

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c]+1)
                    
        return -1 if dp[-1] == float('inf') else dp[-1]
                