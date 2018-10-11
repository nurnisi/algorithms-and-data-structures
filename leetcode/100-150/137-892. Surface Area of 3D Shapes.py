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
