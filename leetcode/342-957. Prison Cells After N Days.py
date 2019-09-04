# 957. Prison Cells After N Days
class Solution:
    def prisonAfterNDays(self, cells, N: int):
        d = {}
        rep = 0
        cellCopy = cells.copy()
        
        while rep < N:
            curCells = [0] * 8
            strCells = ''.join(map(str, cellCopy))
            if strCells in d:
                break
            else:
                for i in range(1, 7):
                    curCells[i] = cellCopy[i-1] ^ cellCopy[i+1] ^ 1
                d[strCells] = curCells.copy()
            cellCopy = curCells.copy()
            rep += 1
        
        if 1 < rep != N:
            cellCopy = cells.copy()
            rem = N%(rep-1)
            for _ in range(rem):
                cellCopy = d[''.join(map(str, cellCopy))].copy()
                
        return cellCopy

    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def nextDay(cells):
            return [int(i>0 and i<7 and cells[i-1]==cells[i+1]) for i in range(8)]
        
        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                N %= seen[c] - N
            seen[c] = N
            
            if N >= 1:
                N -= 1
                cells = nextDay(cells)
        
        return cells
    
# print(Solution().prisonAfterNDays([0,1,0,1,1,0,0,1], 7))
# print(Solution().prisonAfterNDays([0,1,0,1,1,0,0,1], 1))
# print(Solution().prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000))
# print(Solution().prisonAfterNDays([0,0,1,0,0,1,0,0], 44640906))
print(Solution().prisonAfterNDays([0,0,1,1,1,1,0,0], 8))