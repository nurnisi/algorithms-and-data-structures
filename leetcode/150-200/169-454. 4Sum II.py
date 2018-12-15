# 454. 4Sum II
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