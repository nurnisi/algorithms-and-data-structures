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

    def sortArrayByParityII3(self, A):
        ans = [0] * len(A)
        j = 0
        for i in A:
            if i % 2 == 0:
                ans[j] = i
                j += 2

        j = 1
        for i in A:
            if i % 2 == 1:
                ans[j] = i
                j += 2
        
        return ans

    def sortArrayByParityII4(self, A):
        ans = [0] * len(A)
        ans[::2] = (i for i in A if not i % 2)
        ans[1::2] = (i for i in A if i % 2)
        return ans

    def sortArrayByParityII5(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A

sol = Solution()
print(sol.sortArrayByParityII5([4,2,5,7]))