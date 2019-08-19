# 605. Can Place Flowers
class Solution:
    def canPlaceFlowers(self, F: List[int], n: int) -> bool:
        F = [0] + F + [0]
        i = 1
        while n > 0 and i < len(F)-1:
            if F[i-1] == F[i] == F[i+1] == 0:
                n -= 1
                i += 2
            else:
                i += 1
        
        return n == 0