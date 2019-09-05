# 79. Word Search
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recurs(i, j, k):
            if k == s or self.flag:
                self.flag = True
                return True
            if 0 <= i < m and 0 <= j < n \
                and board[i][j] == word[k] \
                and not visited[i][j]:
                ans = []
                visited[i][j] = True
                for di, dj in dirs:
                    ans.append(recurs(i+di, j+dj, k+1))
                visited[i][j] = False
                return any(ans)
            return False
        
        m, n, s = len(board), len(board[0]), len(word)
        dirs = ((-1,0), (0,1), (1,0), (0,-1))
        visited = [[False] * n for _ in range(m)]
        self.flag = False
        
        for i in range(m):
            for j in range(n):
                recurs(i, j, 0)
                if self.flag:
                    return True
        return False
                        
                        
        