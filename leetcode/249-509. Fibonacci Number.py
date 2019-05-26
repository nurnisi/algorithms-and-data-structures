# 509. Fibonacci Number
class Solution:
    def fib(self, N: int) -> int:
        F = [0, 1]
        for i in range(2, N + 1):
            F.append(F[i - 1] + F[i - 2])
        return F[N]

print(Solution().fib(5))