    public int peakIndexInMountainArray(int[] A) {
        int i = 0, len = A.length;
        while (i < len-1 && A[i] < A[i+1]) i++;
        return i;
    }

    public int peakIndexInMountainArray2(int[] A) {
        int lo = 0, hi = A.length - 1;
        while (lo < hi) {
            int mi = lo + (hi-lo)/2;
            if (A[mi] < A[mi+1]) lo = mi+1;
            else hi = mi;
        }
        return lo;
    }