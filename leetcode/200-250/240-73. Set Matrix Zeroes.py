# 73. Set Matrix Zeroes
class Solution:
    def setZeroes2(self, matrix):
        if not matrix or not matrix[0]: return

        # check if 1st row and col has 0s
        n, m = len(matrix), len(matrix[0])
        fr = any(matrix[0][j] == 0 for j in range(m))
        fc = any(matrix[i][0] == 0 for i in range(n))

        # flag rows and cols that has 0s
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if i == 0 and j == 0: continue
                    matrix[i][0] = matrix[0][j] = 'z'

        # set rows to 0s
        for i in range(1, len(matrix)):
            if matrix[i][0] == 'z':
                matrix[i] = [0] * len(matrix[i])
        
        # set cols to 0s
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 'z':
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        
        # set 1st row and col to 0s
        if fr: matrix[0] = [0] * len(matrix[0])
        if fc: 
            for i in range(len(matrix)): matrix[i][0] = 0

        for row in matrix:
            print(row)

    def setZeroes3(self, matrix):
        n, m = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
                
        for r in range(n):
            for c in range(m):
                if r in rows or c in cols:
                    matrix[r][c] = 0
        
        for row in matrix:
            print(row)

    def setZeroes(self, matrix):
        n, m = len(matrix), len(matrix[0])
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    for i in range(n): matrix[i][c] = float('inf') if matrix[i][c] != 0 else 0
                    for j in range(m): matrix[r][j] = float('inf') if matrix[r][j] != 0 else 0
        
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == float('inf'): matrix[r][c] = 0

        for r in matrix: print(r)

sol = Solution()
print(sol.setZeroes([
    [1,1,1],
    [0,1,2]
]))
print(sol.setZeroes([
  [1,1,1],
  [1,0,1],
  [1,1,1]
]))
print(sol.setZeroes([
  [0,1,2,3],
  [3,4,5,2],
  [1,3,1,0]
]))