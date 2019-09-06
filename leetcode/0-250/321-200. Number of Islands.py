# 200. Number of Islands
import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        dirs = ((0,1), (0,-1), (1,0), (-1,0))
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    q = collections.deque()
                    q.append((r, c))
                    grid[r][c] = '-1'
                    while q:
                        rr, cc = q.popleft()
                        for dr, dc in dirs:
                            if 0 <= rr+dr < len(grid) and 0 <= cc+dc < len(grid[0]) \
                                and grid[rr+dr][cc+dc] == '1':
                                q.append((rr+dr, cc+dc))
                                grid[rr+dr][cc+dc] = '-1'
                    ans += 1
        
        return ans
                        
                    