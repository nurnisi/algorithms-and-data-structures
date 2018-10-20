def optimal_supply_schedule(supplies, r, c):
    # find optimal schedule
    dp = [0] * (len(supplies) + 1)
    for i in range(len(supplies)):
        j = i + 1
        if j < 3:
            dp[j] = dp[j - 1] + supplies[i] * r
        else:
            dp[j] = min(dp[j - 4] + c * 4, dp[j - 1] + supplies[i] * r)

    #backtrack optimal schedule
    sc = ['B' for _ in supplies]
    i = len(supplies) - 1
    while i >= 0:
        if dp[i + 1] - supplies[i] == dp[i]:
            sc[i] = 'A'
            i -= 1
        else:
            i -= 4
    print(dp)
    print(sc)

optimal_supply_schedule([11,9,9], 1, 9)