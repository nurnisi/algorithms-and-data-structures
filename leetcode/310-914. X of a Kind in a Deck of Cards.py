# 914. X of a Kind in a Deck of Cards
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnt = list(collections.Counter(deck).values())
        i, n, minim = 2, len(cnt), min(cnt)
        
        while i <= minim:
            j = 0
            while j < n and cnt[j] % i == 0:
                j += 1
            if j == n:
                return True
            i += 1
            
        return False
            
            
        