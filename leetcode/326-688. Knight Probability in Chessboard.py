# 688. Knight Probability in Chessboard
class Solution:
    # TLE
    def knightProbability2(self, N: int, K: int, r: int, c: int) -> float:
        inboard = [(r,c)]
        ans = 0
        i = 0
        moves = ((1,2), (2,1), (-1,2), (-2,1), (1,-2), (2,-1), (-1,-2), (-2,-1))
        
        while i < K and inboard:
            temp = []
            
            while inboard:
                cr, cc = inboard.pop()
                for mr, mc in moves:
                    if 0 <= mr+cr < N and 0 <= mc+cc < N:
                        temp.append((mr+cr, mc+cc))
            
            inboard = temp.copy()
            ans = len(inboard)
            i += 1
        
        return ans / (8**K)
    
    # MLE
    def knightProbability3(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0: return 1
        
        board = [[[] for _ in range(N)] for _ in range(N)]
        moves = ((1,2), (2,1), (-1,2), (-2,1), (1,-2), (2,-1), (-1,-2), (-2,-1))
        
        for rr in range(N):
            for cc in range(N):
                for mr, mc in moves:
                    if 0 <= mr+rr < N and 0 <= mc+cc < N:
                        board[rr][cc].append((mr+rr, mc+cc))
        
        inboard = [(r,c)]
        i = 0
        
        while i < K and inboard:
            temp = []
            
            while inboard:
                cr, cc = inboard.pop()
                temp += board[cr][cc]
            
            inboard = temp.copy()
            i += 1
        
        return len(inboard) / (8**K)

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        prevWays = [[0] * N for _ in range(N)]
        prevWays[r][c] = 1
        moves = ((1,2), (2,1), (-1,2), (-2,1), (1,-2), (2,-1), (-1,-2), (-2,-1))
        
        for _ in range(K):
            ways = [[0] * N for _ in range(N)]
            for cr in range(N):
                for cc in range(N):
                    for mr, mc in moves:
                        if 0 <= cr+mr < N and 0 <= cc+mc < N:
                            ways[cr][cc] += prevWays[cr+mr][cc+mc]/8
            prevWays = ways.copy()
        
        return sum(sum(row) for row in prevWays)
                
print(Solution().knightProbability(3,2,0,0))
            