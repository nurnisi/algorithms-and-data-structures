def dp_bullets_robots(X, F):
    n = len(X)
    opt = [0] * n
    for i in range(1,n):
        for j in range(1,n):
            if i >= j:
                opt[i] = max(opt[i-j] + min(X[i], F[j]), opt[i])
            else: break
    print(opt)

dp_bullets_robots([0,1,10,10,2], [0,1,2,4,8])

