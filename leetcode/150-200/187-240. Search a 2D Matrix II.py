# 240. Search a 2D Matrix II
class Solution:
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

sol = Solution()
print(sol.searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 5))
print(sol.searchMatrix([[-5]], -5))