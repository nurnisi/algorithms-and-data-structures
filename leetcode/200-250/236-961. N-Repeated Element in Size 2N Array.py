# 961. N-Repeated Element in Size 2N Array
import collections
class Solution:
    def repeatedNTimes(self, A):
        for k, v in collections.Counter(A).items():
            if v > 1: return k

sol = Solution()
print(sol.repeatedNTimes([1,2,3,3]))