def longest_equal_subarray2(A):
    longest = cnt = 0
    n = len(A)

    for i in range(n):
        for j in range(i, n):
            cnt += 1 if A[j] else -1
            if cnt == 0:
                longest = max(longest, j - i + 1)
    
    return longest

def longest_equal_subarray(nums):
        d = {0: -1}
        sm = ans = 0
        
        for i, x in enumerate(nums):
            sm += 1 if x else -1
            if sm in d:
                ans = max(ans, i - d[sm])
            else:
                d[sm] = i
        
        return ans

print(longest_equal_subarray([1,0,1,1,0,0,0,0,1]))