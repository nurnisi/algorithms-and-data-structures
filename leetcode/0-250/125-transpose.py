def transpose(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    tran = [[0 for i in range(len(A))] for j in range(len(A[0]))]

    for i in range(len(A)):
        for j in range(len(A[0])):
            tran[j][i] = A[i][j]

    return tran
    
print(transpose([[1,2,3],[4,5,6]]))