    public int peakIndexInMountainArray(int[] A) {
        int i = 0, len = A.length;
        while (i < len-1 && A[i] < A[i+1]) i++;
        return i;
    }