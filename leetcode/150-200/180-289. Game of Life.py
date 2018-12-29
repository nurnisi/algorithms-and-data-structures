# 289. Game of Life
class Solution:
    # brute force
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        temp = [[0]*(n+2)] + [[0] + row + [0] for row in board] + [[0]*(n+2)]
        dirs = ((-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1))

        for i in range(1, m+1):
            for j in range(1, n+1):
                nbrs = 0
                for d in dirs:
                    nbrs += temp[i + d[0]][j + d[1]]
                board[i-1][j-1] = self.nextState(board[i-1][j-1], nbrs)
    
    def nextState(self, cell, nbrs):
        if cell and 2 <= nbrs <= 3: return 1
        elif not cell and nbrs == 3: return 1
        return 0

    # in-place
    def gameOfLife2(self, board):
        dirs = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                nbrs = 0
                for d in dirs:
                    if 0 <= i+d[0] < m and 0 <= j+d[1] < n and board[i+d[0]][j+d[1]] > 0:
                        nbrs += 1
                if not board[i][j]: nbrs *= -1
                elif board[i][j] and not nbrs: nbrs = 1
                board[i][j] = nbrs
                
        for i in range(m):
            for j in range(n):
                board[i][j] = self.nextState2(board[i][j])

    def nextState2(self, cell):
        if 2 <= cell <= 3: return 1
        elif cell == -3: return 1
        return 0 
                
sol = Solution()
sol.gameOfLife2([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
])

sol.gameOfLife2([[1,0,0,0,0,1],[0,0,0,1,1,0],[1,0,1,0,1,0],[1,0,0,0,1,0],[1,1,1,1,0,1],[0,1,1,0,1,0],[1,0,1,0,1,1],[1,0,0,1,1,1],[1,1,0,0,0,0]])
        
        