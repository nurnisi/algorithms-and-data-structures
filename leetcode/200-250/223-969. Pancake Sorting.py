# 969. Pancake Sorting
class Solution:
    def pancakeSort(self, A):
        ans, n = [], len(A)
        B = sorted(range(1, n+1), key=lambda i: -A[i-1])
        
        for i in B:
            for f in ans:
                if i <= f:
                    i = f + 1 - i
            ans.extend([i, n])
            n -= 1
        
        return ans

sol = Solution()
print(sol.pancakeSort([3,2,4,1]))
