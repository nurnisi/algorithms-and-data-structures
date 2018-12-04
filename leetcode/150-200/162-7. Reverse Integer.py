# 7. Reverse Integer
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a, ans = abs(x), 0
        while a:
            ans = ans * 10 + a % 10
            a //= 10
        
        if ans > (2**31-1): return 0
        elif x < 0: return -ans
        else: return ans