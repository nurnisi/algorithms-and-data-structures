# 892. Surface Area of 3D Shapes

class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area, l = 0, len(grid)
        sides = [[-1,0], [0,1], [1,0], [0,-1]]
        for i in range(l):
            for j in range(l):
                if grid[i][j]:
                    for s in sides:
                        if (i + s[0] < 0 or i + s[0] > l-1 
                            or j + s[1] < 0 or j + s[1] > l-1):
                            area += grid[i][j]
                        elif grid[i+s[0]][j+s[1]] < grid[i][j]:
                            area += grid[i][j] - grid[i+s[0]][j+s[1]]
                    area += 2
                
        return area

    def surfaceArea2(self, grid):
        N = len(grid)
        area = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    area += 2
                    for ni, nj in ((i-1, j), (i, j+1), (i+1, j), (i, j-1)):
                        nval = 0
                        if 0 <= ni < N and 0 <= nj < N:
                            nval = grid[ni][nj]
                        area += max(grid[i][j] - nval, 0)

        return area
                        
                        
