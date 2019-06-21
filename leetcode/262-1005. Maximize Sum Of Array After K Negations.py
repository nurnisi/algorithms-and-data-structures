# 1005. Maximize Sum Of Array After K Negations
class Solution:
    def largestSumAfterKNegations(self, A, K: int) -> int:
        A.sort()
        i = 0
        while A[i] < 0 and i < K:
            A[i] = -A[i]
            i += 1
            
        if i < K and (K - i) % 2:
            if A[i - 1] < A[i]: i -= 1
            A[i] = -A[i]

        return sum(A)

print(Solution().largestSumAfterKNegations([-2,9,9,8,4], 5))