# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        p1, p2 = 1, 2
        for i in range(n-2):
            p1, p2 = p2, p1 + p2
        
        return p2