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

    public boolean isPowerOfTwo3(int n) {
        return n>0 && Integer.bitCount()==1;
    }

    public boolean isPowerOfTwo4(int n) {
        while (n!=0 && n%2==0) n/=2;
        return (n==1); 
    }

    public boolean isPowerOfTwo5(int n) {
        return n>0 && (n==1 || (n%2==0 && isPowerOfTwo5(n/2)));
    }

    public boolean isPowerOfTwo6(int n) {
        return n>0 && 1073741824%n==0;
    }
