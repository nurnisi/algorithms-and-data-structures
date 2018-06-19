    public boolean isPowerOfThree(int n) {
        while (n>0 && n%3==0) n/=3;
        return n==1;
    }

    public boolean isPowerOfThree2(int n) {
        return n>0 && (n==1 || (n%3==0 && isPowerOfThree(n/3)));
    }

    public boolean isPowerOfThree3(int n) {
        return Integer.toString(n, 3).matches("^10*$");
    }