def forming_teams(players, k):
    players.sort()
    n = len(players)
    ans = 0

    for i in range(n-2):
        left, right = i + 1, n-1
        while left < right:
            if players[i] >= k:
                break
        
            cur_sum = players[i] + players[left] + players[right]
            if cur_sum == k:
                print(players[i], players[left], players[right])
                ans += 1
                left += 1
                right -= 1
            elif cur_sum < k:
                left += 1
            else:
                right -= 1

    return ans

print(forming_teams([1,2,3,4,5,6,7,8,9,10], 10))