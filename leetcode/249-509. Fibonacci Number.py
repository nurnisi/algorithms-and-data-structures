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

    def fib4(self, N: int) -> int:
        if N < 2: return N
        return self.fib(N - 1) + self.fib(N - 2)    

    F = [0] * 31
    def fib(self, N: int) -> int:
        if N < 2: return N
        prev = cur = 0
        if self.F[N - 2]: prev = self.F[N - 2]
        else:
            prev = self.fib(N - 2)
            self.F[N - 2] = prev
        
        if self.F[N - 1]: cur = self.F[N - 1]
        else:
            cur = self.fib(N - 1)
            self.F[N - 1] = cur

        return prev + cur
        


print(Solution().fib(7))