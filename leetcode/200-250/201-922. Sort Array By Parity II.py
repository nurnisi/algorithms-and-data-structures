# 922. Sort Array By Parity II
class Solution:
    def sortArrayByParityII2(self, A):
        ans = A.copy()
        even, odd = 0, 1
        for i in A:
            if i % 2 == 0:
                ans[even] = i
                even += 2
            else:
                ans[odd] = i
                odd += 2
        
        return ans

    def sortArrayByParityII(self, A):
        even, odd, n = 0, 1, len(A)
        while even < n and odd < n:
            if A[even] % 2 == 1 and A[odd] % 2 == 0: A[even], A[odd] = A[odd], A[even]
            if A[even] % 2 == 0: even += 2
            if A[odd] % 2 == 1: odd += 2
        return A

sol = Solution()
print(sol.sortArrayByParityII([4,2,5,7]))