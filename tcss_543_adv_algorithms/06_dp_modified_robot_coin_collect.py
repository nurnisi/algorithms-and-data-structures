def robotCoinCollect(A):
    l = len(A)

    DPCoins = [[0 for j in range(l)] for i in range(l)]
    DPDirs = [[0 for j in range(l)] for i in range(l)]

    # fill first row
    row = 0
    for col in range(1,l):
        DPCoins[row][col] = DPCoins[row][col-1] + A[row][col]

    # fill first column
    col = 0
    DPCoins[1][col] = A[1][col]
    for row in range(2,l):
        DPCoins[row][col] = DPCoins[row-1][col] + A[row][col]*2
    
    # fill second row
    row = 1
    for col in range(1,l):
        if DPCoins[row][col-1] > DPCoins[row-1][col]:
            DPCoins[row][col] = DPCoins[row][col-1] + A[row][col]
        else:
            DPCoins[row][col] = DPCoins[row-1][col] + A[row][col]
            DPDirs[row][col] = 1

    # fill the rest
    for row in range(2,l):
        for col in range(1,l):
            if DPCoins[row][col-1] > DPCoins[row-1][col]:
                DPCoins[row][col] = DPCoins[row][col-1] + A[row][col]
            else:
                if DPDirs[row-1][col] >= 1:
                    DPCoins[row][col] = DPCoins[row-1][col] + A[row][col]*2
                else:
                    DPCoins[row][col] = DPCoins[row-1][col] + A[row][col]
                DPDirs[row][col] = DPDirs[row-1][col] + 1

    [print(row) for row in DPCoins]
    print()
    [print(row) for row in DPDirs]

    return DPCoins[-1][-1]

def robotCoinCollect1(A):
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
    [1,0,1,0],
    [0,1,0,1],
    [0,0,1,0]
]

B = [
    [0,0,0,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,1,0],
    [0,0,0,0,1,0],
    [0,0,0,0,1,0],
    [0,0,0,0,1,0],
]

print(robotCoinCollect(B))
