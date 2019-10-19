def balanced_sales(A):
    n = len(A)
    left, right = [0] * n, [0] * n

    for i in range(1, n):
        left[i] = left[i-1] + A[i-1]
        right[n-i-1] = right[n-i] + A[n-i]
    
    for i in range(n):
        if left[i] == right[i]:
            return i

    return 0

print(balanced_sales([1,2,3,4,6]))
print(balanced_sales([1,2,3,3]))

