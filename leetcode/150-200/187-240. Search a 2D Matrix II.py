# 240. Search a 2D Matrix II
class Solution:
    # binary search O(nlogn)
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for m in matrix:
            l, r = 0, len(m)
            while l < r:
                mid = (l+r)//2
                if m[mid] == target:
                    return True
                if target > m[mid]:
                    l = mid + 1
                else:
                    r = mid
        
        return False

    # O(m+n)
    def searchMatrix2(self, matrix, target):
        if not matrix: return False
        row, col = 0, len(matrix[0])-1
        while row < len(matrix) and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
        return False

sol = Solution()
print(sol.searchMatrix2([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 20))
print(sol.searchMatrix2([[-5]], -5))