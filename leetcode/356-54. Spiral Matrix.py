# 54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix):
        if not matrix: return matrix
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        ans = []
        
        dirs = ((0,1), (1,0), (0,-1), (-1,0))
        cur = 0
        
        i = j = 0
        while len(ans) < m * n:
            if not visited[i][j]:
                ans.append(matrix[i][j])
                visited[i][j] = True
            
            di, dj = dirs[cur]
            ii, jj = i+di, j+dj
            if ii<0 or ii>=m or jj<0 or jj>=n or visited[ii][jj]:
                cur = (cur+1) % 4
            
            di, dj = dirs[cur]
            i, j = i+di, j+dj
        
        return ans