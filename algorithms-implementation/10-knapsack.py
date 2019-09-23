"""
Given weights and values of n items, we need to put these items
in a knapsack of capacity W to get the maximum total value in the knapsack.

items = {{60, 10}, {100, 20}, {120, 30}} => (value, weight)
W = 50;
"""

# Fractional Knapsack: Greedy
def knapsack_fractional(items, W):
    cap = val = 0
    
    for v, w in sorted(items, key=lambda x: x[0]/x[1], reverse=True):
        if cap + w >= W:
            return val + v//w * (W - cap)
        val, cap = val+v, cap+w
    
    return val

wt = [10, 40, 20, 30] 
val = [60, 40, 100, 120] 
capacity = 50

print(knapsack_fractional(zip(val, wt), capacity))

# 0-1 Knapsack: DP
def knapsack_0_1(wt, val, W):
    n = len(wt)
    dp = [[0] * (W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        w = wt[i-1]
        for j in range(1, W+1):
            if j - w >= 0:
                dp[i][j] = max(val[i-1] + dp[i-1][j-w], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][W]

val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50

print(knapsack_0_1(wt, val, W))

# Unbounded Knapsack: DP
def knapsack_unbounded(wt, val, W):
    n = len(wt)
    dp = [0] * (W+1)

    for w in range(1, W+1):
        for i, cw in enumerate(wt):
            if w >= cw:
                dp[w] = max(dp[w], dp[w-cw] + val[i])
        
    return dp[W]
    
W = 100
val  = [1, 30]
wt = [1, 50]

print(knapsack_unbounded(wt, val, W))

W = 8
val = [10, 40, 50, 70]
wt = [1, 3, 4, 5]

print(knapsack_unbounded(wt, val, W))