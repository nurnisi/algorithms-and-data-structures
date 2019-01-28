# 977. Squares of a Sorted Array
class Solution:
    def sortedSquares2(self, A):
        return sorted([i ** 2 for i in A])

    def sortedSquares(self, A):
        l, r = 0, len(A) - 1
        A, ans = [i ** 2 for i in A], [0] * len(A)
        while l <= r:
            if A[l] > A[r]:
                ans[r - l] = A[l]
                l += 1
            else:
                ans[r - l] = A[r]
                r -= 1
        return ans

sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))