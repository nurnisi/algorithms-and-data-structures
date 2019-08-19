# 914. X of a Kind in a Deck of Cards
class Solution:
    def hasGroupsSizeX2(self, deck: List[int]) -> bool:
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

    def hasGroupsSizeX3(self, deck: List[int]) -> bool:
        counts = list(collections.Counter(deck).values())
        
        cur_gcd = counts[0]
        while counts:
            cur_gcd = self.gcd(cur_gcd, counts.pop())
        
        return cur_gcd > 1
        
    def gcd(self, a, b):
        if b == 0: return a
        return self.gcd(b, a % b)

import functools
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a, b):
            while b > 0: a, b = b, a % b
            return a
        counts = collections.Counter(deck).values()
        return functools.reduce(gcd, counts) > 1
            
        
            
            
        