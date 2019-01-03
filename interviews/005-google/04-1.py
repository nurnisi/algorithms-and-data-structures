def solution(A):
    n = len(A)
    minK = []
    for i in range(n):
        oddMinK = evenMinK = None
        for j in range(i+1, n):
            if not oddMinK and A[i] < A[j]: 
                oddMinK = j
            elif oddMinK and A[i] < A[j] and A[j] - A[i] < A[oddMinK] - A[i]:
                oddMinK = j

            if not evenMinK and A[i] > A[j]:
                evenMinK = j
            elif evenMinK and A[i] > A[j] and A[i] - A[j] < A[i] - A[evenMinK]:
                evenMinK = j
        minK.append((oddMinK, evenMinK))

    isReachable = [(False, False)] * (n-1) + [(True, True)]
    count = 1
    for i in range(n-2, -1, -1):
        oddMinK, evenMinK = minK[i]
        odd = even = False
        if oddMinK:
            odd = isReachable[oddMinK][1]
        if evenMinK:
            even = isReachable[evenMinK][0]
        if odd:
            count += 1
        isReachable[i] = (odd, even)

    return count

print(solution([10,13,12,14,15]))
print(solution([10,11,14,11,10]))
print(solution([3, 2, 1000]))