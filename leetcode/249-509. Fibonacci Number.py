# 509. Fibonacci Number
class Solution:
    def fib2(self, N: int) -> int:
        F = [0, 1]
        for i in range(2, N + 1):
            F.append(F[i - 1] + F[i - 2])
        return F[N]

    def fib3(self, N: int) -> int:
        if N < 2: return N
        prev, cur = 0, 1
        for i in range(2, N + 1):
            prev, cur = cur, prev + cur
        return cur

    def fib(self, N: int) -> int:
        if N < 2: return N
        return self.fib(N - 1) + self.fib(N - 2)    

print(Solution().fib(7))