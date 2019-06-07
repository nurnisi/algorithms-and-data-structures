# 1009. Complement of Base 10 Integer
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int(''.join([str(int(x) ^ 1) for x in bin(N)[2:]]), 2)

print(Solution().bitwiseComplement(10))