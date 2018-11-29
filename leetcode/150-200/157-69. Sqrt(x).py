# 69. Sqrt(x)
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x: return 0
        root = x // 2
        while root * root >= x:
            root //= 2
            
        while root * root <= x:
            root += 1
            
        return root if root * root == x else root - 1
    
    # binary search O(logn)
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 1, x
        while True:
            mid = (right + left) // 2
            sq1, sq2 = mid ** 2, (mid + 1) ** 2
            if sq1 <= x and sq2 > x:
                return mid
            elif sq1 > x:
                right = mid
            else:
                left = mid
        