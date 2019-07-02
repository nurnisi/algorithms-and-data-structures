# 1102. Path With Maximum Minimum Value
class Solution:
    def maximumMinimumPath2(self, A) -> int:
        s = set()
        for i in range(len(A)):
            for j in range(len(A[0])):
                s.add(A[i][j])
  
        arr = sorted(s)
        chset = set()
        for x in arr:
            chset.add(x)
            AC = [[0] * len(A[0]) for _ in range(len(A))]
            self.flag = False
            if not self.dfs(A, AC, chset, 0, 0, len(A), len(A[0])): return x
        
        return -1
    
    def dfs2(self, A, AC, chset, i, j, r, c):
        if i < 0 or i >= r or j < 0 or j >= c or A[i][j] in chset or AC[i][j] == 1:
            return False

        if (i == r - 1 and j == c - 1) or self.flag:
            return True
        
        AC[i][j] = 1
        for ii, jj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            self.flag |= self.dfs(A, AC, chset, i+ii, j+jj, r, c)
        return self.flag

    def maximumMinimumPath(self, A) -> int:
        arr = [[-1] * len(A[0]) for _ in range(len(A))]

        def dfs(i, j, mn):
            if 0 <= i < len(A) and 0 <= j < len(A[0]) :
                if arr[i][j] == -1:
                    arr[i][j] = max(mn, A[i][j])
                else:
                    arr[i][j] = min(mn, arr[i][j])
                mn = arr[i][j]

                for ii, jj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    dfs(i+ii, j+jj, mn)

        dfs(0, 0, 0)
        return arr[-1][-1]

        
print(Solution().maximumMinimumPath([[1,1,0,3,1,1],[0,1,0,1,1,0],[3,3,1,3,1,1],[0,3,2,2,0,0],[1,0,1,2,3,0]]))
print(Solution().maximumMinimumPath([[2,2,1,2,2,2],[1,2,2,2,1,2]]))
print(Solution().maximumMinimumPath([[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]))