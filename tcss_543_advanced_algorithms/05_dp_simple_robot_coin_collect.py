def robotCoinCollect(A):
    DP = [[0 for j in range(len(A[0]))] for i in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A[0])):
            if i > 0 and j > 0:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1]) + A[i][j]
            elif i == 0:
                DP[i][j] = DP[i][j-1] + A[i][j]
            elif j == 0:
                DP[i][j] = DP[i-1][j] + A[i][j]
    [print(row) for row in DP]
    return DP[-1][-1]

A = [
    [0,0,1,0],
    [0,0,1,0],
    [0,1,0,1],
    [0,0,1,0]
]

print(robotCoinCollect(A))
