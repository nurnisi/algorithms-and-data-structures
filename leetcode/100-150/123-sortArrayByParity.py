class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = A[:]
        i, j = 0, len(A) - 1
        for num in A:
            if num % 2 == 0:
                res[i] = num
                i+=1
            else:
                res[j] = num
                j-=1
            
        return res


