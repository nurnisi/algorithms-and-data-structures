def peakIndexInMountainArray(self, A):
    i = 0
    while i < len(A)-1 and A[i] < A[i+1]: i+=1
    return i

def peakIndexInMountainArray2(self, A):
    for i in range(len(A)):
        if (A[i] > A[i+1]):
            return i