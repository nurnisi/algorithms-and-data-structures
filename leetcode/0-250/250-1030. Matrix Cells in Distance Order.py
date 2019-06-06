# 1030. Matrix Cells in Distance Order
from collections import deque

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        matrix = [[0] * C for i in range(R)]
        matrix[r0][c0] = 1

        queue = deque()
        queue.append([r0, c0])

        ans = []
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        
        while queue:
            r1, c1 = queue.popleft()
            ans.append([r1, c1])
            
            for r, c in dirs:
                if 0 <= r1 + r < R and 0 <= c1 + c < C and not matrix[r1 + r][c1 + c]:
                    matrix[r1 + r][c1 + c] = 1
                    queue.append([r1 + r, c1 + c])
            
        return ans
        
print(Solution().allCellsDistOrder(2, 3, 1, 2))

