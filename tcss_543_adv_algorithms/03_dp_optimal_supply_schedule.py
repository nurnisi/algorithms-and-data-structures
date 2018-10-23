def optimal_supply_schedule(supplies, r, c):
    # find optimal schedule
    dp = [0] * len(supplies)
    for i in range(1, len(supplies)):
        if i < 4:
            dp[i] = dp[i - 1] + supplies[i] * r
        else:
            dp[i] = min(dp[i - 4] + c * 4, dp[i - 1] + supplies[i] * r)

    #backtrack optimal schedule
    sc = ['B' for _ in supplies]
    i = len(supplies) - 1
    while i > 0:
        if dp[i] - supplies[i] == dp[i-1]:
            sc[i] = 'A'
            i -= 1
        else:
            i -= 4
    print(dp)
    print(sc)

optimal_supply_schedule([0,11,9,9,12,12,12,12,9,9,11], 1, 10)