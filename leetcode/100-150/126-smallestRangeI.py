def smallestRangeI(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    A.sort()
    if A[len(A)-1] - A[0] - 2 * K > 0:
        return A[len(A)-1] - A[0] - 2 * K
    else: 
        return 0


print(smallestRangeI(A = [1,3,6], K = 3))