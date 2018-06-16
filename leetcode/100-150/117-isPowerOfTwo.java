    public boolean isPowerOfTwo(int n) {
        int count = 0;
        while (n > 0) {
            if ((n & 1) == 1) count++;
            n >>= 1;
        }
        return count == 1;
    }

    public boolean isPowerOfTwo2(int n) {
        return n>0 && (n&(n-1))==0;
    }