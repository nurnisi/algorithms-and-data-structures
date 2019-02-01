# 200. Number of Islands
from collections import deque
class Solution:
    # iterative: queue
    def numIslands2(self, grid):
        seen = [[0] * len(grid[0]) for _ in range(len(grid))]
        queue, dirs = deque(), ((0,-1), (0,1), (-1,0), (1,0))
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not seen[i][j]:
                    queue.append((i, j))
                    seen[i][j] = 1
                    while queue:
                        ci, cj = queue.popleft()
                        for di, dj in dirs:
                            if 0 <= ci + di < len(grid) and \
                                0 <= cj + dj < len(grid[0]) and \
                                not seen[ci + di][cj + dj] and \
                                grid[ci + di][cj + dj] == "1":
                                queue.append((ci + di, cj + dj))
                                seen[ci + di][cj + dj] = 1
                    islands += 1
        return islands

    # iterative: stack
    def numIslands3(self, grid):
        if not grid: return 0
        islands, n, m = 0, len(grid), len(grid[0])
        seen = [[0] * m for _ in range(n)]
        stack, dirs = [], ((0,-1), (0,1), (-1,0), (1,0))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not seen[i][j]:
                    stack.append((i, j))
                    seen[i][j] = 1
                    while stack:
                        ci, cj = stack.pop()
                        for di, dj in dirs:
                            cdi, cdj = ci + di, cj + dj
                            if 0 <= cdi < n and \
                                0 <= cdj < m and \
                                not seen[cdi][cdj] and \
                                grid[cdi][cdj] == "1":
                                stack.append((cdi, cdj))
                                seen[cdi][cdj] = 1
                    islands += 1
        return islands

    # recursive
    def numIslands(self, grid):
        if not grid: return 0
        islands, n, m = 0, len(grid), len(grid[0])
        seen = [[0] * m for _ in range(n)]
        dirs = ((0,-1),(0,1),(-1,0),(1,0))

        def helper(i, j):
            for di, dj in dirs:
                ci, cj = i + di, j + dj
                if 0 <= ci < n and 0 <= cj < m and \
                    grid[ci][cj] == "1" and not seen[ci][cj]:
                    seen[ci][cj] = 1
                    helper(ci, cj)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not seen[i][j]:
                    seen[i][j] = 1
                    helper(i, j)
                    islands += 1

        return islands

sol = Solution()
print(sol.numIslands([["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]))