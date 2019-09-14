# 289. Game of Life
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
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