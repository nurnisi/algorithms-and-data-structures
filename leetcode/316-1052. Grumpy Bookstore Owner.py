# 1052. Grumpy Bookstore Owner
class Solution:
    def maxSatisfied(self, C: List[int], G: List[int], X: int) -> int:
        hi = cur = sum(C[:X]) + sum(C[i] for i in range(X, len(C)) if G[i] == 0)
        
        for i in range(X, len(C)):
            if G[i] == 1:
                cur += C[i]
            if G[i-X] == 1:
                cur -= C[i-X]
            hi = max(hi, cur)
            
        return hi