# 119. Pascal's Triangle II
class Solution:
    def getRow(self, rowIndex: 'int') -> 'List[int]':
        if rowIndex == 0: return [1]
        elif rowIndex == 1: return [1, 1]
        row, r = [1, 1], 1
        while r <= rowIndex:
            row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
            r += 1
        return row

sol = Solution()
print(sol.getRow(5))