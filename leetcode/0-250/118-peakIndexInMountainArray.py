def peakIndexInMountainArray(self, A):
    i = 0
    while i < len(A)-1 and A[i] < A[i+1]: i+=1
    return i

def peakIndexInMountainArray2(self, A):
    for i in range(len(A)):
        if (A[i] > A[i+1]):
            return i


def peakIndexInMountainArray3(self, A):
    lo, hi = 0, len(A)-1
    while lo < hi:
        mi = lo + (hi-lo)/2
        if A[mi] < A[mi+1]: lo = mi+1
        else: hi = mi
    return lo