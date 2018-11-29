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
        