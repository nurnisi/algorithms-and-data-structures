# 542. 01 Matrix
import collections
class Solution(object):
    # TLE
    def updateMatrix2(self, matrix):
        n, m = len(matrix), len(matrix[0])
        ans = [[float('inf')] * m for _ in range(n)]
        dirs = ((0,1), (1,0), (-1,0), (0,-1))
        
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    dist = 0
                    queue = collections.deque()
                    queue.append((r,c))
                    while queue:
                        size = len(queue)
                        for _ in range(size):
                            rr, cc = queue.popleft()
                            ans[rr][cc] = dist
                            for dr, dc in dirs:
                                if 0 <= rr+dr < n and 0 <= cc+dc < m \
                                    and matrix[rr+dr][cc+dc] == 1 \
                                    and dist+1 < ans[rr+dr][cc+dc]:
                                        queue.append((rr+dr, cc+dc))
                        dist += 1
            
        return ans

    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        q = collections.deque()
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    q.append((r,c))
                else:
                    matrix[r][c] = float('inf')
        
        dirs = ((0,1), (1,0), (-1,0), (0,-1))
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                if 0 <= r+dr < m and 0 <= c+dc < n \
                    and matrix[r+dr][c+dc] > matrix[r][c]+1:
                    q.append((r+dr, c+dc))
                    matrix[r+dr][c+dc] = matrix[r][c]+1
        
        return matrix