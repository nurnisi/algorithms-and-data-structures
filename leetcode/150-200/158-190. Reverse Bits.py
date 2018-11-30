# 190. Reverse Bits
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[:1:-1] + "0"*(32-len(bin(n))+2), 2)


sol = Solution()
print(sol.reverseBits(43261596))