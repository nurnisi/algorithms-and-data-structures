# 1175. Prime Arrangements
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,float('inf')]
        ans = 1
        pcnt = 0
        while primes[pcnt] <= n:
            pcnt += 1
            
        ncnt = n - pcnt
        while pcnt > 0: 
            ans *= pcnt
            pcnt -= 1
            
        while ncnt > 0: 
            ans *= ncnt
            ncnt -= 1
            
        return ans % (10**9 + 7)