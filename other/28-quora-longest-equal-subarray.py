def longest_equal_subarray(A):
    longest = cnt = 0
    n = len(A)

    for i in range(n):
        for j in range(i, n):
            cnt += 1 if A[j] else -1
            if cnt == 0:
                longest = max(longest, j - i + 1)
    
    return longest

print(longest_equal_subarray([1,0,1,1,0,0,0,0,1]))