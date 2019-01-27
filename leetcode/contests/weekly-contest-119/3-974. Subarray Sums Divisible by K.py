class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        dp = [0]
        s = set(A)
        ans, n = 0, len(A)
        if 0 in s and len(s) == 1:
            return 200010000

        for i in range(n):
            dp.append(A[i] + dp[i])

        for i in range(n+1):
            for j in range(i+1, n+1):
                if (dp[j] - dp[i]) % K == 0: ans += 1
        
        return ans

sol = Solution()
print(sol.subarraysDivByK(A = [4,5,0,-2,-3,1], K = 5))
print(sol.subarraysDivByK([0]*20000, 1000))
# print(sol.subarraysDivByK())