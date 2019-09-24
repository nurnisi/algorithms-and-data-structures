# 907. Sum of Subarray Minimums
class Solution:
    # brute force: TLE
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        ans = 0
        for i in range(n):
            for j in range(i+1, n+1):
                ans += min(A[i:j])
        
        return ans % (10**9 + 7)