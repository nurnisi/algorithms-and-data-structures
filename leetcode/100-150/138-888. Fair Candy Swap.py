# 888. Fair Candy Swap

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        hmap = {}
        for i in A:
            hmap[i] = hmap.get(i, 1)

        sumA, sumB = sum(A), sum(B)
        half = (sumA + sumB) / 2
        for j in B:
            i = half - sumB + j
            if i in hmap:
                return [i, j]

        