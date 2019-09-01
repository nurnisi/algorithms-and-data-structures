# 1175. Prime Arrangements
import functools
class Solution:
    def numPrimeArrangements2(self, n: int) -> int:
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

    def numPrimeArrangements(self, n: int) -> int:
        def isPrime(x):
            i = 2
            while i*i <= x:
                if x%i == 0:
                    return 0
                i += 1
            return 1

        primes = 0
        for i in range(2, n+1):
            primes += isPrime(i)
        
        return functools.reduce(lambda x,y: x*y, [1]+[i for i in range(1, primes+1)]) \
            * functools.reduce(lambda x,y: x*y, [1]+[i for i in range(1, n-primes+1)]) \
            % (10**9+7)

print(Solution().numPrimeArrangements(2))