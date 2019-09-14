# 289. Game of Life
class Solution:
    def gameOfLife2(self, board) -> None:
        rows, cols = len(board), len(board[0])
        nextState = [row[:] for row in board]
        dirs = ((0,1), (1,0), (-1,0), (0,-1), (-1,-1), (-1,1), (1,-1), (1,1))
        
        for i in range(rows):
            for j in range(cols):
                nbrs = 0
                for di, dj in dirs:
                    if 0 <= i+di < rows and 0 <= j+dj < cols:
                        nbrs += nextState[i+di][j+dj]
                
                if nextState[i][j] == 1 and (nbrs < 2 or nbrs > 3):
                    board[i][j] = 0
                elif nextState[i][j] == 0 and nbrs == 3:
                    board[i][j] = 1
                       
        return board

    def gameOfLife(self, board) -> None:
        rows, cols = len(board), len(board[0])
        dirs = ((0,1), (1,0), (-1,0), (0,-1), (-1,-1), (-1,1), (1,-1), (1,1))
        
        for i in range(rows):
            for j in range(cols):
                nbrs = 0
                for di, dj in dirs:
                    if 0 <= i+di < rows and 0 <= j+dj < cols and board[i+di][j+dj] > 0:
                        nbrs += 1
                board[i][j] = nbrs+10 if board[i][j] == 1 else -nbrs
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] > 0:
                    if 12 <= board[i][j] <= 13:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                elif board[i][j] <= 0:
                    if board[i][j] == -3:
                        board[i][j] = 1      
                    else:
                        board[i][j] = 0
        
        return board

print(Solution().gameOfLife([[1,0,0,0,0,1],[0,0,0,1,1,0],[1,0,1,0,1,0],[1,0,0,0,1,0],[1,1,1,1,0,1],[0,1,1,0,1,0],[1,0,1,0,1,1],[1,0,0,1,1,1],[1,1,0,0,0,0]]))