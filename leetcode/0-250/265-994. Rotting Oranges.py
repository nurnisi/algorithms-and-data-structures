# 994. Rotting Oranges
from collections import deque
class Solution:
    def orangesRotting(self, grid) -> int:
        rotten = deque([])
        freshCnt, n, m = 0, len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2: rotten.append((i, j))
                elif grid[i][j] == 1: freshCnt += 1
        
        if freshCnt == 0: return 0
        
        time = -1
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while rotten:
            size = len(rotten)
            for _ in range(size):
                r, c = rotten.popleft()
                for rd, cd in dirs:
                    if 0 <= r + rd < len(grid) \
                        and 0 <= c + cd < len(grid[0]) \
                        and grid[r + rd][c + cd] == 1:
                        rotten.append((r + rd, c + cd))
                        grid[r + rd][c + cd] = 2
                        freshCnt -= 1
            time += 1
            
        return time if freshCnt == 0 else -1
                        
print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))