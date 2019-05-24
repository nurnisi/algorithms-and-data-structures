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

    def isMonotonic2(self, A):
        return (all(A[i] <= A[i+1] for i in range(len(A)-1)) or 
                all(A[i] >= A[i+1] for i in range(len(A)-1)))

    def isMonotonic3(self, A):
        store = 0
        for i in range(len(A)-1):
            c = cmp(A[i], A[i+1])
            if c:
                if c != store != 0:
                    return False
                store = c
        return True

    def isMonotonic4(self, A):
        increasing = decreasing = True
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                increasing = False
            if A[i] < A[i+1]:
                decreasing = False
        return increasing or decreasing
        