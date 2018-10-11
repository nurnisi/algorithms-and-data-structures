# 896. Monotonic Array
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 2:
            return True
        if A[0] <= A[-1]:
            for i in range(len(A)-1):
                if A[i] > A[i+1]:
                    return False
        else:
            for i in range(len(A)-1):
                if A[i] < A[i+1]:
                    return False
        return True