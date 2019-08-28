# 941. Valid Mountain Array
class Solution:
    def validMountainArray2(self, A: List[int]) -> bool:
        if len(A) < 3 or A[0] > A[1]:
            return False
        
        cnt = 0
        i = 1
        while i < len(A)-1:
            if A[i-1] == A[i]:
                return False
            if A[i-1] < A[i] > A[i+1]:
                cnt += 1
            i += 1
        
        return cnt == 1 and A[-2] > A[-1]

    def validMountainArray(self, A: List[int]) -> bool:
        i, j, n = 0, len(A)-1, len(A)
        while i+1 < n and A[i] < A[i+1]: i += 1
        while j > 0 and A[j-1] > A[j]: j -= 1
        return 0 < i == j < n-1

print(Solution().validMountainArray([14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3]))
            
            