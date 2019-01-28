# 977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, A):
        return sorted([i ** 2 for i in A])

sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))