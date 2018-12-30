# 36. Valid Sudoku
import collections
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # rows
        for row in board:
            count = collections.Counter(row)
            flag = self.checkValidity(count)
            if not flag: return flag 
        
        # columns
        for i in range(9):
            count = collections.defaultdict(int)
            for j in range(9):
                count[board[j][i]] += 1
            flag = self.checkValidity(count)
            if not flag: return flag

        # boxes
        for i in range(3):
            for j in range(3):
                count = collections.defaultdict(int)
                for k in range(3):
                    for l in range(3):
                        count[board[i*3+k][j*3+l]] += 1
                flag = self.checkValidity(count)
                if not flag: return flag

        return True

    def checkValidity(self, count):
        for c in count:
                if c != '.' and count[c] > 1:
                    return False
        return True

sol = Solution()
print(sol.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))

print(sol.isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))