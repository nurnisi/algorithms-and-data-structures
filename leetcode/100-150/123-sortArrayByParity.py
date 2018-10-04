def sortArrayByParity(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    res = A[:]
    i, j = 0, len(A) - 1
    for num in A:
        if num % 2 == 0:
            res[i] = num
            i+=1
        else:
            res[j] = num
            j-=1
        
    return res

def sortArrayByParity2(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    i, j = 0, len(A) - 1
    while i < j:
        if A[i] % 2 == 1 and A[j] % 2 == 0:
            A[i], A[j] = A[j], A[i]
        if A[i] % 2 == 0:
            i+=1
        if A[j] % 2 == 1:
            j-=1
        
    return A

def sortArrayByParity3(A):
    A.sort(key = lambda x : x % 2)
    return A


print(sortArrayByParity3([3,5,6,4]))