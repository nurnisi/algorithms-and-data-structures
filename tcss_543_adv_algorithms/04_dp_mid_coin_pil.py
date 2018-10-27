def mySolution(A):
    DP = [0] * (len(A) + 1)
    for i in range(len(A)):
        if i < 2:
            DP[i + 1] = max(DP[i], A[i]*2, A[i])
        else:
            DP[i + 1] = max(DP[i], DP[i-2] + A[i]*2, A[i] + DP[i-1])
    
    print(DP)
    return DP[len(A)]


def classSolution(A):
    n = len(A)
    V = [0] * n
    V[0] = A[0]*2
    V[1] = max(V[0], A[1]*2)
    V[2] = max(V[1], A[2]+V[0], A[2]*2)
    for i in range(3, n):
        V[i] = max(A[i]+V[i-2], V[i-1], A[i]*2+V[i-3])
    
    print(V)
    return V[n-1]

print(mySolution([4,5,10,7,8,2,3,1]))
print(mySolution([1,6,9,7]))

print(classSolution([4,5,10,7,8,2,3,1]))
print(classSolution([1,6,9,7]))