# 204. Count Primes
class Solution:
    # time limit exceeded
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, count = 3, 0
        while i < n:
            if self.isPrime(i):
                count += 1
            i += 2
        return 0 if n == 1 else count + 1

    def getPrimes(self):
        max_int = 2_147_483_647
        primes = [2]
        i = 3
        while i <= max_int:
            if self.isPrime(i):
                primes.append(i)
            i += 1
        return primes

    def isPrime(self, n):
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    # approach: mark all non-prime integers
    def countPrimes2(self, n):
        if n <= 2: return 0
        primes = [1] * n
        primes[0], primes[1] = 0, 0
        i = 2
        while i * i <= n:
            j = 2
            if primes[i]:
                while i * j < n:
                    primes[i * j] = 0
                    j += 1
            i += 1
        return sum(primes)
    
    # approach: mark all non-prime integers - optimized
    def countPrimes3(self, n):
        if n <= 2: return 0
        primes = [1] * n
        primes[0], primes[1] = 0, 0
        i = 2
        while i * i <= n:
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = 0
            i += 1
        return sum(primes)

    # approach: mark all non-prime integers - syntax sugar
    def countPrimes4(self, n):
        if n <= 2: return 0
        primes = [1] * n
        primes[0], primes[1] = 0, 0
        i = 2
        while i * i <= n:
            if primes[i]:
                primes[i*i:n:i] = [0] * len(primes[i*i:n:i])
            i += 1
        return sum(primes)

cp = Solution()
print(cp.countPrimes4(474844))