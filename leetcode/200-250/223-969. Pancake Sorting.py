# 969. Pancake Sorting
class Solution:
    def pancakeSort2(self, A):
        ans, n = [], len(A)
        B = sorted(range(1, n+1), key=lambda i: -A[i-1])
        
        for i in B:
            for f in ans:
                if i <= f:
                    i = f + 1 - i
            ans.extend([i, n])
            n -= 1
        
        return ans
    
    def pancakeSort(self, A):
        res = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i+1, x])
            A = A[:i:-1] + A[:i]
        return res

sol = Solution()
print(sol.pancakeSort2([3,2,4,1]))
