# 1009. Complement of Base 10 Integer
class Solution:
    def bitwiseComplement3(self, N: int) -> int:
        return int(''.join([str(int(x) ^ 1) for x in bin(N)[2:]]), 2)

    def bitwiseComplement2(self, N: int) -> int:
        X = 1
        while N > X: X = X * 2 + 1
        return X - N

    def bitwiseComplement(self, N: int) -> int:
        X = 1
        while N > X: X = X * 2 + 1
        return X ^ N

print(Solution().bitwiseComplement(10))