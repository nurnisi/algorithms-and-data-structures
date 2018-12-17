# 62. Unique Paths
from math import factorial
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[0 for _ in range(n)] for _ in range(m)]
        grid[0][:] = [1 for _ in range(n)]
        for j in range(m): grid[j][0] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[-1][-1]

    # short
    def uniquePaths2(self, m, n):
        grid = [[1 for _ in range(n)] for _ in range(m)]
            
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[-1][-1]

    # optimized space complexity
    def uniquePaths3(self, m, n):
        top = bottom = [1 for _ in range(n)]
        for _ in range(1, m):
            for j in range(1, n):
                bottom[j] = bottom[j-1] + top[j]
                top = bottom
        
        return top[-1]

    # optimized space complexity 2
    def uniquePaths4(self, m, n):
        arr = [1 for _ in range(n)]
        for _ in range(1, m):
            for j in range(1, n):
                arr[j] += arr[j-1]
        
        return arr[-1]

    # O(1) math solution
    def uniquePaths5(self, m, n):
        return factorial(m+n-2) / (factorial(m-1) * factorial(n-1))

        
