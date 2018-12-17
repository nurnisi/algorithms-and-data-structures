# 62. Unique Paths
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

    def uniquePaths(self, m, n):
        grid = [[1 for _ in range(n)] for _ in range(m)]
            
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[-1][-1]
        
