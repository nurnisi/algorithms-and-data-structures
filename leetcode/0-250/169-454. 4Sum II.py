# 454. 4Sum II
import collections
class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ab = {}
        for a in A:
            for b in B:
                ab[a+b] = ab.get(a+b, 0) + 1
        
        count = 0
        for c in C:
            for d in D:
                count += ab.get(-c-d, 0)
                                   
        return count

    # short solution
    def fourSumCount2(self, A, B, C, D):
        ab = collections.Counter([a+b for a in A for b in B])
        return sum([ab[-c-d] for c in C for d in D])

sol = Solution()
print(sol.fourSumCount2([1,2], [-2,-1], [-1,2], [0,2]))