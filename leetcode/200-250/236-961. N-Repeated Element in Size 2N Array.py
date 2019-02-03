# 961. N-Repeated Element in Size 2N Array
import collections
class Solution:
    def repeatedNTimes2(self, A):
        for k, v in collections.Counter(A).items():
            if v > 1: return k

    def repeatedNTimes(self, A):
        s = set()
        for i in A:
            if i in s:
                return i
            s.add(i)


sol = Solution()
print(sol.repeatedNTimes([1,2,3,3]))