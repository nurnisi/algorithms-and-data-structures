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

                
sol = Solution()
sol.gameOfLife([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
])
        
        